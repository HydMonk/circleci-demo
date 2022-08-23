# Import the Add function, and assert that it works correctly.
from main import doCalculate

def TestAdd():
        assert doCalculate(2,3) == 5
        print("Calculate functions works")

if __name__ == '__main__':
        TestAdd()
