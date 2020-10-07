from django.test import Client


def client() -> Client:
    return Client()
