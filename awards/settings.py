from decouple import config  # type: ignore[import]

SECRET_KEY = config("SECRET_KEY")
