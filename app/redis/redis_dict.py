class RedisDict:

    def __init__(self):
        self._content = {}

    def get_content(self, key):
        return self._content.get(key, None)
