from src.env import db, env

mongo = db.get("mongo")


host_scheme = "mongodb+srv://" if (not env.isLocal and not env.isTest) else "mongodb://"

MONGO = {
    "NAME": mongo["database"],
    "ENGINE": "django_mongodb_backend",
    "USER": mongo["user"],
    "PASSWORD": mongo["pass"],
    "HOST": host_scheme + mongo["host"],
    "PORT": mongo["port"],
    "OPTIONS": {
        "retryWrites": "true",
        "w": "majority",
    },
}
