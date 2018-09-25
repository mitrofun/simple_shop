import pytest
from apps.category import models


@pytest.mark.django_db
def test_loaded_in_init_test():
    """
    Check loaded data has in test database
    """
    assert models.Category.objects.all().count() > 0
    assert models.Product.objects.all().count() > 0
