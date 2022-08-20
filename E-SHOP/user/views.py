from user.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializers import UserSerializer


class UsersAPIView(APIView):
    """Creates a new user in the system"""

    serializer_class = UserSerializer

    def get(self, request, pk=None):
        if pk is None:
            users = CustomUser.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        
        user = CustomUser.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"user": serializer.data, "status": status.HTTP_201_CREATED})

        return Response({"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})
