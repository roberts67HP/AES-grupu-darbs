
#Testēšanai. Jāizdzēš tad kad ir pabeigts.
def string_to_bytes (text) :
    bytesList = []
    for char in text :
        bytesList.append(ord(char))
    return bytesList