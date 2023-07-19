class Solution:
    def intToRoman(self, num:int) -> str:
        mapping_table = {
                            1000 : "M",
                            900  : "CM",
                            500  : "D",
                            400  : "CD",
                            100  : "C",
                            90   : "XC",
                            50   : "L",
                            40   : "XL",
                            10   : "X",
                            9    : "IX",
                            5    : "V",
                            4    : "IV",
                            1    : "I"
        }

        roman_string = '' 

        for base, roman_symbols in mapping_table.items():
            roman_string += (num // base) * roman_symbols
            num = num % base

        return roman_string

assert  Solution().intToRoman(3) == 'III'
assert  Solution().intToRoman(1994) == 'MCMXCIV'       
