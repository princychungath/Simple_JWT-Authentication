from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[
    path('',views.BookLists.as_view(),name="book-list"),
    path('create',views.BookCreate.as_view(),name="create"),
    path('update/<int:pk>',views.BookUpdate.as_view(),name="update"),
    path('delete/<int:pk>',views.BookDestroy.as_view(),name="destroy"),
    path('retrieve/<int:pk>',views.BookDetail.as_view(),name="retrieve"),

    path('register',views.RegisterUser.as_view(),name="register"),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]