import pytest
from redis.redis_dict import RedisDict


class TestRedisDict:

    def test_get_content_successfuly(self):
        redis_dict = RedisDict()
        redis_dict._contents = {1: "First redis element"}

        assert redis_dict._contents.get(1, None) == redis_dict.get_content(1)

    def test_get_content_does_not_exit(self):
        redis_dict = RedisDict()

        assert None == redis_dict.get_content(1)

    def test_add_content_successfuly(self):
        redis_dict = RedisDict()
        redis_dict.set_content(1, "First redis element")

        assert redis_dict._contents.get(1, None) == redis_dict.get_content(1)

    def test_add_content_with_existing_key(self):
        redis_dict = RedisDict()
        redis_dict.set_content(1, "First redis element")
        redis_dict.set_content(1, "Updated redis element")

        assert "Updated redis element" == redis_dict.get_content(1)

    def test_add_content_mutable_key(self):
        redis_dict = RedisDict()
        redis_dict.set_content([1], "First redis element")
        redis_dict.set_content({2}, "Second redis element")
        redis_dict.set_content({3: 3}, "Third redis element")

        assert "First redis element" == redis_dict._contents.get((1,))
        assert "Second redis element" == redis_dict._contents.get((2,))
        assert "Third redis element" == redis_dict._contents.get((3,))
