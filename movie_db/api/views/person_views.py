from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from ..models import Person
from ..serializers import PersonSerializer
from ..services.person_service import PersonService
from ..permissions import IsStaffOrReadOnly

class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadOnly] # Přidáno
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    def list(self, request):
        role = request.GET.get('role')
        limit = request.GET.get('limit')

        try:
            queryset = PersonService.get_filtered_queryset(role=role, limit=limit)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized_instance = self.get_serializer(instance).data
        self.perform_destroy(instance)
        return Response(serialized_instance, status=status.HTTP_200_OK)

    
class RoleListView(generics.ListAPIView):
    serializer_class = PersonSerializer
    role = None

    def get_queryset(self):
        limit = self.request.query_params.get('limit')
        return PersonService.get_filtered_queryset(role=self.role, limit=limit)
    
    
class ActorListView(RoleListView):
    role = 'actor'

class DirectorListView(RoleListView):
    role = 'director'