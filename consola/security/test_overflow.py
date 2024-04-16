# len_overflow.py
class A(object):
    def __len__(self):
     return 100 ** 100
class B:
    def __len__(self):
     return 100 ** 100
    

if __name__ == "__main__":
    try:
        len(A())
        print("OK: 'class A(object)' with 'return 100 ** 100' - len calculated")
    except Exception as e:
        print("Not OK: 'class A(object)' with 'return 100 ** 100' - len raise Error: " + repr(e))
    try:
        len(B())
        print("OK: 'class B' with 'return 100 ** 100' - len calculated")
    except Exception as e:
        print("Not OK: 'class B' with 'return 100 ** 100' - len raise Error: " + repr(e))