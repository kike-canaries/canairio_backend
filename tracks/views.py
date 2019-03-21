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


@api_view(['POST'])
def save_track(request):
    track_data = request.data
    # @todo:gustavo how should I choose the identifier for each track?
    db.child(settings.TRACK_COLLECTION_NAME).push(track_data)
    return Response(track_data)
