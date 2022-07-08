# Jormungandr - Onboarding
from func.src.services.user_review import UserReviewDataService
from func.src.domain.exceptions import UserUniqueIdNotExists
from .stubs import stub_unique_id

# Third party
from unittest.mock import patch
import pytest


@pytest.mark.asyncio
@patch('func.src.services.user_review.UserRepository.find_one_by_unique_id', return_value=None)
async def test_when_unique_id_not_exists_then_raises(mock_find_one):
    with pytest.raises(UserUniqueIdNotExists):
        await UserReviewDataService.get_registration_data(unique_id=stub_unique_id)


@pytest.mark.asyncio
async def test_when_unique_id_valid_then_return_customer_registration_built():
    result = await UserReviewDataService.get_registration_data(unique_id=stub_unique_id)

    assert isinstance(result, dict)

