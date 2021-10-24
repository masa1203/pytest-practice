import unittest


class AdditionTestCase(unittest.TestCase):
    def test_main(self):
        # Arrange
        # ...noting
        # Act
        result = addtion(3, 2)

        # Assert
        assert result == 5
