from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from users.views import login, magic_login

urlpatterns = [
    # pyre doesn't include stubs for the Django admin.
    # TODO: Determine if we even want to use the admin.
    path("admin/", admin.site.urls),  # type: ignore
    path("login", login, name="login"),
    path("login/magic", magic_login, name="magic-login"),
    path("users/", include("users.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls)),] + urlpatterns
