from ..models import Person


class PersonService:
    @staticmethod
    def get_filtered_queryset(role=None, limit=None):
        queryset = Person.objects.all()

        if role:
            queryset = queryset.filter(role=role)

        if limit:
            try:
                limit = int(limit)
                queryset = queryset[:limit]
            except ValueError:
                raise ValueError("Limit must be an integer.")

        return queryset