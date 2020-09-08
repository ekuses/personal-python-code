#Standard
import unittest
#Local
import CaesarCipher

class TestCaesar(unittest.TestCase):

    def test_encipher_short(self):
        txt= "Hello there."
        offset=20
        self.assertEqual(CaesarCipher.caesar_encipher(txt,offset),"Byffi nbyly.")

    def test_encipher_long(self):
        txt =       ("The little cat is majoring in physics in the capital of Byterland."
                    "A piece of sad news comes to him these days: his mother is getting ill."
                    "Being worried about spending so much on railway tickets (Byterland is such a big country,"
                    "and he has to spend 16 shours on train to his hometown), he decided only to send SMS with his mother.")

        enciphered = ("Dro vsddvo mkd sc wktybsxq sx zricsmc sx dro mkzsdkv yp Lidobvkxn."
                    "K zsomo yp ckn xogc mywoc dy rsw droco nkic: rsc wydrob sc qoddsxq svv."
                    "Losxq gybbson klyed czoxnsxq cy wemr yx bksvgki dsmuodc (Lidobvkxn sc cemr k lsq myexdbi,"
                    "kxn ro rkc dy czoxn 16 cryebc yx dbksx dy rsc rywodygx), ro nomsnon yxvi dy coxn CWC gsdr rsc wydrob.")
        offset=400
        self.assertEqual(CaesarCipher.caesar_encipher(txt,offset), enciphered)

    def test_encipher_empty(self):
        txt= ""
        offset=40
        self.assertEqual(CaesarCipher.caesar_encipher(txt,offset),"")

    def test_encipher_no_alphabet(self):
        txt= """1234567890-=!@#$%^&*()_+[]\{}|;':",./<>?"""
        offset=20
        self.assertEqual(CaesarCipher.caesar_encipher(txt,offset),"""1234567890-=!@#$%^&*()_+[]\{}|;':",./<>?""")

    def test_encipher_neg_offset(self):
        txt = "This function should return an empty string regardless of the txt passed in because the function should not take negative offsets right now."
        offset = -20
        self.assertEqual(CaesarCipher.caesar_encipher(txt,offset),"")

    def test_decipher_short(self):
        txt="Byffi nbyly."
        offset=20
        self.assertEqual(CaesarCipher.caesar_decipher(txt,offset),"Hello there.")

    def test_decipher_long(self):
        txt =       ("Dro vsddvo mkd sc wktybsxq sx zricsmc sx dro mkzsdkv yp Lidobvkxn."
                    "K zsomo yp ckn xogc mywoc dy rsw droco nkic: rsc wydrob sc qoddsxq svv."
                    "Losxq gybbson klyed czoxnsxq cy wemr yx bksvgki dsmuodc (Lidobvkxn sc cemr k lsq myexdbi,"
                    "kxn ro rkc dy czoxn 16 cryebc yx dbksx dy rsc rywodygx), ro nomsnon yxvi dy coxn CWC gsdr rsc wydrob.")

        deciphered = ("The little cat is majoring in physics in the capital of Byterland."
                    "A piece of sad news comes to him these days: his mother is getting ill."
                    "Being worried about spending so much on railway tickets (Byterland is such a big country,"
                    "and he has to spend 16 shours on train to his hometown), he decided only to send SMS with his mother.")
        offset=400
        self.assertEqual(CaesarCipher.caesar_decipher(txt,offset),deciphered)

    def test_decipher_empty(self):
        txt=""
        offset=20
        self.assertEqual(CaesarCipher.caesar_decipher(txt,offset),"")

    def test_decipher_no_alphabet(self):
        txt="""1234567890-=!@#$%^&*()_+[]\{}|;':",./<>?"""
        offset=20
        self.assertEqual(CaesarCipher.caesar_decipher(txt,offset),"""1234567890-=!@#$%^&*()_+[]\{}|;':",./<>?""")

    def test_decipher_neg_offset(self):
        txt = "This function should return an empty string regardless of the txt passed in because the function should not take negative offsets right now."
        offset = -20
        self.assertEqual(CaesarCipher.caesar_decipher(txt,offset),"")

    @unittest.skip("Repetitive test")
    def test_decipher2(self):
        txt="Byffi nbyly."
        offset=20
        self.assertEqual(CaesarCipher.caesar_decipher(txt,offset),"Hello there.")


if __name__ == "__main__":
    unittest.main();
