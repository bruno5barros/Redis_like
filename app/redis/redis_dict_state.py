class RedisDictState:

    def __init__(self, content_state):
        self._content_state = content_state

    def get_content_state(self):
        return self._content_state
