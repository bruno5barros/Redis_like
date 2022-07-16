import pytest
from redis.redis_dict import RedisDict


class TestRedisDict:

    def test_get_successfuly(self):
        redis_dict = RedisDict()
        redis_dict._content = {1: "First redis element"}

        content = redis_dict.get_content(1)

        assert redis_dict._content.get(1, None) == content

    def test_get_does_not_exit(self):
        redis_dict = RedisDict()
        content = redis_dict.get_content(key=1)

        assert None == content
