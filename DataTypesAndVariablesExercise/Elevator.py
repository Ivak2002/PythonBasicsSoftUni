from math import ceil
people = int(input())
one_elevator_lift_limit = int(input())
needed_courses = ceil(people/one_elevator_lift_limit)
print(needed_courses)