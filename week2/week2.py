from typing import List, Any, Dict, Set
import copy
import json as j
import random as r


# 1. Write a function to check if a number is even.
def check_even(n: int) -> str:
    # check for the int
    if not isinstance(n, int):
        return "\nInvalid Input! Enter an integer please."

    # even check
    if n % 2 == 0:
        return f"\nIndeed, {abs(n)} is an Even number."

    else:
        return f"\nSorry, {abs(n)} is not an even number."


# print(check_even(-10))


# 2. Create a list and find the sum of all its elements.
def list_sum() -> str:
    nums: List[int] = []  # empty for now

    # creating a valid integers list
    while True:
        try:
            inp: int = int(input("Enter your numbers(0 to exit):"))
            if inp == 0:
                break
            nums.append(inp)

        except:
            print("Invalid Input! Enter an integer please.\n")

    # for summation
    res: int = 0
    for n in nums:
        res += n

    # final result
    return f"\nYour List: {nums} \n\t The sum = {res}"


# print(list_sum())


# 3. Write a program to find the maximum and minimum in a list.
def max_min(list: List[int]) -> str:
    # if list consists of same numbers
    if all(n == list[0] for n in list):
        return f"{list} \nAll the elements are equal!"

    # for max value
    base_1: int = list[0]  # first number
    for n in list:
        if base_1 < n:
            # only if the base value is smaller than n otherwise pass
            base_1 = n

    # for min value
    base_2: int = list[0]
    for n in list:
        if base_2 > n:
            # only if the base value is greater than n otherwise pass
            base_2 = n

    return f"{list} \nThe max value = {base_1}, The min value = {base_2}."


# print(max_min([24, 23, 99, 42, 1001, 1111, 22202, 0]))


# 4. Create a program that removes duplicates from a list.
def rem_dup(itm: List[str | int]) -> str:
    old_list: List[str | int] = copy.deepcopy(itm)  # to preserved the original
    seen: List[str | int] = []  # saves the first occurence

    for i in old_list:
        if i not in seen:
            seen.append(i)

        else:
            itm.remove(i)

    return f"Old List : {old_list},\n New List : {itm}"


# print(rem_dup([1, 2, 1, 2,3,4, 3,4]))


# 5. Write a function to reverse a list.
def rev_list(lst: List[Any]) -> str:
    new_list: List[Any] = []

    for i in lst:
        new_list.insert(0, i)

    return f"old list: {lst}, \n new list : {new_list}"


# print(rev_list(['hamza', 'ali', 4, 'saim', 434]))


# 6. Create a tuple and access its elements.
def tup(inp: List[str | int]) -> None:
    a: tuple = tuple(inp)
    print(a[1:3])  # at index 1 and 2 (3 exclusive)
    print(a[2:-1])  # at index 2 to 2nd last


# tup(['hamza', 88, 'saim', 55, 'anique', 44, 'shayan', 66])


# 7. Convert a list into a tuple and vice versa.
def lst_tup(inp: List | tuple) -> str:
    if type(inp) is list:
        res1: tuple = tuple(inp)
        return f"Given List: {inp}, Tuple: {res1}"
        # manually list -> tuple
        """
            res = ()
            for n in inp:
                res += (n,)  -> we are creating a new tuple each and every time (not mutating).
        """

    else:
        res2: List = list(inp)
        return f"Given Tuple: {inp}, List: {res2}"
        # manually tuple -> list
        """
            res = []
            for n in inp:
                res.append(n)
        """


# print(lst_tup([1, 2, 3]))
# print(lst_tup((1, 2, 3)))


# 8. Write a program to merge two or more dictionaries.
def merge_dict(**kargs: Dict) -> str:
    # merging
    new_dict: Dict = {}
    seen: Dict = {}

    # going into first wrapper
    for d in kargs.values():
        # getting the inside dicts
        for key, value in d.items():

            count: int | None = seen.get(key)
            # we make its first count explicitly
            if count is None:
                seen[key] = count = 1

            # if key is duplicate change its name
            if key in new_dict.keys():
                if type(count) == int:
                    count += 1  # increase it's duplicate count
                    new_dict[key + str(count)] = value

            else:
                # creating a key and assigning a value (normal)
                new_dict.setdefault(key, value)

            # successfully updates the duplicate count in seen
            if type(count) == int:
                seen[key] = count

    # printing old dicts
    print("\nOld Dictionaries:")
    for _, value in kargs.items():
        print(value)

    return f"\nNew Dictionary: {j.dumps(new_dict, indent=4, sort_keys=True)}, \n {seen}"


# print(
#     merge_dict(
#         first={
#             "Name": "Muhammad Hamza Zai",
#             "Age": 17,
#             "Father Name": "Muhammad Ifraq Zai",
#             "Gender": "Male",
#             "area": "liaquatabad"
#         },
#         second={
#             "Name": "Muhammad Ifraq Zai",
#             "Age": 55,
#             "Father Name": "Farooq Ali Khan",
#             "Gender": "Male",
#             'area': 'North'
#         },
#         third={"Name": "Farooq Ali Khan", "Age": 88, "Gender": "Male"},
#     )
# )

# for *args
# merge_dict(
#     {"Name": "Hamza", "Age": 17, "Father Name": "Ifraq"},
#     {"Name": "Ifraq", "Age": 55, "Father Name": "Farooq"},
# )


# 9. Write a function to count the frequency of elements in a list.
def ele_fre(lis: List) -> None:
    # saves the count in it
    res: Dict = {}

    # looping the list
    for i in lis:
        # check for existence
        count: None | int = res.get(str(i))

        # if not exists
        if count is None:
            # the first entry
            count = 1
            # res[str(i)] = f"{i} appears {count} time."
            res[str(i)] = count

        else:
            # already exists increase by 1
            count += 1
            res[str(i)] = count

    # result
    print(f"Given List: {lis} \n Elements Frequencies:")
    for key, value in res.items():
        word: str = "time" if value == 1 else "times"
        print(f"\t{key}: appears {value} {word}.")


# (ele_fre([1, 2, 3, 3, 2, 3, 2, 8, 4, 5, 6, 4, 3, 7, 8, 9, 0]))
# (ele_fre([0,0,0,0]))


# 10. Create a dictionary of squares of numbers from 1 to n.
def num_sqr(n: int = 10) -> str:
    # using dictionary comprehension
    res: Dict = {x: x**2 for x in range(1, n + 1)}
    return f"Dictionary of squares from 1 to {n}: \n\t{j.dumps(res, indent=4)}"


# print(num_sqr(60))


# 11. Write a program to sort a list in ascending order.
def sort_lis(lis: List[int]) -> str:
    old_list: List[int] = copy.deepcopy(lis)
    swapped: bool = True  # the indicator

    # sorting
    # outer loop for multiple checks or passes
    while swapped:
        swapped = False  # the indicator

        # which actually do checks
        for i in range(len(lis) - 1):

            if lis[i] > lis[i + 1]:
                # swapping
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
                swapped = True

        # no swapped means everything is sorted
        if not swapped:
            break

    return f"Old List: {old_list} \n New List: {lis}"


# print(sort_lis([29, 28, 30, 18]))

#  not efficient and can't solve complex cases
# def sort_lis(lis: List[int]) -> str:
#     old_list: List[int] = copy.deepcopy(lis)

#     # for comparing
#     base_val: int = lis[0]

#     # sorting
#     for n in lis[1:]:
#         # normal case
#         if base_val > n:
#             lis.pop(lis.index(n))
#             lis.insert(lis.index(base_val), n)

#         # for rare case
#         elif n < lis[lis.index(n) - 1]:
#             ind: int = lis.index(n)  # safing it's index
#             lis.pop(ind)
#             lis.insert(ind - (1 if ind > 1 else 0), n)

#         base_val = n  # updating it with next element

#     return f"Old List: {old_list} \n New List: {lis}"

# print(sort_lis([28, 29, 30, 18]))


# 12. Create a program to check if a key exists in a dictionary.
def key_check(d: Dict, k: str) -> str:
    # count: int = 0  # if multiple keys exists(same)

    # immediate check
    if not k in d:
        return f"The dictionary: {j.dumps(d, indent=4)}\n has no key named '{k}'."

    # checking
    for key, _ in d.items():
        if key == k:
            break
            # count += 1 # dictionary duplicates are overwritten implicitly.

    # word: str = 'keys' if count > 1 else 'key'

    return f"The dictionary: {j.dumps(d, indent=4)}\n has a key named '{k}'."


# print(
#     key_check(
#         {"Name": "Muhammad Hamza Zai", "Age": None, "Nationality": "Pakistani", "Age":23}, "Age"
#     )
# )
# 13. Create a set and perform union, intersection, and difference.
def set_opr(s1: Set, s2: Set) -> None:
    # union
    print(f"Orginal sets: {s1}, {s2}. \n\t Union : {s1.union(s2)}.")
    # Intersection
    print(f"\nOrginal sets: {s1}, {s2}. \n\t Intersection : {s1.intersection(s2)}.")
    # Difference
    print(f"\nOrginal sets: {s1}, {s2}. \n\t Difference : {s1.difference(s2)}.")


# set_opr({r.randint(1, 10) for _ in range(5)}, {r.randint(1,10) for _ in range(5)})


# 14. Write a function to find common elements in two lists.
def find_common(lis1: List[Any], lis2: List[Any]) -> str:
    common: List[Any] = []
    # storing the first list elements in seen
    seen: Dict = {x: 0 for x in lis1} # this handles duplicates itself

    # comparing with lis2 (efficient way then nested loop)
    for n in lis2:
        if n in seen:
            common.append(n)

    return f"{seen}, \n{common}"

# True, False = 1, 0
# print(find_common([1, 2, 3, "hamza", True, 2,4, False], [1, 3,2, 4, "hamza", True,4, 0]))

# 15. Write a function that returns the factorial of a number.
def factorial(n: int)-> int:
    base: int = 1
    for i in range(2,n+1):
        base *= i

    return base

# return the base
print(factorial(0))

# 16. Create a function that checks whether a string is a palindrome.
# 17. Write a function to count vowels in a string.
# 18. Create a dictionary and iterate over its keys and values.
# 19. Write a function to remove all punctuation from a string.
# 20. Write a function to capitalize the first letter of each word in a string.
# 21. Create a list comprehension to get squares of all even numbers in a range.
# 22. Write a function to check if a string is an anagram.
# 23. Create a nested dictionary to represent student records.
# 24. Write a function to flatten a nested list.
# 25. Write a program to find the second highest number in a list.
# 26. Create a function to rotate a list left by k positions.
# 27. Write a function to find the missing number from a list of 1 to N.
# 28. Write a program to remove all None values from a list.
# 29. Write a function to merge two dictionaries and handle key collisions by summing values.
# 30. Create a function to find unique elements present in only one of two lists.
