from rest_framework import viewsets, status
from rest_framework.response import Response
from barda.core.models import AdminData
from barda.core.serializers import AdminDataSerializer


class AdminDataViewSet(viewsets.ModelViewSet):
    """
    get, create, edit and delete AdminData
    """

    queryset = AdminData.objects.all()
    serializer_class = AdminDataSerializer

    def list(self, request):
        """
        cget all AdminData
        """
        admin_serializer = AdminDataSerializer(self.queryset, many=True)
        return Response(admin_serializer.data)

    def createt(self, request):
        """
        create single AdminData
        """
        serializer = AdminDataSerializer(data=request.data)
        if serializer.is_valid():
            admin = serializer.save()
            # * hash password
            admin.set_password(admin.password)
            admin.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        get single AdminData by id
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
        update single AdminData by id
        """
        try:
            admin_instance = self.get_object()
            serializer = self.serializer_class(
                admin_instance, data=request.data, partial=True
            )
            if serializer.is_valid():
                admin = serializer.save()
                # * hash password
                admin.set_password(admin.password)
                admin.save()
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
