import csv

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from canairio import settings
from tracks.firebase_settings import db


@api_view(['GET'])
def list_tracks(request):
    tracks = db.child("tracks_data")
    tracks = tracks.order_by_child('deviceId').limit_to_first(5).get()
    # @todo:gustavo add filtering
    # @todo:gustavo add sorting
    # @todo:gustavo add pagination
    return Response(tracks.val())


@api_view(['GET'])
def get_track(request, track_id=None):
    output = request.query_params.get('output', None)
    tracks = db.child("tracks_data")
    if not track_id:
        return Response({'message': 'Invalid track_id'}, status=400)

    tracks = tracks.order_by_child('name').equal_to(track_id).get().val()

    if output == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(track_id)

        writer = csv.writer(response)
        data = tracks[track_id]['data']
        writer.writerow(data[0].keys())
        for track in data:
            writer.writerow(track.values())

        return response
    # @todo:gustavo add filtering
    # @todo:gustavo add sorting
    # @todo:gustavo add pagination
    return Response(tracks)


@api_view(['POST'])
def save_track(request):
    track_data = request.data
    # @todo:gustavo how should I choose the identifier for each track?
    db.child(settings.TRACK_COLLECTION_NAME).push(track_data)
    return Response(track_data)
