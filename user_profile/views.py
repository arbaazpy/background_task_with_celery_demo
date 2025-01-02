

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer
from .tasks import update_full_name

class UserProfileCreateView(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user_profile = serializer.save()
            # Trigger the background task to update full_name
            update_full_name.delay(user_profile.id, sleep_for=10)
            return Response({
                "id": user_profile.id,
                "first_name": user_profile.first_name,
                "last_name": user_profile.last_name,
                "message": "User created successfully, full_name will be updated in background."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
