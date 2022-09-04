from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

from rest_framework.response import Response


class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            data["email"] = (
                get_user_model()
                .objects.filter(email=request.data["email"])
                .first()
                .email
            )
            return Response(data=data)
