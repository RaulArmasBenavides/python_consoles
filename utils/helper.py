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
    




if __name__ =="__main__":
  print(espar(123)) # [Finished in 437ms]
