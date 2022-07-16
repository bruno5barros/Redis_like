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
