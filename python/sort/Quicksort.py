#!/usr/bin/python

"""This is a class that implements various sorting algorithms"""
from maths.Number import Number
from maths.Arithmetic import Arithmetic
import math

class Quicksort:
  """Class that performs sorting operations using the custom Number
  objects and arithmatic class"""
  def Sort(self, unsorted):
    """Perform a quicksort comparison sort:

    pseudocode from http://en.wikipedia.org/wiki/Quicksort
    function quicksort(a)
    if length(a) ≤ 1
       // an array of zero or one elements is already sorted
       return a
    select and remove a pivot element pivot from array
    // see Choice of pivot, below
    create empty lists less and greater
    for each x in a
       if x ≤ pivot then append x to less
       else append x to greater
    // two recursive calls
    return concatenate(quicksort(less), list(pivot), quicksort(greater))
    """
    if len(unsorted) <= 1:
      return unsorted
    midpoint = math.floor(len(unsorted) /2)
    pivot = unsorted[midpoint];
    print("sorting for {} with pivot {}".format(unsorted, pivot))
    unsorted.remove(pivot)
    less = []
    more = []
    for item in unsorted:
      if Arithmetic().LessThan(item, pivot):
        less.append(item)
      else:
        more.append(item)

    print("sorted for pivot {}: {}".format(pivot, less + [pivot] + more))
    return Quicksort.Sort(self, less) + [pivot] + Quicksort.Sort(self, more)
