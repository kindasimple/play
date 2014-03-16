#!/usr/bin/python

from maths import Arithmetic, Number

print("Do some arithmetic")
print("2 + 3 = %d" % Arithmetic().Add(Number(2), Number(3)).value)
print("8 - 3 = %d" % Arithmetic().Subtract(Number(8), Number(3)).value)
print("4 * 5 = %d" % Arithmetic().Multiply(Number(4), Number(5)).value)
print("16 / 4 = %d" % Arithmetic().Divide(Number(16), Number(4)).value)

print("Get some projects from Github")
from github_demo import github_list_repo
