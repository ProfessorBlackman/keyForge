from decouple import config


if not config("DEBUG", default=False, cast=bool):
    DATABASE = {
            "NAME": config("RDS_DB_NAME"),
            "USER": config("RDS_USERNAME"),
            "PASSWORD": config("RDS_PASSWORD"),
            "HOST": config("RDS_HOSTNAME"),
            "PORT": config("RDS_PORT"),
    }
else:
    DATABASE = {
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST"),
            "PORT": config("DB_PORT"),
    }