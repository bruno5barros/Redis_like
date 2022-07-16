class RedisDict:

    def __init__(self):
        self._contents = {}

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
