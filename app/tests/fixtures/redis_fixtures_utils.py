import pytest
from redis.redis_dict import RedisDict
from tests.constants import REDIS_FIRST_ELEMENT


@pytest.fixture
def redis_dict_one_item():
    redis_dict = RedisDict()
    redis_dict._contents = {1: REDIS_FIRST_ELEMENT}

    return redis_dict


@pytest.fixture
def redis_dict():
    redis_dict = RedisDict()

    return redis_dict


@pytest.fixture
def redis_dict_begin_trans():
    redis_dict = RedisDict()
    redis_dict._contents = {1: REDIS_FIRST_ELEMENT}
    redis_dict._redis_dict_state = True
    redis_dict.begin_transactions()

    return redis_dict
