import unittest
import threading


class testTODOAcceptance(unittest.TestCase):
    def test_main(self):
        app = TODOApp(io=(self.fake_input, self.fake_output))

        app_thread = threading.Thread(target=app.run, daemon=True)
        app_thread.start()

        self.send_input("quit")
        app_thread.join(timeout=1)
        self.assertEquel(self.get_output(), "Bye!\n")
