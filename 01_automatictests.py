import unittest

class MyTestCase(unittest.TestCase):
    def test_one(self):
        pass

    def notatest(self):
        # "test"の文字列から始まらないと実行されない
        pass

if __name__ == "__main__":
    unittest.main() # テストランナー関数