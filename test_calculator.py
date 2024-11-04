import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) #actual output vs expected output

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    #subtract
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-1, -2), 1)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(1, 0), 1)

    #multiply
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-9, 4), -36)

    # divide
    def test_divide(self):
        self.assertEqual(self.calc.divide(42, 7), 6)

    def test_divide_two(self):
        self.assertEqual(self.calc.divide(10, 1), 10)
    
    # modulo
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(42, 7), 0)

    def test_modulo_two(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()