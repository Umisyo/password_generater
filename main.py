import random

class PassWord:
    def __init__(self, pass_length: int):
        self.pass_length = pass_length
        self.pass_word = self.generater()

    def generater(self):
        symbols = '!"#$%&-^¥@;:/<>+*{}[]|~='
        upper_strings = [chr(i) for i in range(65, 65+26)]
        lower_strings = [chr(i) for i in range(97, 97+26)]
        numbers = [chr(i) for i in range(48, 48+10)]

        upper_length = 0
        lower_length = 0
        symbols_length = 0
        nubmer_length = 0

        while (upper_length + lower_length + symbols_length + nubmer_length != self.pass_length):
            upper_length = random.choice(range(1, self.pass_length))
            lower_length = random.choice(range(1, self.pass_length))
            symbols_length = random.choice(range(1, self.pass_length))
            numbers_length = random.choice(range(1, self.pass_length))

        upper_pass_array = random.choices(upper_strings, k=upper_length)
        lower_pass_array = random.choices(lower_strings, k=lower_length)
        symbol_pass_array = random.choices(symbols, k=symbols_length)
        number_pass_array = random.choices(numbers, k=numbers_length)

        pass_array = random.sample(upper_pass_array + lower_pass_array + symbol_pass_array + number_pass_array, k=self.pass_length)

        pass_word = ''.join(pass_array)

        return pass_word


if __name__ == '__main__':
    pw = PassWord(8)
    print(pw.pass_word)

