import datetime
from itertools import islice
import json
import os
import pytz
import time

from django.conf import settings
from django.contrib.gis.geos import Point

from .models import TrackPoint

from firebase import firebase


"""
SELECT COUNT(1) FROM tracks_trackpoint;
SELECT COUNT(1), track_name FROM tracks_trackpoint GROUP BY track_name;
SELECT COUNT(1), device_id FROM tracks_trackpoint GROUP BY device_id;

-- Most active devices
SELECT COUNT(*) AS measurements, COUNT(DISTINCT(track_name)) AS tracks,
  max(sampled_at) AS latest, device_id
  FROM tracks_trackpoint
  GROUP BY device_id
  ORDER BY 3 DESC,2 DESC, 1 DESC;

-- Longest tracks
SELECT ST_Area(ST_Extent(geom)), track_name, device_id
  FROM tracks_trackpoint
  GROUP BY track_name, device_id
  ORDER BY 1 DESC;

-- Find devices that are feeding more or less at the same time
-- This one requires timescaledb extension
SELECT time_bucket('5 minute', sampled_at) AS five_min,
  count(distinct(device_id)) AS device_count
  FROM tracks_trackpoint
  GROUP BY five_min
  HAVING COUNT(distinct(device_id)) > 1
  ORDER BY 2 desc, 1 desc;
"""


def get_all_tracks_from_firebase():
    f_client = firebase.FirebaseApplication(
        settings['FB_STORAGE_BUCKET'],
        None
    )
    result = f_client.get('/tracks_data', None)


def save_json(json_thing, filename, path='/tmp'):
    with open(os.path.sep.join([path, filename]), 'w') as the_file:
        the_file.write(json.dumps(json_thing))


def load_file(file_name='/tmp/thing.json'):
    """
    Returns the json from a valid json file
    """
    thef = open(file_name)
    raw = thef.read()
    result = json.loads(raw)
    return result


def prepare_json_canairio_files_for_db(
    deviceId,
    dirpath='/tmp/canairiobernal'
):
    result = []
    for filename in os.listdir(dirpath):
        full_path = os.path.sep.join([dirpath, filename])
        the_json = load_file(full_path)
        the_json['deviceId'] = deviceId
        track_name = os.path.splitext(filename)[0]
        the_json['name'] = track_name
        result.append(the_json)
    return result


def store_from_path_to_db(deviceId, dirpath='/tmp/canairiobernal'):
    tracks = prepare_json_canairio_files_for_db(deviceId, dirpath)
    for track in tracks:
        dump_track_to_db(track)


def get_latest_tracks_from_firebase():
    f_client = firebase.FirebaseApplication(
        settings['FB_STORAGE_BUCKET'],
        None
    )
    latest_track = TrackPoint.objects.order_by('-created_at').first()
    if not latest_track:
        latest_tracks = f_client.get('/tracks_data', None).values()
    else:
        summary = f_client.get('/tracks_info', None)
        track_names = set(
            filter(lambda x: x > latest_track.track_name, summary)
        )
        latest_tracks = []
        for name in track_names:
            latest_tracks.append(f_client.get('/tracks_data', name))
    return sorted(latest_tracks, key=lambda track: track['name'])


def store_tracks_to_db():
    tracks = get_latest_tracks_from_firebase()
    print('fetched {} tracks'.format(len(tracks)))
    for track in tracks:
        dump_track_to_db(track)
        build_geojson(track['name'], 'sample/data')


def dump_track_to_db(track):
    batch_size = 100
    print('processing {}'.format(track['name']))
    if 'data' not in track:
        print('please delete {}'.format(track))
        return
    sampled_at = datetime.datetime.fromtimestamp(
        point['timestamp'],
        pytz.utc
    )
    points_to_insert = (TrackPoint(
            geom=Point(point['lon'], point['lat']),
            track_name=track['name'],
            device_id=track['deviceId'],
            pm25=point['P25'],
            sampled_at=sampled_at,
        )
        for point in track.get('data', [])
    )
    while True:
        batch = list(islice(points_to_insert, batch_size))
        if not batch:
            break
        TrackPoint.objects.bulk_create(batch, batch_size)


def build_geojson(track_name, path='/tmp/'):
    points = TrackPoint.objects.filter(track_name=track_name)
    build_thing = []
    for point in points:
        line = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [point.geom.x, point.geom.y]
            },
            "properties": {
                "timestamp": time.mktime(point.sampled_at.timetuple()),
                "p25": int(point.pm25)
            }
        }
        build_thing.append(line)
    file_name = os.path.sep.join([path, track_name + '.json'])
    print(file_name)
    with(open(file_name, 'w')) as json_file:
        json.dump(build_thing, json_file)
    return build_thing


def export_from_db_to_dir(path='/tmp/dump_canario_tracks'):
    track_names = TrackPoint.objects.order_by('track_name').values_list(
        'track_name',
        flat=True,
    ).distinct()
    for track_name in track_names:
        build_geojson(track_name[0], path)
