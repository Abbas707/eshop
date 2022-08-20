from django.urls import path
from user.views import UsersAPIView


urlpatterns = [
    path('register/', UsersAPIView.as_view(), name="user_create"),
    path('register/<int:pk>/', UsersAPIView.as_view(), name="user"),
]
