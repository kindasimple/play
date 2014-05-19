#!/usr/bin/python

"""This is a class that implements various sorting algorithms"""
from maths.Number import Number
from maths.Arithmetic import Arithmetic
import math

class Sorting:
  """Class that performs sorting operations using the custom Number
  objects and arithmatic class"""

  def InsertionSort(self, items) :
    """pseudocode from: http://en.wikipedia.org/wiki/Insertion_sort
    for i ← 1 to length(A)
    x ← A[i]
    j ← i
    while j > 0 and A[j-1] > x
        A[j] ← A[j-1]
        j ← j - 1
    A[j] ← x"""
    for i, x in enumerate(items) :
      j = i
      while j > 0 and Arithmetic().GreaterThan(items[j-1], x) :
        items[j] = items[j-1]
        j -= 1
      items[j] = x
    return items

  def Mergesort(self, unsorted):
    """Perform a mergesort comparison sort:
    pseudocode from http://en.wikipedia.org/wiki/Merge_sort

    // Base case. A list of zero or one elements is sorted, by definition.
    if length(m) <= 1
        return m

    // Recursive case. First, *divide* the list into equal-sized sublists.
    var list left, right
    var integer middle = length(m) / 2
    for each x in m before middle
         add x to left
    for each x in m after or equal middle
         add x to right

    // Recursively sort both sublists.
    left = merge_sort(left)
    right = merge_sort(right)
    // *Conquer*: merge the now-sorted sublists.
    return merge(left, right)"""
    ## Base case is sorted one-item list
    if len(unsorted) <= 1:
      return unsorted

    ## Recursive case where we split the list
    middle = math.floor(len(unsorted) / 2)
    left = []
    right = []
    for idx, item in enumerate(unsorted):
      if idx < middle:
        left.append(item)
      else:
        right.append(item)

    # Sort each sublist
    left = self.Mergesort(left)
    right = self.Mergesort(right)

    # Merge the sublists
    sorted = []
    idxLeft = 0
    idxRight = 0
    while idxLeft < len(left) and idxRight < len(right):
      if(Arithmetic().LessThan(left[idxLeft], right[idxRight])):
        sorted.append(left[idxLeft])
        idxLeft += 1
      else:
        sorted.append(right[idxRight])
        idxRight += 1

    # Merge remaining elements
    while idxLeft < len(left):
      sorted.append(left[idxLeft])
      idxLeft += 1
    while idxRight < len(right):
      sorted.append(right[idxRight])
      idxRight += 1
    return sorted


  def HeapsortSiftDown(self, items):
    """http://en.wikipedia.org/wiki/Heapsort

    function heapsort(a, count) is
    input: an unordered array a of length count

    (Build the heap in array a so that largest value is at the root)
    heapify(a, count)

    (The following loop maintains the invariants that a[0:end] is a heap and every element
     beyond end is greater than everything before it (so a[end:count] is in sorted order))
    end ← count - 1
    while end > 0 do
        (a[0] is the root and largest value. The swap moves it in front of the sorted elements.)
        swap(a[end], a[0])
        (the heap size is reduced by one)
        end ← end - 1
        (the swap ruined the heap property, so restore it)
        siftDown(a, 0, end)

    function heapify(a,count) is
    (end is assigned the index of the first (left) child of the root)
    end := 1

    while end < count
       (sift up the node at index end to the proper place such that all nodes above
        the end index are in heap order)
       siftUp(a, 0, end)
       end := end + 1
    (after sifting up the last node all nodes are in heap order)
    """
    end = len(items) - 1
    self.maxheapifySiftDown(items, len(items))
    #print("Heapified with downsift: ", items)
    while end > 0 :
      items[end], items[0] = items[0], items[end]
      end -= 1
      self.SiftDown(items, 0, end)
      #print("Resifted: ", items)

    #print("Heapsort DownSorted: ", items)
    return items

  def HeapsortSiftUp(self, items):
    end = len(items) - 1
    self.maxheapifySiftUp(items, len(items))
    #print("Heapified with Upsift: ", items)
    while end > 0:
      items[end], items[0] = items[0], items[end]

      self.maxheapifySiftUp(items, end)
      #print("Resifted: ", end, items)
      end -= 1

    #print("Heapsort UpSorted: ", items)
    return items

  def maxheapifySiftUp(self, items, count) :
    end = 1

    while end < count:
      self.SiftUp(items, 0, end)
      end += 1

  def maxheapifySiftDown(self, items, count) :
    start = math.floor((count-2)/2)

    while start >= 0 :
      self.SiftDown(items, start, count-1)
      start -= 1

  def SiftUp(self, items, start, end) :
    """Pseudocode:
    function siftUp(a, start, end) is
    input:  start represents the limit of how far up the heap to sift.
                 end is the node to sift up.
    child := end
    while child > start
       parent := floor((child - 1) / 2)
       if a[parent] < a[child] then (out of max-heap order)
           swap(a[parent], a[child])
           child := parent (repeat to continue sifting up the parent now)
       else
           return"""
    #print("Sifting ", items)
    child = end
    while child > start:
      parent = math.floor((child - 1)/2)
      #print("if on ", items[parent], items[child])
      if Arithmetic().LessThan(items[parent], items[child]):
        items[parent], items[child] = items[child], items[parent]
        child = parent
      else:
        return

  def SiftDown(self, items, start, end) :
    """Pseudocode:
    siftDown(start, end) :
    root = start
    lastLeaf = end

    while root*2 +1 <= lastLeaf :
        child = root*2 +1
        if (child+1 <= lastLeaf) and (a[child+1] > a[child]) :
            child = child+1
        if a[root] < a[child] :
            swap(a[root], a[child])
            root = child
        else :
            return
    """
    root = start
    child = start*2+1
    while child <= end :
      if (child+1 <= end) and (Arithmetic().GreaterThan(items[child+1], items[child]) ):
        child += 1
      if Arithmetic().LessThan(items[root], items[child]) :
        items[root], items[child] = items[child], items[root]
        root = child
      else :
        return
      child = root*2+1


  def Quicksort(self, unsorted):
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
    #print("sorting for {} with pivot {}".format(unsorted, pivot))
    unsorted.remove(pivot)
    less = []
    more = []
    for item in unsorted:
      if Arithmetic().LessThan(item, pivot):
        less.append(item)
      else:
        more.append(item)

    #print("sorted for pivot {}: {}".format(pivot, less + [pivot] + more))
    return Sorting.Quicksort(self, less) + [pivot] + Sorting.Quicksort(self, more)
