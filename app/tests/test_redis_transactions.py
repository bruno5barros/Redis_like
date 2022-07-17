import pytest
from redis.redis_dict import RedisDict
from tests.constants import REDIS_FIRST_ELEMENT, REDIS_SECOND_ELEMENT


class TestRedisTransactions:

    def test_begin_transactions_successfuly(self):
        redis_dict = RedisDict()

        transaction_allowed, redis_state = redis_dict.begin_transactions()

        assert True == transaction_allowed
        assert redis_state.get_content_state() != None

    def test_begin_transactions_twice(self):
        redis_dict = RedisDict()

        transaction_allowed, redis_state = redis_dict.begin_transactions()
        redis_dict._contents = {1: REDIS_FIRST_ELEMENT}
        transaction_allowed2, redis_state2 = redis_dict.begin_transactions()

        assert transaction_allowed == transaction_allowed2
        assert redis_state.get_content_state() == redis_state2.get_content_state()

    def test_commit_transactions_closed(self, redis_dict):
        assert redis_dict.commit_transations() == "Transactions are closed."

    def test_commit_no_transactions(self, redis_dict_one_item):
        redis_dict_one_item.begin_transactions()

        assert redis_dict_one_item.commit_transations() == "NO TRANSACTION"
        assert redis_dict_one_item._transaction_allowed == True
        assert redis_dict_one_item._redis_dict_state.get_content_state(
        ) == redis_dict_one_item._contents

    def test_commit_transactions_successfuly(self, redis_dict_begin_trans):
        redis_dict_begin_trans._contents = {1: REDIS_FIRST_ELEMENT,
                                            tuple({2}): REDIS_SECOND_ELEMENT}

        assert redis_dict_begin_trans.commit_transations() == "Commited."
        assert redis_dict_begin_trans._contents == {1: REDIS_FIRST_ELEMENT,
                                                    tuple({2}): REDIS_SECOND_ELEMENT}
        assert redis_dict_begin_trans._transaction_allowed == False
        assert redis_dict_begin_trans._redis_dict_state == None

    def test_rollback_transactions_closed(self, redis_dict):
        assert redis_dict.rollback_transations() == "Transactions are closed."

    def test_rollback_no_transactions(self, redis_dict_one_item):
        redis_dict_one_item.begin_transactions()

        assert redis_dict_one_item.rollback_transations() == "NO TRANSACTION"
        assert redis_dict_one_item._transaction_allowed == True
        assert redis_dict_one_item._redis_dict_state.get_content_state(
        ) == redis_dict_one_item._contents

    def test_rollback_transactions_successfuly(self, redis_dict_begin_trans):
        redis_dict_begin_trans._contents = {1: REDIS_FIRST_ELEMENT,
                                            tuple({2}): REDIS_SECOND_ELEMENT}

        assert redis_dict_begin_trans.rollback_transations() == "Rolled back."
        assert redis_dict_begin_trans._contents == {1: REDIS_FIRST_ELEMENT}
        assert redis_dict_begin_trans._transaction_allowed == False
        assert redis_dict_begin_trans._redis_dict_state == None
