from decouple import config  # type: ignore[import]

DATABASE_URI = config("DATABASE_URI")
SECRET_KEY = config("SECRET_KEY")
