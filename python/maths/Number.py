#!/usr/bin/python

class Number:
	"""Object for numeral representation"""
	def __init__(self, value: int):
		self.value = value
	def __str__(self):
		return str(self.value)
	def __repr__(self):
		return str(self.value)
