from aes import *

def main() :
    aes = AES()

    #Jādzēš tad kad pabeigts testēt
    plaintext = chr(0x00)+chr(0x11)+chr(0x22)+chr(0x33)+chr(0x44)+chr(0x55)+chr(0x66)+chr(0x77)+chr(0x88)+chr(0x99)+chr(0xaa)+chr(0xbb)+chr(0xcc)+chr(0xdd)+chr(0xee)+chr(0xff)
    #

    aes.encrypt(plaintext, AES.KeyInfo.SMALL)

if __name__=="__main__":
    main()