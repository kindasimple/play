#!/usr/bin/python

"""This is a class that performs elementary arithmetic"""
from maths.Number import Number

class Arithmetic:
	"""Class that performs arithmetic operations by wrapping python
operations in methods"""
	def Add(self, addend1: Number, addend2: Number):
		return Number(addend1.value + addend2.value)

	def Subtract(self, minuend: Number, subtrahend: Number):
		return Number(minuend.value - subtrahend.value)

	def Equals(self, left: Number, right: Number):
		return left.value == right.value 
