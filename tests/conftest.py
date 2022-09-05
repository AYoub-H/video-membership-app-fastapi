import pytest

from app import db
from app.users.models import User


@pytest.fixture(scope="module")
def setup_db_session():
    session = db.get_session()
    yield session
    qs = User.objects.filter(email="ayb@gmail.com")
    if qs.count() != 0:
        qs.delete()
    session.shutdown()
