import pytest

from app.users.models import User


@pytest.mark.skip()
def test_create_user(setup_db_session):
    User.create_user(email="ayb@gmail.com", password="ayb123")


@pytest.mark.skip()
def tes_duplicate_user_creation(setup_db_session):
    with pytest.raises(Exception):
        User.create_user(email="ayb@gmail.com", password="pwd")
