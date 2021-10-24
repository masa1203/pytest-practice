import unittest


class MyTestCase(unittest.TestCase):
    def test_one(self):
        pass

    def notatest(self):
        """
        "test"の文字列から始まらないと実行されない
        """
        pass


class MySecondeTestCse(unittest.TestCase):
    """
    複数のテストケースを実行できる
    """
    def test_two(self):
        pass

    def test_two_part2(self):
        """
        テストケースは細かく分割できる
        """
        pass


if __name__ == "__main__":
    # テストランナー関数
    unittest.main()
