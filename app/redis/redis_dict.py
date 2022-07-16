from redis.redis_dict_state import RedisDictState
import copy


class RedisDict:

    def __init__(self):
        self._contents = {}
        self._transaction_allowed = False
        self._redis_dict_state = None

    def get_content(self, key):
        return self._contents.get(key)

    def set_content(self, key, value):
        key = tuple(key) if isinstance(key, (list, set, dict)) else key
        self._contents[key] = value

    def unset_content(self, key):
        key = tuple(key) if isinstance(key, (list, set, dict)) else key
        return self._contents.pop(key, None)

    def find_content(self, value):
        return [key for key, dict_value in self._contents.items() if dict_value == value]

    def begin_transactions(self):
        if not self._transaction_allowed:
            self._redis_dict_state = RedisDictState(
                copy.deepcopy(self._contents))
            self._transaction_allowed = True

            return self._transaction_allowed, self._redis_dict_state

        return self._transaction_allowed, self._redis_dict_state
