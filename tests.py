import unittest
from task import conv_endian


class TestCase(unittest.TestCase):

    # Unit Tests for conv_endian()
    def test_invalidEndian(self):
        """Test for an invalid endian input"""
        self.assertEqual(conv_endian(4, 'lit'), None)

    def test_ConvertZero(self):
        """Test for 0 as input"""
        self.assertEqual(conv_endian(0, 'big'), '00')

    def test_ValidBigE(self):
        """Test for a valid big endian input"""
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_ValidLittleE(self):
        """Test for a valid little endian input"""
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_ValidNegBigE(self):
        """Test for a valid negative big endian input"""
        self.assertEqual(conv_endian(-954786, 'big'), '-0E 91 A2')

    def test_ValidNegLittleE(self):
        """Test for a valid negative little endian input"""
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')


if __name__ == '__main__':
    unittest.main()
