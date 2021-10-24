import unittest


class AdditionTestCase(unittest.TestCase):
    def test_main(self):
        # Arrange
        # ...noting
        # Act
        result = addtion(3, 2)

        # Assert
        assert result == 5


def addtion(*args):
    a1, a2 = args
    return a1 + a2
