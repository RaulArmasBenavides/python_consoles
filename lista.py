def doblar (lista):
  """ 
  Doblar 
  >>> l = [1, 2, 3, 4, 5]
  >>> doblar(l)
  [2, 4, 6, 8, 10]

  """
  return [n*2 for n in lista]

if __name__ =="__main__":
   import doctest 
   doctest.testmod()