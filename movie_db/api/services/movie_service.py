from ..models import Movie

class MovieService:
    @staticmethod
    def get_filtered_queryset(director_id=None, actor_id=None, genre=None, from_year=None, to_year=None, limit=None):
        queryset = Movie.objects.all()
        
        if director_id:
            queryset = queryset.filter(director__pk=director_id)

        if actor_id:
            queryset = queryset.filter(actors__pk=actor_id)

        if genre:
            queryset = queryset.filter(genres__icontains=genre)
            
        if from_year:
            try:
                fromYear = int(from_year)
                queryset = queryset.filter(year__gte=fromYear)
            except ValueError:
                raise ValueError("from_year must be an integer.")

        if to_year:
            try:
                to_year = int(to_year)
                queryset = queryset.filter(year__lte=to_year)
            except ValueError:
                raise ValueError("to_year must be an integer.")

        if limit:
            try:
                limit = int(limit)
                queryset = queryset[:limit]
            except ValueError:
                raise ValueError("Limit must be an integer.")
            
        return queryset