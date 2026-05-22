import unittest
from task import conv_endian, conv_num


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

    def test_DefaultEndian(self):
        """Test for default endian value='big'"""
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_integer(self):
        """Test that string integer returns correct val"""
        self.assertEqual(conv_num('12345'), 12345)

    def test_negative_float(self):
        """Tests that neg float string returns correct val"""
        self.assertEqual(conv_num('-123.45'), -123.45)

    def test_leading_decimal(self):
        """Tests that decimal with leading dec will return correct float"""
        self.assertEqual(conv_num('.45'), 0.45)

    def test_trailing_decimal(self):
        """Tests that decimal with trailing dec will return correct float"""
        self.assertEqual(conv_num('123.'), 123.0)

    def test_hex_upper(self):
        """Test that hex in upper case will return correct val"""
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test_hex_lower(self):
        """Test that hex in lower case will return correct val"""
        self.assertEqual(conv_num('0Xad4'), 2772)

    def test_hex_negative(self):
        """Test that negative hex val will return correct integer"""
        self.assertEqual(conv_num('-0xAD4'), -2772)

    def test_invalid_hex(self):
        """Test that invalid hex returns None"""
        self.assertIsNone(conv_num('0xAZ4'))

    def test_invalid_alpha(self):
        """Test that invalid integer string returns None"""
        self.assertIsNone(conv_num('12345A'))

    def test_multiple_decimals(self):
        """Test that a string with invalid decimal returns None"""
        self.assertIsNone(conv_num('12.3.45'))

    def test_empty_string(self):
        """Test that empty string returns None"""
        self.assertIsNone(conv_num(''))

    def test_not_string(self):
        """Test that number that isnt in a string returns None"""
        self.assertIsNone(conv_num(123))

    def test_negative_sign_only(self):
        """Test that string with only negative side returns None"""
        self.assertIsNone(conv_num('-'))

    def test_hex_prefix_only(self):
        """Tests that hex with only prefix returns None"""
        self.assertIsNone(conv_num('0x'))

    def test_returns_int_type(self):
        """Test that that a string with integer returns integer type"""
        self.assertIsInstance(conv_num('12345'), int)

    def test_returns_float_type(self):
        """Test that string with float returns float type"""
        self.assertIsInstance(conv_num('123.45'), float)


if __name__ == '__main__':
    unittest.main()
