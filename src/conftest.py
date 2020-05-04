from django.test import Client


# pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
def client() -> Client:
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    return Client()
