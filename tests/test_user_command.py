import pytest

from django.contrib.auth import get_user_model
from django.core.management import call_command


@pytest.mark.django_db
def test_command_createdefaultuser():
    """
    Test user command to create admin user
    """
    call_command('createdefaultuser')

    user = get_user_model().objects.first()

    assert get_user_model().objects.count() == 1
    assert user.username == 'admin'
