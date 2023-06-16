#!/usr/bin/python3
"""
   Calculates the total amount of rainwater retained after it rains
"""
def rain(walls):
    if len(walls) == 0:
        return 0

    total_water = 0
    left_max = 0
    right_max = 0
    left_pointer = 0
    right_pointer = len(walls) - 1

    while left_pointer < right_pointer:
        if walls[left_pointer] < walls[right_pointer]:
            if walls[left_pointer] > left_max:
                left_max = walls[left_pointer]
            else:
                total_water += left_max - walls[left_pointer]
            left_pointer += 1
        else:
            if walls[right_pointer] > right_max:
                right_max = walls[right_pointer]
            else:
                total_water += right_max - walls[right_pointer]
            right_pointer -= 1

    return total_water
