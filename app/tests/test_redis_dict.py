import pytest
from redis.redis_dict import RedisDict
from tests.constants import REDIS_FIRST_ELEMENT, REDIS_SECOND_ELEMENT, REDIS_THIRD_ELEMENT, REDIS_SAME_ELEMENT


class TestRedisDict:

    def test_get_content_successfuly(self, redis_dict_one_item):
        assert REDIS_FIRST_ELEMENT == redis_dict_one_item.get_content(1)

    def test_get_content_does_not_exit(self, redis_dict):
        assert None == redis_dict.get_content(1)

    def test_add_content_successfuly(self, redis_dict):
        redis_dict.set_content(1, REDIS_FIRST_ELEMENT)

        assert REDIS_FIRST_ELEMENT == redis_dict.get_content(1)

    def test_add_content_with_existing_key(self, redis_dict):
        redis_dict.set_content(1, REDIS_FIRST_ELEMENT)
        redis_dict.set_content(1, "Updated redis element")

        assert "Updated redis element" == redis_dict.get_content(1)

    def test_add_content_mutable_key(self, redis_dict):
        redis_dict.set_content([1], REDIS_FIRST_ELEMENT)
        redis_dict.set_content({2}, REDIS_SECOND_ELEMENT)
        redis_dict.set_content({3: 3}, REDIS_THIRD_ELEMENT)

        assert REDIS_FIRST_ELEMENT == redis_dict._contents.get((1,))
        assert REDIS_SECOND_ELEMENT == redis_dict._contents.get((2,))
        assert REDIS_THIRD_ELEMENT == redis_dict._contents.get((3,))

    def test_remove_content_successfuly(self, redis_dict_one_item):
        assert REDIS_FIRST_ELEMENT == redis_dict_one_item.unset_content(1)

    def test_remove_content_key_doesnt_exists(self, redis_dict_one_item):
        assert None == redis_dict_one_item.unset_content(2)

    def test_remove_content_mutable_key(self, redis_dict):
        redis_dict._contents = {tuple([1]): REDIS_FIRST_ELEMENT, tuple(
            {2}): REDIS_SECOND_ELEMENT, tuple({3: 3}): REDIS_THIRD_ELEMENT}

        assert REDIS_FIRST_ELEMENT == redis_dict.unset_content((1,))
        assert REDIS_SECOND_ELEMENT == redis_dict._contents.get((2,))
        assert REDIS_THIRD_ELEMENT == redis_dict._contents.get((3,))

    def test_search_one_content_value(self, redis_dict_one_item):
        assert [1] == redis_dict_one_item.find_content(REDIS_FIRST_ELEMENT)

    def test_search_content_value_dosent_exists(self, redis_dict_one_item):
        assert [] == redis_dict_one_item.find_content(REDIS_SECOND_ELEMENT)

    def test_search_multiple_content_value(self, redis_dict):
        redis_dict._contents = {tuple([1]): REDIS_SAME_ELEMENT, tuple(
            {2}): REDIS_SAME_ELEMENT, tuple({3: 3}): REDIS_SAME_ELEMENT, tuple({4: 4}): "Fourth redis element"}

        assert [(1,), (2,), (3,)] == redis_dict.find_content(
            REDIS_SAME_ELEMENT)
