import math, sys

class Cryptogram:
    def __init__(self, cryptogram):        
        self.chars = [chr(int(char, 2)) for char in str(cryptogram).strip().split(' ')]

    def __len__(self):
        return len(self.chars)
    
    def getChar(self, index):
        return self.chars[index]


class Decryptor:
    def __init__(self, data, lines):
        lettersCount = {
            "A": 721, "d": 12864, "a": 34660, "m": 11290, " ": 77607,
            "M": 616, "i": 32622, "c": 15615, "k": 13767, "e": 27987,
            "w": 16569, "z": 25099, "P": 1334, "n": 17496, "T": 996,
            "u": 8639, "s": 16972, "y": 15193, "l": 7540, "o": 25960,
            "t": 12129, "j": 7351, "L": 352, "K": 733, "ę": 5953, 
            "g": 5326, "p": 9242, "r": 17350, "G": 372, "ó": 3467,
            "—": 1305, "S": 1078, ",": 9598, "ł": 10823, "W": 1324, "O": 591,
            "b": 6362, "R": 545, "E": 37, "!": 1083, ":": 1355, "I": 848,
            "ć": 2165, ".": 3456, "D": 586, "J": 760, "C": 568, "h": 4290,
            "B": 594, "N": 825, "(": 317, "f": 524, ";": 1597, "ń": 735,
            ")": 318, "Z": 808, "Ś": 73, "U": 194, "F": 57, "?": 441,
            "H": 322, "Ó": 14, "Ł": 25, "x": 6, "v": 16, "-": 54, "Ź": 4,
            "V": 20, "/": 3, "Ć": 1, "q": 4, "1": 116, "8": 35, "2": 30,
            "7": 55, "4": 24, "6": 19, "–": 32, "9": 25, "0": 22, "3": 31, "5": 17,
            "X": 22,
        }
        self.letters = {letter: count ** (1/4) for letter, count in lettersCount.items()}
        self.cryptograms = []
        for line in data.splitlines():
            if len(self.cryptograms) < lines:
                self.cryptograms.append(Cryptogram(line))



    def match_key(self, pos):
        letter_chance = {}
        for cryptogram in self.cryptograms:
            # If we are seeking key on index that is out of range our cryptogram
            if (pos >= len(cryptogram)):
                continue
            for letter in self.letters.keys():
                possible_key = ord(cryptogram.getChar(pos)) ^ ord(letter)

                letter_chance[possible_key] = letter_chance.get(possible_key, 0) + self.letters[letter]

        
        return max(letter_chance.keys(), key=lambda k: letter_chance[k])

    def get_longest_cryptogram_length(self):
        return max(len(cryptogram) for cryptogram in self.cryptograms)

    def generate_key(self):
        key_length = self.get_longest_cryptogram_length()

        return [self.match_key(letter_index) for letter_index in range(key_length)]

    def decrypt(self, cryptogram, key):
        message = [chr(ord(cryptogram.getChar(index)) ^ key[index])
                        for index in range(len(cryptogram))]
        return "".join(message)


def main(testCount):
    with open('data', 'r') as data_file:
        decryptor = Decryptor(data_file.read(), testCount)

    key = decryptor.generate_key()

    for cryptogram in decryptor.cryptograms:
        print(decryptor.decrypt(cryptogram, key), "\n")


if __name__ == '__main__':
    testCount = 21
    if len(sys.argv) == 2:
        testCount = int(sys.argv[1])
    main(testCount)
