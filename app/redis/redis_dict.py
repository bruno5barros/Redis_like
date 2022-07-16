class RedisDict:

    def __init__(self):
        self._contents = {}

    def get_content(self, key):
        return self._contents.get(key)
