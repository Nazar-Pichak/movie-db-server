from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class CustomAPIRootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'people': reverse('person-list', request=request),
            'movies': reverse('movie-list', request=request),
            'actors': reverse('actors', request=request),
            'directors': reverse('directors', request=request),
            'genres': reverse('get_genres', request=request),
            'register': reverse('register', request=request),
            'auth': reverse('auth', request=request),
        })