from django.urls import path

from applications.views import scholarship

urlpatterns = [
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("ticket", scholarship, name="scholarship"),
]
