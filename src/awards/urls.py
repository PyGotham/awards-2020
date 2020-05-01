from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from users.views import login, magic_login

urlpatterns = [
    # pyre doesn't include stubs for the Django admin.
    # TODO: Determine if we even want to use the admin.
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("admin/", admin.site.urls),  # type: ignore
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("login", login, name="login"),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("login/magic", magic_login, name="magic-login"),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("users/", include("users.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls)),] + urlpatterns
