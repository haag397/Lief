from rest_framework import viewsets, status
from rest_framework.response import Response
from barda.app.models import AdminData
from barda.app.serializers import AdminDataSerializer


class AdminDataViewSet(viewsets.ModelViewSet):
    """
    viewing, creating, editing and deleting AdminData instances.
    """

    queryset = AdminData.objects.all()
    serializer_class = AdminDataSerializer

    def list(self, request):
        admin_serializer = AdminDataSerializer(self.queryset, many=True)
        return Response(admin_serializer.data)

    def createt(self, request):
        serializer = AdminDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Handles GET requests to retrieve a single AdminData instance.
        """
        try:
            admin_instance = self.get_object()
            admin_serializer = self.serializer_class(admin_instance)
            return Response(admin_serializer.data)
        except AdminData.DoesNotExist:
            return Response(
                {"error": "AdminData not found."}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk=None):
        """
        Handles PUT requests to update an existing AdminData instance.
        """
        try:
            admin_instance = self.get_object()
            serializer = self.serializer_class(
                admin_instance, data=request.data, partial=True
            )  # partial=True allows partial updates
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AdminData.DoesNotExist:
            return Response(
                {"error": "AdminData not found."}, status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, pk=None):
        """
        Handles DELETE requests to delete an AdminData instance.
        """
        try:
            admin_instance = self.get_object()
            admin_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AdminData.DoesNotExist:
            return Response(
                {"error": "AdminData not found."}, status=status.HTTP_404_NOT_FOUND
            )


#     def perform_create(self, serializer):
#         """
#         Override the perform_create method to handle password hashing or any
#         other logic that should be executed upon creating a new AdminData instance.
#         """
#         admin = serializer.save()
#         admin.set_password(admin.password)  # Ensure password is hashed
#         admin.save()
# # Create your views here.
