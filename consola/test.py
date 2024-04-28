import re
class Numero:
    normal = ""
    romano = ""

    def __init__(self, numero):
        self.normal = numero
        self.romano = self.convertir_a_romano(numero)
    
    def convertir_a_romano(self, numero):
            roman_map = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
            integers = list(roman_map)
            symbols = list(roman_map.values())
            i = 12
            result = ""

            while numero > 0:
                if integers[i] <= numero:
                    result += symbols[i]
                    numero -= integers[i]
                else:
                    i -= 1
            return result
    
    def imprime(self):
        print(f"Normal: {self.normal}, Romano: {self.romano}")
    
    def suma_romano(self, otro_romano):
        if not self.is_romano(otro_romano):
            raise ValueError(f"{otro_romano} no es un número romano válido.")
        otro_normal = self.convertir_a_normal(otro_romano)
        self.normal += otro_normal
        self.romano = self.convertir_a_romano(self.normal)

    def convertir_a_normal(self, romano):
        romano_a_valor = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        i = 0
        while i < len(romano):
            if i + 1 < len(romano) and romano_a_valor[romano[i]] < romano_a_valor[romano[i + 1]]:
                total -= romano_a_valor[romano[i]]
            else:
                total += romano_a_valor[romano[i]]
            i += 1
        return total
    
    def is_romano(self, romano):
        patron = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        if re.match(patron, romano):
            return True
        else:
            raise ValueError(f"{romano} no es un número romano válido.")
    

if __name__ == "__main__":
    mn= Numero(25)
    mn.imprime()
    print(mn.is_romano('XX454'))