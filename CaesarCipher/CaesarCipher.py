#currently only take positive offsets
def caesar_encipher(txt,offset):
    if (offset < 0):
        return ""
    true_offset = offset%26

    if(isinstance(txt,str)):
        ret = ""
        for char in txt:
            ascii = ord(char)
            if ( (ascii >= 65) and (ascii<=90) ):
                newascii = (ascii + true_offset) % 91
                if newascii < (90-65):
                    newascii += 65
                newchar = chr(newascii)
                ret = ''.join((ret,newchar))
            elif ( (ascii >= 97) and (ascii <= 122) ):
                newascii = (ascii+true_offset) % 123
                if newascii < (122-97):
                    newascii += 97
                newchar = chr(newascii)
                ret = ''.join((ret,newchar))
            else:
                ret = ''.join((ret,char))
        return ret
    else:
        return ""

#curently does not take negatives
def caesar_decipher(txt,offset):
    if (offset < 0):
        return ""
    true_offset = offset%26
    return caesar_encipher(txt,26-true_offset)

#main function. Created for testing caesar ciper functions.
#Should be removed when unit tests are created
def main():
    #Testfile
    txt = "Hello there my name is Silian and I created this python caesar cipher."
    offset = 1500
    ciphertxt = caesar_encipher(txt,offset)

    print("Text to encrypt is:\t " + txt)
    print("Ciphertext:\t\t " + ciphertxt)
    print("Deciphered Text:\t " + caesar_decipher(ciphertxt,offset))

#if __name__ == "__main__":
    #main()
