from rest_framework import serializers
from .models import Book,Customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username']


class BookSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['id','title', 'description', 'author', 'price']


class UserSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = Customer
        fields = ["username", "first_name", "last_name", "email", "password", "password2"]

    def save(self):
        reg = Customer(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password should match'})
        reg.set_password(password)
        reg.save()
        return reg