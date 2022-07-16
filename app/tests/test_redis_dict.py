import pytest
from redis.redis_dict import RedisDict


class TestRedisDict:

    def test_get_content_successfuly(self):
        redis_dict = RedisDict()
        redis_dict._contents = {1: "First redis element"}

        content_value = redis_dict.get_content(1)

        assert redis_dict._contents.get(1, None) == content_value

    def test_get_content_does_not_exit(self):
        redis_dict = RedisDict()
        content_value = redis_dict.get_content(key=1)

        assert None == content_value

    def test_add_content_successfuly(self):
        redis_dict = RedisDict()
        redis_dict.set_content(1, "First redis element")

        content_value = redis_dict._contents.get(1)

        assert redis_dict._contents.get(1, None) == content_value

    def test_add_content_with_existing_key(self):
        redis_dict = RedisDict()
        redis_dict.set_content(1, "First redis element")
        redis_dict.set_content(1, "Second redis element")

        content_value = redis_dict._contents.get(1)

        assert "Second redis element" == content_value

    def test_add_content_mutable_key(self):
        redis_dict = RedisDict()
        redis_dict.set_content([1], "First redis element")

        content_value = redis_dict._contents.get((1,))

        assert "First redis element" == content_value
