import uuid

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from app.config import get_settings
from app.users import validators

settings = get_settings()


class User(Model):
    __keyspace__ = settings.keyspace
    user_id = columns.UUID(primary_key=True, default=uuid.uuid1)
    email = columns.Text(primary_key=True)
    password = columns.Text()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"User(email={self.email}, user_id={self.user_id})"

    @staticmethod
    def create_user(email, password=None):
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise Exception("User already exist.")
        valid, message, email = validators.email_validator(email)
        if not valid:
            raise Exception(f"Invalid email: {message}")
        obj = User(email=email)
        obj.password = password
        obj.save()
        return obj
