#!/usr/bin/python3
"""
defines a function that finds the peak of a list of unsorted integers
"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    size = len(list_of_integers)
    
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    
    
    left = 0
    right = len(list_of_integers) - 1
    
    mid = int(left + right) // 2
    p = list_of_integers[mid]
    
    if p > list_of_integers[mid - 1] and p > list_of_integers[mid + 1]:
        return p
    elif p < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[left:mid + 1])
    elif p < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:right + 1])
    else:
        return list_of_integers[left]
