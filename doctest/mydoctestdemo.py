def doblar (lista):
  """ 
  Doblar 
  >>> l = [1, 2, 3, 4, 5]
  >>> doblar(l)
  [2, 4, 6, 8, 10]

  """
  return [n*2 for n in lista]


def invertir_cadena(texto):
    """
    Invierte una cadena de texto.

    >>> invertir_cadena('Hola Mundo')
    'odnuM aloH'
    >>> invertir_cadena('')
    ''
    """
    return texto[::-1]

def es_primo(num):
    """
    Verifica si un número es primo.

    >>> es_primo(11)
    True
    >>> es_primo(4)
    False
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def mcd(a, b):
    """
    Calcula el máximo común divisor de a y b.

    >>> mcd(60, 48)
    12
    >>> mcd(7, 5)
    1
    """
    while b:
        a, b = b, a % b
    return a

if __name__ =="__main__":
   import doctest 
   doctest.testmod()