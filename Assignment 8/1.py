class RomanNumeral:
    def __init__(self, num):
        self.num = num

    def to_roman(self):
        roman = ''
        for value, numeral in RomanNumeral.roman_numeral_map:
            while self.num >= value:
                roman += numeral
                self.num -= value
        return roman

    def to_int(self):
        integer = 0
        for value, numeral in RomanNumeral.roman_numeral_map:
            while self.numeral.startswith(numeral):
                integer += value
                self.numeral = self.numeral[len(numeral):]
        return integer

    roman_numeral_map = (
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    )