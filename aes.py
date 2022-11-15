import random
import enum

from testing import *

s_box = (
    (0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5,
     0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76),
    (0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0,
     0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0),
    (0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC,
     0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15),
    (0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A,
     0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75),
    (0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0,
     0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84),
    (0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B,
     0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF),
    (0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85,
     0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8),
    (0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5,
     0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2),
    (0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17,
     0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73),
    (0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88,
     0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB),
    (0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C,
     0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79),
    (0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9,
     0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08),
    (0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6,
     0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A),
    (0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E,
     0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E),
    (0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94,
     0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF),
    (0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68,
     0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16)
)

inv_s_box = (
    (0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38,
     0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB),
    (0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87,
     0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB),
    (0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D,
     0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E),
    (0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2,
     0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25),
    (0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16,
     0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92),
    (0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA,
     0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84),
    (0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A,
     0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06),
    (0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02,
     0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B),
    (0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA,
     0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73),
    (0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85,
     0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E),
    (0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89,
     0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B),
    (0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20,
     0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4),
    (0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31,
     0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F),
    (0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D,
     0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF),
    (0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0,
     0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61),
    (0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26,
     0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D)
)


class Block:
    # Izkārtojums 2d sarakstā (balstoties uz FIPS pdf)
    # in0 in4 in8 in12
    # in1 in5 in9 in13
    # in2 in6 in10 in14
    # in3 in7 in11 in15

    def __init__(self, byteList, gridSize):
        self.list = []
        byteListIndex = 0
        for y in range(gridSize):
            col = []
            for x in range(gridSize):
                if byteListIndex < len(byteList):
                    col.append(byteList[byteListIndex])
                    byteListIndex += 1
                else:
                    col.append(0)
            self.list.append(col)

    def printBytes(self):
        for col in self.list:
            for byte in col:
                print(hex(byte)+", ", end="")
        print()


class Blocks:
    def __init__(self, plaintext, gridSize):
        self.list = []

        startIndex = 0
        endIndex = gridSize * gridSize

        while True:
            # plainTextBytes = bytes(plaintext[startIndex : endIndex], 'utf-8')
            plainTextBytes = plaintext

            self.list.append(Block(plainTextBytes, gridSize))
            startIndex += gridSize * gridSize
            endIndex += gridSize * gridSize
            if endIndex > len(plaintext):
                break

    def printBlocks(self):
        for block in self.list:
            block.printBytes()

class AES:
    # Nav vēl kārtīgi implementēts
    class KeyInfo (enum.Enum):
        SMALL = 128, 10,
        MEDIUM = 192, 12,
        LARGE = 256, 14

        def __init__ (self, bitSize, rounds) :
            self.bitSize = bitSize
            self.rounds = rounds

    class EncryptedCipherText :
        def __init__ (self, cipheredText, keyInfo, initialKey, roundKeys, finalKey) :
            self.cipheredTextBlocks = cipheredText
            self.keyInfo = keyInfo
            self.initialKey = initialKey
            self.roundKeys = roundKeys
            self.finalKey = finalKey

    def encrypt (self, plaintext, keyInfo = KeyInfo.SMALL) :
        plainTextBlocks = Blocks(plaintext, 4)
        initialKeyBlock = None
        roundKeyBlocks = []
        finalKeyBlock = None
        firstLoop = True

        for block in plainTextBlocks.list:
            if firstLoop :
                initialKeyBlock = self.generate_key(keyInfo.bitSize)
            self.add_round_key(block, initialKeyBlock)
            self.sub_bytes(block)
            self.shift_rows(block)
            self.mix_columns(block)

            roundIndex = 0
            while roundIndex < keyInfo.rounds - 1 :
                if firstLoop :
                    roundKeyBlocks.append(self.generate_key(keyInfo.bitSize))

                self.sub_bytes(block)
                self.shift_rows(block)
                self.mix_columns(block)
                self.add_round_key(block, roundKeyBlocks[roundIndex])

                roundIndex += 1
            self.sub_bytes(block)
            self.shift_rows(block)
            if firstLoop :
                finalKeyBlock = self.generate_key(keyInfo.bitSize)
            self.add_round_key(block, finalKeyBlock)
            firstLoop = False
        
        return AES.EncryptedCipherText(plainTextBlocks, keyInfo, initialKeyBlock, roundKeyBlocks, finalKeyBlock)

    def decrypt (self, encrCiphertext) :
        for block in encrCiphertext.cipheredTextBlocks.list :
            self.add_round_key(block, encrCiphertext.finalKey)
            self.sub_bytes(block)
            self.shift_rows(block)
            self.mix_columns(block)

            roundIndex = len(encrCiphertext.roundKeys)
            while roundIndex > 0 :
                self.sub_bytes(block)
                self.shift_rows(block)
                self.mix_columns(block)
                self.add_round_key(block, encrCiphertext.roundKeys[roundIndex - 1])

                roundIndex -= 1
            self.sub_bytes(block)
            self.shift_rows(block)
            self.add_round_key(block, encrCiphertext.initialKey)
        
        plaintext = ""

        for block in encrCiphertext.cipheredTextBlocks.list :
            for col in block.list :
                for byte in col :
                    plaintext += chr(byte)
        return plaintext

    def encrypt_test (self):
        keyInfo = AES.KeyInfo.SMALL
        plainTextBlocks = Blocks(bytes([
            0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77,
            0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff
        ]), 4)
        initialKeyBlock = Block(bytes([
            0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
            0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f
        ]), 4)

        print("\nPlaintext before = ", end=" ")
        plainTextBlocks.printBlocks()
        print("\nInitial key = ", end=" ")
        initialKeyBlock.printBytes()

        for block in plainTextBlocks.list:
            self.add_round_key(block, initialKeyBlock)

            self.sub_bytes(block)
            print("\nPlaintext after sub bytes = ", end=" ")
            plainTextBlocks.printBlocks()
            self.shift_rows(block)
            print("\nPlaintext after shift rows = ", end=" ")
            plainTextBlocks.printBlocks()
            self.mix_columns(block)
            print("\nPlaintext after mix columns = ", end=" ")
            plainTextBlocks.printBlocks()

            # roundIndex = 0
            # while roundIndex < keyInfo.rounds - 1 :
            #     roundKeyBlock = self.generate_key(keyInfo.bitSize)
            # self.sub_bytes(block)
            #     self.shift_rows(block)
            #     self.mix columns(block)
            #     self.add_round_key(block, roundKeyBlock)
            # roundIndex += 1
            # self.sub_bytes(block)
            # self.shift_rows(block)
            # finalKeyBlock = self.generate_key(keyInfo.bitSize)
            # self.add_round_key(block, finalKeyBlock)

        print("Plaintext After = ", end="")
        plainTextBlocks.printBlocks()

    def decrypt_test(self):
        keyInfo = AES.KeyInfo.SMALL
        cipherTextBlocks = Blocks(bytes([
            0x8e, 0xa2, 0xb7, 0xca, 0x51, 0x67, 0x45, 0xbf,
            0xea, 0xfc, 0x49, 0x90, 0x4b, 0x49, 0x60, 0x89
        ]), 4)
        initialKeyBlock = Block(bytes([
            0x24, 0xfc, 0x79, 0xcc, 0xbf, 0x09, 0x79, 0xe9,
            0x37, 0x1a, 0xc2, 0x3c, 0x6d, 0x68, 0xde, 0x36
        ]), 4)

        print("\nCiphertext before = ", end=" ")
        cipherTextBlocks.printBlocks()
        print("\nInitial key = ", end=" ")
        initialKeyBlock.printBytes()

        for block in cipherTextBlocks.list:
            self.add_round_key(block, initialKeyBlock)
            print("\nCiphertext after round key = ", end=" ")
            cipherTextBlocks.printBlocks()

            self.inv_shift_rows(block)
            print("\nCiphertext after inv shift rows = ", end=" ")
            cipherTextBlocks.printBlocks()

            self.inv_sub_bytes(block)
            print("\nCiphertext after inv sub bytes = ", end=" ")
            cipherTextBlocks.printBlocks()

            self.inv_mix_columns(block)
            print("\nCiphertext after inv mix columns = ", end=" ")
            cipherTextBlocks.printBlocks()

    def generate_key(self, size):
        random.seed()
        return Block(random.randbytes(int(size / 8)), 4)

    def add_round_key(self, plaintextBlock, keyBlock):
        for y in range(len(plaintextBlock.list)):
            plaintextCol = plaintextBlock.list[y]
            keyBlockCol = keyBlock.list[y]
            for x in range(len(plaintextCol)):
                # xor katram baitam
                plaintextCol[x] ^= keyBlockCol[x]

    def sub_bytes(self, plaintextBlock):
        for y in range(len(plaintextBlock.list)):
            plaintextCol = plaintextBlock.list[y]
            for x in range(len(plaintextCol)):
                byte = plaintextCol[x]
                # tiek iegūta baita kreisā daļa un labā daļa
                byteLeft = (byte & 0xF0) >> 4
                byteRight = byte & 0x0F
                # no s_box iegūst konkrēto baitu ar abām daļām
                plaintextCol[x] = s_box[byteLeft][byteRight]

    def inv_sub_bytes(self, ciphertextBlock) :
        for y in range(len(ciphertextBlock.list)):
            ciphertextCol = ciphertextBlock.list[y]
            for x in range(len(ciphertextCol)):
                byte = ciphertextCol[x]
                # tiek iegūta baita kreisā daļa un labā daļa
                byteLeft = (byte & 0xF0) >> 4
                byteRight = byte & 0x0F
                # no inv_s_box iegūst konkrēto baitu ar abām daļām
                ciphertextCol[x] = inv_s_box[byteLeft][byteRight]

    def shift_rows(self, plaintextBlock):
        shiftAmount = 0
        for rowIndex in range(4):
            # Izveido jaunu sarakstu un pievieno baitus no plaintext bloka rindas
            tempRowBytes = []
            for col in plaintextBlock.list:
                tempRowBytes.append(col[rowIndex])

            # Pabīdīšana pa kreisi
            shiftCount = 0
            while shiftCount < shiftAmount:
                byte = tempRowBytes.pop(0)
                tempRowBytes.append(byte)
                shiftCount += 1

            # Aizvieto rindas iepriekšējo plaintext baitu secību ar jauno
            tempRowByteIndex = 0
            for col in plaintextBlock.list:
                col[rowIndex] = tempRowBytes[tempRowByteIndex]
                tempRowByteIndex += 1

            shiftAmount += 1

    def inv_shift_rows(self, ciphertextBlock):
        shiftAmount = 0
        for rowIndex in range(4):
            # Izveido jaunu sarakstu un pievieno baitus no ciphertext bloka rindas
            tempRowBytes = []
            for col in ciphertextBlock.list:
                tempRowBytes.append(col[rowIndex])

            # Pabīdīšana pa labi
            shiftCount = 0
            while shiftCount < shiftAmount:
                byte = tempRowBytes.pop()
                tempRowBytes.insert(0, byte)
                shiftCount += 1

            # Aizvieto rindas iepriekšējo ciphertext baitu secību ar jauno
            tempRowByteIndex = 0
            for col in ciphertextBlock.list:
                col[rowIndex] = tempRowBytes[tempRowByteIndex]
                tempRowByteIndex += 1

            shiftAmount += 1

    def mix_columns(self, plaintextBlock):
        #                   col0 col1 col2 col3
        # row0 [2  3  1  1] [0x63 0x9  0xcd 0xba]
        # row1 [1  2  3  1]X[0x53 0x60 0x70 0xca] = xor(row[i] x column[i]) = [?]
        # row2 [1  1  2  3] [0xe0 0xe1 0xb7 0xd0]
        # row3 [3  1  1  2] [0x8c 0x4  0x51 0xe7]
        multipliers = [
            [2, 3, 1, 1],
            [1, 2, 3, 1],
            [1, 1, 2, 3],
            [3, 1, 1, 2]
        ]
        # iterē cauri katrai plaintext vērtībai
        tempText = []
        resArr = []
        for col in plaintextBlock.list:
            tempRowBytes = []
            for rowIndex in range(4):
                tempRowBytes.append(col[rowIndex])
            tempText.append(tempRowBytes)
        # prints values for debug purpose
        num = 0

        for y in range(4):
            for x in range(4):
                # print("On value ", hex(tempText[y][x]), " at x - ", x, "  y - ", y)
                res = 0
                # kā matricu sareizina multis rindas ar plaintext kolonnām, bet skaitīšanas vietā XOR sareizināto. Piem. (2*63 XOR 3*53 XOR 1*e0 XOR 1*8c)
                for z in range(4):
                    num = 0
                    # print("Z loop start value - ", hex(tempText[y][z]))
                    if (multipliers[x][z] == 1):
                        # print("multi is 1")
                        num = tempText[y][z]
                        # print(hex(num))
                    elif (multipliers[x][z] == 2):
                        # print("multi is 2")
                        num = (2 * tempText[y][z])
                        # print(hex(num))
                    # ja reizinātājs ir 3, tad rēķina šādi: 2 * vērtība XOR vērtība. Piem. 3 * ab = (2 * ab) XOR ab
                    elif (multipliers[x][z] == 3):
                        # print("multi is 3")
                        num = (2 * tempText[y][z]) ^ tempText[y][z]
                        # print(hex(num))
                        # ja reizinot ir overflow (skaitlis >255 (>ff in hex)), tad rezultātu XOR ar 1b (27). (var izpildīties tikai tad, ja reizina ar 2 vai 3)
                    if (num > 255):
                        # print("XOR by 1b")
                        num = num ^ 27
                        # print(hex(num))
                    # ja vēl joprojām ir overflow (skaitlis >255  (>ff in hex)), tad overflow ciparu nomet nost (vērtība = 256 % vērtība.)
                    if (num > 255):
                        # print("Removing overflow")
                        num %= 256
                        # print(hex(num))
                    res ^= num
                # print("After Column Mix value ", hex(res))
                resArr.append(res)
        tempRowByteIndex = 0
        for col in plaintextBlock.list:
            for rowIndex in range(4):     
                col[rowIndex] = resArr[tempRowByteIndex]
                tempRowByteIndex += 1

    def inv_mix_columns (self, ciphertextBlock) :
        multipliers = [
            [14, 11, 13, 9],
            [9, 14, 11, 13],
            [13, 9, 14, 11],
            [11, 13, 9, 14]
        ]
        tempText = []
        resArr = []
        for col in ciphertextBlock.list:
            tempRowBytes = []
            for rowIndex in range(4):
                tempRowBytes.append(col[rowIndex])
            tempText.append(tempRowBytes)
        # prints values for debug purpose
        num = 0

        for y in range(4):
            for x in range(4):
                print("On value ", hex(tempText[y][x]), " at x - ", x, "  y - ", y)
                res = 0
                for z in range(4):
                    num = 0
                    print("Z loop start value - ", hex(tempText[y][z]))
                    if (multipliers[x][z] == 9):
                        print("multi is 9")
                        num = (((tempText[y][z] * 2) * 2) * 2) ^ tempText[y][z]
                        print(hex(num))
                    elif (multipliers[x][z] == 11):
                        print("multi is 11")
                        num = ((((tempText[y][z] * 2) * 2) ^ tempText[y][z]) * 2) ^ tempText[y][z]
                        print(hex(num))
                    elif (multipliers[x][z] == 13):
                        print("multi is 13")
                        num = ((((tempText[y][z] * 2) ^ tempText[y][z]) * 2) * 2) ^ tempText[y][z]
                        print(hex(num))
                    elif (multipliers[x][z] == 14):
                        print("multi is 14")
                        num = ((((tempText[y][z] * 2) ^ tempText[y][z]) * 2) ^ tempText[y][z]) * 2
                        print(hex(num))
                    if (num > 255):
                        print("XOR by 1b")
                        num = num ^ 27
                        print(hex(num))
                    # ja vēl joprojām ir overflow (skaitlis >255  (>ff in hex)), tad overflow ciparu nomet nost (vērtība = 256 % vērtība.)
                    if (num > 255):
                        print("Removing overflow")
                        num %= 256
                        print(hex(num))
                    res ^= num
                # print("After Column Mix value ", hex(res))
                resArr.append(res)
        tempRowByteIndex = 0
        for col in ciphertextBlock.list:
            for rowIndex in range(4):     
                col[rowIndex] = resArr[tempRowByteIndex]
                tempRowByteIndex += 1