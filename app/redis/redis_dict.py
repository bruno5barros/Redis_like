from redis.redis_dict_state import RedisDictState
import copy


class RedisDict:

    def __init__(self):
        self._contents = {}
        self._transaction_allowed = False
        self._redis_dict_state = None

    def get_content(self, key):  # O(1) Constant time
        return self._contents.get(key)

    def get_all_content(self):
        print("List of contents: \n", self._contents)

    def set_content(self, key, value):  # O(1)
        key = tuple(key) if isinstance(key, (list, set, dict)) else key
        self._contents[key] = value

    def unset_content(self, key):  # O(1)
        key = tuple(key) if isinstance(key, (list, set, dict)) else key
        return self._contents.pop(key, None)

    def find_content(self, value):  # O(n) Grow linearly based on n
        return [key for key, dict_value in self._contents.items() if dict_value == value]

    def begin_transactions(self):  # O(n)
        if not self._transaction_allowed:
            self._redis_dict_state = RedisDictState(
                copy.deepcopy(self._contents))
            self._transaction_allowed = True

        return self._transaction_allowed, self._redis_dict_state

    def commit_transations(self):  # O(1)
        if self._transaction_allowed and self._redis_dict_state:
            if self._contents != self._redis_dict_state.get_content_state():
                self._redis_dict_state = None
                self._transaction_allowed = False

                return "Commited."
            elif self._contents == self._redis_dict_state.get_content_state():
                return "NO TRANSACTION"

        return "Transactions are closed."

    def rollback_transations(self):  # O(n) Space Complexity
        if self._transaction_allowed and self._redis_dict_state:
            if self._contents != self._redis_dict_state.get_content_state():
                self._contents = self._redis_dict_state.get_content_state()
                self._redis_dict_state = None
                self._transaction_allowed = False

                return "Rolled back."
            elif self._contents == self._redis_dict_state.get_content_state():
                return "NO TRANSACTION"

        return "Transactions are closed."
