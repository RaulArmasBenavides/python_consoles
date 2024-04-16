# test_eval.py
import sys
import os
def run_code(string):
    """ Evaluate the passed string as code """
    try:
        #Pass __builtins__ dictionary as empty
        eval(string, {'__builtins__':{}})
    except Exception as e:
        print(repr(e))

if __name__ == "__main__":
    run_code(sys.argv[1])
    #Now the attacker is not able to