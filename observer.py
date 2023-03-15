import uuid
from tcpsender import TCPSender

class Observer:
    def __init__(self, id=None) -> None:
        if (id is None):
            id = uuid.uuid1()
        self._id = id
        self._sender = TCPSender()

    def update(self, state, source):
        if (source is self._id):
            return
        self._sender.send_data(self.prepare_data(state))

    def prepare_data(self, data):
        data["source"] = self._id
        return data