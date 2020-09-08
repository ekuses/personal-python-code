#Standard
import unittest
#Local
import RomanNumConvert

class TestRomanConvert(unittest.TestCase):

    def test_1(self):
        numeral = "I"
        self.assertEqual(RomanNumConvert.roman_to_arabic_num(numeral),1)

    def test_120(self):
        numeral = "CXX"
        self.assertEqual(RomanNumConvert.roman_to_arabic_num(numeral),120)

    def test_444(self):
        numeral = "CDXLIV"
        self.assertEqual(RomanNumConvert.roman_to_arabic_num(numeral),444)

    def test_449(self):
        numeral = "CDXLIX"
        self.assertEqual(RomanNumConvert.roman_to_arabic_num(numeral),449)

    def test_944(self):
        numeral = "CMXLIV"
        self.assertEqual(RomanNumConvert.roman_to_arabic_num(numeral),944)

    def test_994(self):
         numeral = "CMXCIV"
         self.assertEqual(RomanNumConvert.roman_to_arabic_num(numeral),994)

    def test_888(self):
        numeral = "DCCCLXXXVIII"
        self.assertEqual(RomanNumConvert.roman_to_arabic_num(numeral),888)

    def test_empty_string(self):
        numeral = ""
        self.assertEqual(RomanNumConvert.roman_to_arabic_num(numeral),0)

    def test_non_string(self):
        numeral = 1
        self.assertEqual(RomanNumConvert.roman_to_arabic_num(numeral),0)

    @unittest.expectedFailure
    def test_invalid_numeral(self):
        numeral = "XXC"
        self.assertEqual(RomanNumConvert.roman_to_arabic_num(numeral),80)


if __name__ == "__main__":
    unittest.main();
