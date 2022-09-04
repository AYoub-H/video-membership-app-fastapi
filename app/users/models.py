import uuid

from cassandra.cqlengine import columns
from cassandra.cqlenigine.models import Model


class User(Model):
    user_id = columns.UUID(primary_key=True, default=uuid.uuid1)
    email = columns.Text(primary_key=True)
    password = columns.Text()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"User(email={self.email}, user_id={self.user_id})"
