from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Movie
from ..serializers import MovieSerializer
from ..services.movie_service import MovieService
from ..permissions import IsStaffOrReadOnly
from django.conf import settings

@api_view(['GET'])
def get_genres(request):
    return Response(settings.GENRES)

class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadOnly] # Přidáno
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized_instance = self.get_serializer(instance).data
        self.perform_destroy(instance)
        return Response(serialized_instance, status=status.HTTP_200_OK)
    
    def list(self, request):
        actor_id = request.GET.get('actorID')
        director_id = request.GET.get('directorID')
        genre = request.GET.get('genre')
        from_year = request.GET.get('fromYear')
        to_year = request.GET.get('toYear')
        limit = request.GET.get('limit')
        
        try:
            queryset = MovieService.get_filtered_queryset(
                director_id=director_id,
                actor_id=actor_id,
                genre=genre,
                from_year=from_year,
                to_year=to_year,
                limit=limit
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)