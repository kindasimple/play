# Python


I like the portability of python and vi to write simple, portable packages. I'm just playing around with the language, environment, and test framework. I'll also see what I can do with available packages for public web APIs and hopefully hardware.
* * *

## Resources

Python documentation can be found at [docs.python.org](http://docs.python.org/). The 
section on [PyUnit](http://docs.python.org/3/library/unittest.html) details unit testing
with the TestSuite.

I did [some research](http://quitecomplex.com/2014/03/10/dev-log-march-10/) to get up and running with Python. 
Getting the environment. [This introduction](http://mirnazim.org/writings/python-ecosystem-introduction/) was useful.

To install the PIP package manager for Python, run the script, [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py). 

## Packages

* github_demo: query for users repos
* maths: basic arithmatic with PyUnit tests

For a demo, run 

```
python demo.py
```


### github_demo

Script using PyGithub to query the API for Github. It requires the module Github from the package github2

```
python get-pip.py

pip install PyGithub
```

### Arithmetic

Wrapping basic arithmetic operations in classes. Its not useful except as an example of how to organize modules in packages and to set up a Test Suite.

```
>>> from maths import Arithmetic, Number
>>> 
>>> # Do some arithmetic
>>> print("2 + 3 = %d" % Arithmetic().Add(Number(2), Number(3)).value)
2 + 3 = 5
>>> print("8 - 3 = %d" % Arithmetic().Subtract(Number(8), Number(3)).value)
8 - 3 = 5
>>> print("4 * 5 = %d" % Arithmetic().Multiply(Number(4), Number(5)).value)
4 * 5 = 20
>>> print("16 / 4 = %d" % Arithmetic().Divide(Number(16), Number(4)).value)
16 / 4 = 4
```

####Testing

This package is mainly an excuse to run PyTest on a project. Execute the unit 
test runner with the following command:

```
python -m unittest tests/testArithmetic.py
-----------------------------------------------
Ran 4 tests in 0.003s

OK

```

The code for the test runner is given in tests/testArithmetic.py

```
import unittest
from maths import Number, Arithmetic

class BaseArithmeticTestCase(unittest.TestCase):
	def setUp(self):
		self.math = Arithmetic()

	def tearDown(self):
		self.math = None

class ArithmeticTestCase(BaseArithmeticTestCase):
	def testAdd(self):
		addend1 = Number(5)
		addend2 = Number(2)
		sum = Number(7)

		self.assertTrue(self.math.Equals(self.math.Add(addend1, addend2), sum), 'incorrect result')
```

The unit test can be run from the command line by adding the entry point to the test module

```
if __name__ == "__main__":
	unittest.main()
```

and invoking a test from the command line

```
 python -m unittest tests/testArithmetic.py
 python -m unittest discover tests/
```

The test runner is the class `ArithmeticTestCase`. Assuming there are many test runners to test different modules, its convenient to set up a test suite.

```
## test configuration
#######################

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ArithmeticTestCase)
    return suite
```

A configured test suite is then run by a test runner.

```
if __name__ == "__main__":
        runner = unittest.TextTestRunner()
        test_suite = suite()
        runner.run(test_suite)
```
