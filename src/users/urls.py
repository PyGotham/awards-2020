from django.urls import path

from users.views import profile

app_name = "users"

urlpatterns = [
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("profile", profile, name="profile"),
]
