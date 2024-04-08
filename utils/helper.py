##comprobar si un numero es impart

def espar(num):
    return num%2==0 
 

def is_leap_year(year):
    # Check if the year is evenly divisible by 4
    if year % 4 == 0:
        # If the year can also be evenly divided by 100, it must also be evenly divisible by 400 to be a leap year
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def roman_to_int(s):
    """
    Convierte numero romano a entero
    """
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
            result -= roman_values[s[i]]
        else:
            result += roman_values[s[i]]

    return result


def int_to_roman(x):
    """
    Convierte numero entero a romano
    """
    roman_map = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
    integers = list(roman_map)
    symbols = list(roman_map.values())
    i = 12
    result = ""

    while x != 0:
        if integers[i] <= x:
            result += symbols[i]
            x -= integers[i]
        else:
            i -= 1
    return result



if __name__ =="__main__":
  print(espar(123)) # [Finished in 437ms]
