import copy

class Solution:
    def letterCombinations(self, digits:str) -> str:
        if digits == "":
            return list()
        
        char_array =    [ ['a','b','c'],
                        ['d','e','f'],
                        ['g','h','i'],
                        ['j','k','l'],
                        ['m','n','o'],
                        ['p','q','r','s'],
                        ['t','u','v'],
                        ['w','x','y','z']
                        ]
        
        letter_combination = list([""])

        for char in digits:
            index = int(char)
            # print(index)

            new_combination = list()
            for letter in char_array [index -2]:  # -1 -1
                # print("letter: {}".format(letter))
                for original_comb in letter_combination:
                    combination = original_comb + letter
                    new_combination.append(combination)
            letter_combination = copy.deepcopy(new_combination)
        return letter_combination
    
assert (Solution().letterCombinations("23")) == ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']   

                
