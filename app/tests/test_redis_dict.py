import pytest
from redis.redis_dict import RedisDict


class TectRedisDict:

    def test_get_successfuly(self):
        RedisDict._content = {1: "First redis element"}

        content = RedisDict.get_content(1)

        assert RedisDict._content == content

    def test_get_does_not_exit(self):
        content = RedisDict.get_content(1)

        assert None == content
