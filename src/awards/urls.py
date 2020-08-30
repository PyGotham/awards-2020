from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic.base import RedirectView, TemplateView

from users.views import login, magic_login

urlpatterns = [
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path(
        "", TemplateView.as_view(template_name="homepage/index.html"), name="homepage"
    ),
    # pyre doesn't include stubs for the Django admin.
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path(
        "admin/login/",
        RedirectView.as_view(
            pattern_name=settings.LOGIN_URL, permanent=True, query_string=True
        ),
    ),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("admin/", admin.site.urls),  # type: ignore
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("apply/", include("applications.urls", namespace="applications")),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("login", login, name="login"),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("login/magic", magic_login, name="magic-login"),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("logout", LogoutView.as_view(), name="logout"),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("users/", include("users.urls", namespace="users")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
