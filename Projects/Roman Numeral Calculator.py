"""TODO: create a RomanNumerals helper object"""
class RomanNumerals:
    def __init__(self, input):
        self.input = input
        
    def to_roman(input):
    #Convert an integer to a Roman numeral.
        
        ints = [1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1]
        nums = ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
        result = []
        
        
        for i in range(len(ints)):
            count = int(input / ints[i])
            result.append(nums[i] * count)
            input -= ints[i] * count
        return ''.join(result)
        

    def from_roman(input):
    #Convert a Roman numeral to an integer.

        input = input.upper(  )
        nums = {'M':1000, 'CM': 900, 'D':500, 'CD': 400, 'C':100, 'XC': 90, 'L':50, 'XL': 40, 'X':10, 'IX':9, 'V':5, 'IV': 4, 'I':1}
        sum = 0

        for i in range(len(input)):
        
            value = nums[input[i]]
            # If the next place holds a larger number, this value is negative
            if i+1 < len(input) and nums[input[i+1]] > value:
                sum -= value
            else: sum += value

            if RomanNumerals.to_roman(sum) == input:
                return sum
            
print(RomanNumerals.to_roman(1000))
