from rest_framework import generics
from .models import Book
from .serializers import BookSerializer,UserSignUpSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .pagination import MyCustomPagination
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

class RegisterUser(APIView):
    def post(self, request, format=None):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            refresh = RefreshToken.for_user(customer)
            return Response({"message": "User created."}) 
        else:
            return Response(serializer.errors)

 
class BookLists(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer
    pagination_class=MyCustomPagination

class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

    def post(self,request,*args,**kwargs):
        response=super().post(request,*args,**kwargs)
        return Response({"message":"book is created"}, status=200)


class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
           return Response({"message":"You don't have the permission to update this book"})
        return super().patch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
           return Response({"message":"You don't have the permission to update this book"})
        return super().put(request, *args, **kwargs)
        


class BookDestroy(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response({"message": "You don't have the permission to delete this book"})
        response = super().delete(request, *args, **kwargs)
        return Response({'message': 'Book is deleted'})
    
