from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic.base import RedirectView, TemplateView

from users.views import login, magic_login

urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="homepage/index.html"), name="homepage"
    ),
    path(
        "admin/login/",
        RedirectView.as_view(
            pattern_name=settings.LOGIN_URL, permanent=True, query_string=True
        ),
    ),
    # pyre doesn't include stubs for the Django admin.
    path("admin/", admin.site.urls),  # type: ignore
    path("apply/", include("applications.urls", namespace="applications")),
    path("login", login, name="login"),
    path("login/magic", magic_login, name="magic-login"),
    # pyre-ignore[16]: Determine why this ignore is needed.
    path("logout", LogoutView.as_view(), name="logout"),
    path("users/", include("users.urls", namespace="users")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
