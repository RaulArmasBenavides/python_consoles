# test_eval.py
import sys
import os

def run_code(string):
    """ Evaluate the passed string as code """
    try:
        print(string)
        #eval(string, {})
    except Exception as e:
        print(repr(e))
        

if __name__ == "__main__":
        run_code(sys.argv[1])