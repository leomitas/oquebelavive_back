from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("user/", views.UserView.as_view()),
    # path("user/<int:id>/", views.UserDetailView.as_view()),
    path("user/login/", jwt_views.TokenObtainPairView.as_view()),
]