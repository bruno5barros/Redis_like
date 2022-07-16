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

    def test_remove_content_successfuly(self):
        redis_dict = RedisDict()
        redis_dict._contents = {1: "First redis element"}

        assert "First redis element" == redis_dict.unset_content(1)

    def test_remove_content_key_doesnt_exists(self):
        redis_dict = RedisDict()
        redis_dict._contents = {1: "First redis element"}

        assert None == redis_dict.unset_content(2)

    def test_remove_content_mutable_key(self):
        redis_dict = RedisDict()
        redis_dict._contents = {tuple([1]): "First redis element", tuple(
            {2}): "Second redis element", tuple({3: 3}): "Third redis element"}

        assert "First redis element" == redis_dict.unset_content((1,))
        assert "Second redis element" == redis_dict._contents.get((2,))
        assert "Third redis element" == redis_dict._contents.get((3,))

    def test_search_one_content_value(self):
        redis_dict = RedisDict()
        redis_dict._contents = {1: "First redis element"}

        assert [1] == redis_dict.find_content("First redis element")

    def test_search_content_value_dosent_exists(self):
        redis_dict = RedisDict()
        redis_dict._contents = {1: "First redis element"}

        assert [] == redis_dict.find_content("Second redis element")

    def test_search_multiple_content_value(self):
        redis_dict = RedisDict()
        redis_dict._contents = {tuple([1]): "Same element", tuple(
            {2}): "Same element", tuple({3: 3}): "Same element", tuple({4: 4}): "Fourth redis element"}

        assert [(1,), (2,), (3,)] == redis_dict.find_content("Same element")

    def test_begin_transactions_successfuly(self):
        redis_dict = RedisDict()

        transaction_allowed, redis_state = redis_dict.begin_transactions()

        assert True == transaction_allowed
        assert redis_state.get_content_state() != None

    def test_begin_transactions_twice(self):
        redis_dict = RedisDict()

        transaction_allowed, redis_state = redis_dict.begin_transactions()
        redis_dict._contents = {1: "First redis element"}
        transaction_allowed2, redis_state2 = redis_dict.begin_transactions()

        assert transaction_allowed == transaction_allowed2
        assert redis_state.get_content_state() == redis_state2.get_content_state()

    def test_commit_transactions_closed(self):
        redis_dict = RedisDict()

        assert redis_dict.commit_transations() == "Transactions are closed."

    def test_commit_no_transactions(self):
        redis_dict = RedisDict()
        redis_dict._contents = {1: "First redis element"}
        transaction_allowed, redis_state = redis_dict.begin_transactions()

        assert redis_dict.commit_transations() == "NO TRANSACTION"
        assert redis_dict._transaction_allowed == True
        assert redis_dict._redis_dict_state.get_content_state() == redis_dict._contents

    def test_commit_transactions_successfuly(self):
        redis_dict = RedisDict()
        redis_dict._contents = {1: "First redis element"}
        redis_dict._redis_dict_state = True
        transaction_allowed, redis_state = redis_dict.begin_transactions()
        redis_dict._contents = {1: "First redis element",
                                tuple({2}): "Second redis element"}

        assert redis_dict.commit_transations() == "Commited."
        assert redis_dict._contents == {1: "First redis element",
                                        tuple({2}): "Second redis element"}
        assert redis_dict._transaction_allowed == False
        assert redis_dict._redis_dict_state == None
