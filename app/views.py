from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Organisation
from .serializers import UserSerializer, OrganisationSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance
        refresh = RefreshToken.for_user(user)
        return Response({
            "status": "success",
            "message": "Registration successful",
            "data": {
                "accessToken": str(refresh.access_token),
                "user": UserSerializer(user).data
            }
        }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "status": "success",
                "message": "Login successful",
                "data": {
                    "accessToken": str(refresh.access_token),
                    "user": UserSerializer(user).data
                }
            }, status=status.HTTP_200_OK)
        return Response({
            "status": "Bad request",
            "message": "Authentication failed",
            "statusCode": 401
        }, status=status.HTTP_401_UNAUTHORIZED)

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class OrganisationListView(generics.ListAPIView):
    serializer_class = OrganisationSerializer

    def get_queryset(self):
        user = self.request.user
        return user.organisations.all()

class OrganisationDetailView(generics.RetrieveAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_field = 'orgId'

class CreateOrganisationView(generics.CreateAPIView):
    serializer_class = OrganisationSerializer

    def perform_create(self, serializer):
        serializer.save()

class AddUserToOrganisationView(generics.GenericAPIView):
    def post(self, request, orgId, *args, **kwargs):
        org = Organisation.objects.get(orgId=orgId)
        user = User.objects.get(userId=request.data['userId'])
        org.users.add(user)
        return Response({
            "status": "success",
            "message": "User added to organisation successfully",
        }, status=status.HTTP_200_OK)