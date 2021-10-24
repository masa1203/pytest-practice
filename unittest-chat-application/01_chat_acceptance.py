import unittest
import unittest.mock
from multiprocessing.managers import SyncManager


class Connection(SyncManager):
    def __init__(self, address):
        self.register("get_messages")
        super().__init__(address=address, authkey=b'mychatsecret')
        self.connect()

    def broadcast(self, message):
        messages = self.get_messages()
        messages.append(message)


class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname

    def send_message(self, message):
        sent_message = "{}: {}".format(self.nickname, message)
        self.connection.broadcast(message)
        return sent_message


class TestConnection(unittest.TestCase):
    def test_broadcast(self):
        with unittest.mock.patch.object(Connection, "connect"):
            c = Connection(("localhost", 9090))
        with unittest.mock.patch.object(c, "get_messages", return_value=[]):
            c.broadcast("some message")
        assert c.get_messages()[-1] == "some message"


class TestChatClient(unittest.TestCase):
    def test_nickname(self):
        client = ChatClient("User 1")

        assert client.nickname == "User 1"

    def test_send_message(self):
        client = ChatClient("User 1")
        client.connection = unittest.mock.Mock()
        sent_message = client.send_message("This is test message")

        assert sent_message == "User 1: This is test message"


class TestChatAcceptance(unittest.TestCase):
    def test_message_exchange(self):
        user1 = ChatClient("Masayoshi")
        user2 = ChatClient("Nakagawa")

        user1.send_message("Hello World!")
        messages = user2.fetch_messages()

        assert messages == ["Masayoshi: Hello World"]


if __name__ == "__main__":
    unittest.main()
