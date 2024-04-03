# Calculate how many years ago the fatehr was twice as old as his son  ( or in how many years he will be twice as old)
def twice_as_old(dad_year_old,son_years_old):
  return abs(dad_year_old - (2*son_years_old))
    

#function which tells us if a given character is a letter or not.
def is_it_letter(s):
    return s.isalpha()

if __name__ =="__main__":
 print(twice_as_old(50,26))
      
    
