def group_of_tens(numbers_string):
    nums = [int(x) for x in numbers_string.split(", ")]
    groups = 10

    while nums:
        current_group = [n for n in nums if n <= groups]
        nums = [n for n in nums if n > groups]

        print(f"Group of {groups}'s: {current_group}")
        groups += 10


numbers = input()
group_of_tens(numbers)
