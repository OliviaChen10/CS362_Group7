import unittest
from task import conv_endian, my_datetime, conv_num


class TestCase(unittest.TestCase):

    def test_invalid_endian(self):
        """Test for an invalid endian input"""
        self.assertEqual(conv_endian(4, 'lit'), None)

    def test_zero_bigE(self):
        """Test for 0 as input for big endian"""
        self.assertEqual(conv_endian(0, 'big'), '00')

    def test_zero_littleE(self):
        """Test for 0 as an input for little endian"""
        self.assertEqual(conv_endian(0, 'little'), '00')

    def test_zero_default_endian(self):
        """Test for 0 with the default endian value"""
        self.assertEqual(conv_endian(0), '00')

    def test_valid_bigE(self):
        """Test for a valid big endian input"""
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_valid_littleE(self):
        """Test for a valid little endian input"""
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_valid_neg_bigE(self):
        """Test for a valid negative big endian input"""
        self.assertEqual(conv_endian(-954786, 'big'), '-0E 91 A2')

    def test_valid_neg_littleE(self):
        """Test for a valid negative little endian input"""
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test_default_endian(self):
        """Test for default endian value='big'"""
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_large_number_bigE(self):
        """Test to convert a large number to hex (big E)"""
        self.assertEqual(conv_endian(784653299378, 'big'), 'B6 B0 FB 2E B2')

    def test_large_number_littleE(self):
        """Test to convert a large number to hex (little E)"""
        self.assertEqual(conv_endian(784653299378, 'little'), 'B2 2E FB B0 B6')

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

    def test_large_time(self):
        """Tests for a large datetime."""
        self.assertEqual(my_datetime(98765432100), "10-02-5099")

    def test_month_upper(self):
        """Tests for the ending of the month."""
        self.assertEqual(my_datetime(86400 * 30), "01-31-1970")

    def test_month_lower(self):
        """Tests for the beginning of the month."""
        self.assertEqual(my_datetime(86400 * 31), "02-01-1970")

    def test_new_year(self):
        """Tests that the New Year's Day will return the correct value."""
        self.assertEqual(my_datetime(86400 * 365), "01-01-1971")

    def test_last_day(self):
        """Tests that the last day of the year will return the correct value."""
        self.assertEqual(my_datetime(86400 * 364), "12-31-1970")

    def test_last_30day(self):
        """Tests that the last day of a month with 30 days will return the correct value."""
        self.assertEqual(my_datetime(86400 * 180), "06-30-1970")

    def test_last_31day(self):
        """Tests that the last day of a month with 31 days will return the correct value."""
        self.assertEqual(my_datetime(86400 * 150), "05-31-1970")

    def test_leap_year(self):
        """Tests that the boundary for leap year is correct."""
        self.assertEqual(my_datetime(68169600), "02-29-1972")

    def test_dayafter_leap(self):
        """Tests that the day after leap year will return the correct value."""
        self.assertEqual(my_datetime(68256000), "03-01-1972")

    def test_leapyear_boundary(self):
        """Tests that the leap year boundary will return the correct value."""
        self.assertEqual(my_datetime(68083200), "02-28-1972")

    def test_date_time(self):
        """Tests that the date time will return correctly."""
        self.assertEqual(my_datetime(2578960), "01-30-1970")

    def test_start_year(self):
        """Tests that the starting date is correct."""
        self.assertEqual(my_datetime(0), "01-01-1970")

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
