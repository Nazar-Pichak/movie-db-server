from django.urls import path, include, re_path
from .views.person_views import PersonViewSet
from rest_framework.routers import DefaultRouter

from .views.person_views import ActorListView, DirectorListView
from .views.auth_views import RegisterUserView, AuthView
from .views.movie_views import MovieViewSet, get_genres

class CustomRouter(DefaultRouter):
    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'


router = CustomRouter()
router.register(r'people', PersonViewSet, basename='person')
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('', include(router.urls)),
    path('actors/', ActorListView.as_view(), name='actors'),
    path('directors/', DirectorListView.as_view(), name='directors'),
    path('genres/', get_genres, name="get_genres"),
    re_path(r'^user/?$', RegisterUserView.as_view(), name='register'),
    re_path(r'^auth/?$', AuthView.as_view(), name='auth'),
]