from django.urls import path
from users.views import profile

urlpatterns = [
    path("profile", profile, name="profile"),
]
