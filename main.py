from aes import *

def main() :
    aes = AES()

    #aes.encrypt_test()
    aes.decrypt_test()

    # test = "asdasdasd"
    # encrCiphertext = aes.encrypt(test, AES.KeyInfo.SMALL)
    # resPlaintext = aes.decrypt(encrCiphertext)
    # print(resPlaintext)

if __name__=="__main__":
    main()




# round[ 0].input 00112233445566778899aabbccddeeff
# round[ 0].k_sch 000102030405060708090a0b0c0d0e0f
# round[ 1].start 00102030405060708090a0b0c0d0e0f0
# round[ 1].s_box 63cab7040953d051cd60e0e7ba70e18c
# round[ 1].s_row 6353e08c0960e104cd70b751bacad0e7
# round[ 1].m_col 5f72641557f5bc92f7be3b291db9f91a
# round[ 1].k_sch d6aa74fdd2af72fadaa678f1d6ab76fe
# round[ 2].start 89d810e8855ace682d1843d8cb128fe4
# round[ 2].s_box a761ca9b97be8b45d8ad1a611fc97369
# round[ 2].s_row a7be1a6997ad739bd8c9ca451f618b61
# round[ 2].m_col ff87968431d86a51645151fa773ad009





# round[ 0].iinput 8ea2b7ca516745bfeafc49904b496089
# round[ 0].ik_sch 24fc79ccbf0979e9371ac23c6d68de36
# round[ 1].istart aa5ece06ee6e3c56dde68bac2621bebf
# round[ 1].is_row aa218b56ee5ebeacdd6ecebf26e63c06
# round[ 1].is_box 627bceb9999d5aaac945ecf423f56da5
# round[ 1].ik_sch 4e5a6699a9f24fe07e572baacdf8cdea
# round[ 1].ik_add 2c21a820306f154ab712c75eee0da04f
# round[ 2].istart d1ed44fd1a0f3f2afa4ff27b7c332a69
# round[ 2].is_row d133f22a1aed2a7bfa0f44697c4f3ffd
# round[ 2].is_box 516604954353950314fb86e401922521
#0x8e, 0xa2, 0xb7, 0xca, 0x51, 0x67, 0x45, 0xbf, 0xea, 0xfc, 0x49, 0x90, 0x4b, 0x49, 0x60, 0x89