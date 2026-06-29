# from typing import list, Any, dict, set # old used in < 3.9
from typing import Any, TypedDict, get_type_hints, cast
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
    nums: list[int] = []  # empty for now

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
    return f"\nYour list: {nums} \n\t The sum = {res}"


# print(list_sum())


# 3. Write a program to find the maximum and minimum in a list.
def max_min(list: list[int]) -> str:
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
def rem_dup(itm: list[str | int]) -> str:
    old_list: list[str | int] = copy.deepcopy(itm)  # to preserved the original
    seen: list[str | int] = []  # saves the first occurence

    for i in old_list:
        if i not in seen:
            seen.append(i)

        else:
            itm.remove(i)

    return f"Old list : {old_list},\n New list : {itm}"


# print(rem_dup([1, 2, 1, 2,3,4, 3,4]))


# 5. Write a function to reverse a list.
def rev_list(lst: list[Any]) -> str:
    new_list: list[Any] = []

    for i in lst:
        new_list.insert(0, i)

    return f"old list: {lst}, \n new list : {new_list}"


# print(rev_list(['hamza', 'ali', 4, 'saim', 434]))


# 6. Create a tuple and access its elements.
def tup(inp: list[str | int]) -> None:
    a: tuple = tuple(inp)
    print(a[1:3])  # at index 1 and 2 (3 exclusive)
    print(a[2:-1])  # at index 2 to 2nd last


# tup(['hamza', 88, 'saim', 55, 'anique', 44, 'shayan', 66])


# 7. Convert a list into a tuple and vice versa.
def lst_tup(inp: list | tuple) -> str:
    if type(inp) is list:
        res1: tuple = tuple(inp)
        return f"Given list: {inp}, Tuple: {res1}"
        # manually list -> tuple
        """
            res = ()
            for n in inp:
                res += (n,)  -> we are creating a new tuple each and every time (not mutating).
        """

    else:
        res2: list = list(inp)
        return f"Given Tuple: {inp}, list: {res2}"
        # manually tuple -> list
        """
            res = []
            for n in inp:
                res.append(n)
        """


# print(lst_tup([1, 2, 3]))
# print(lst_tup((1, 2, 3)))


# 8. Write a program to merge two or more dictionaries.
def merge_dict(**kargs: dict) -> str:
    # merging
    new_dict: dict = {}
    seen: dict = {}

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
    print("\nOld dictionaries:")
    for _, value in kargs.items():
        print(value)

    return f"\nNew dictionary: {j.dumps(new_dict, indent=4, sort_keys=True)}, \n {seen}"


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
def ele_fre(lis: list) -> None:
    # saves the count in it
    res: dict = {}

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
    print(f"Given list: {lis} \n Elements Frequencies:")
    for key, value in res.items():
        word: str = "time" if value == 1 else "times"
        print(f"\t{key}: appears {value} {word}.")


# (ele_fre([1, 2, 3, 3, 2, 3, 2, 8, 4, 5, 6, 4, 3, 7, 8, 9, 0]))
# (ele_fre([0,0,0,0]))


# 10. Create a dictionary of squares of numbers from 1 to n.
def num_sqr(n: int = 10) -> str:
    # using dictionary comprehension
    res: dict = {x: x**2 for x in range(1, n + 1)}
    return f"dictionary of squares from 1 to {n}: \n\t{j.dumps(res, indent=4)}"


# print(num_sqr(60))


# 11. Write a program to sort a list in ascending order.
def sort_lis(lis: list[int]) -> str:
    old_list: list[int] = copy.deepcopy(lis)
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

    return f"Old list: {old_list} \n New list: {lis}"


# print(sort_lis([29, 28, 30, 18]))

#  not efficient and can't solve complex cases
# def sort_lis(lis: list[int]) -> str:
#     old_list: list[int] = copy.deepcopy(lis)

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

#     return f"Old list: {old_list} \n New list: {lis}"

# print(sort_lis([28, 29, 30, 18]))


# 12. Create a program to check if a key exists in a dictionary.
def key_check(d: dict, k: str) -> str:
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
def set_opr(s1: set, s2: set) -> None:
    # union
    print(f"Orginal sets: {s1}, {s2}. \n\t Union : {s1.union(s2)}.")
    # Intersection
    print(f"\nOrginal sets: {s1}, {s2}. \n\t Intersection : {s1.intersection(s2)}.")
    # Difference
    print(f"\nOrginal sets: {s1}, {s2}. \n\t Difference : {s1.difference(s2)}.")


# set_opr({r.randint(1, 10) for _ in range(5)}, {r.randint(1,10) for _ in range(5)})


# 14. Write a function to find common elements in two lists.
def find_common(lis1: list[Any], lis2: list[Any]) -> str:
    common: list[Any] = []
    # storing the first list elements in seen
    seen: dict = {x: 0 for x in lis1}  # this handles duplicates itself

    # comparing with lis2 (efficient way then nested loop)
    for n in lis2:
        if n in seen:
            common.append(n)

    return f"{seen}, \n{common}"


# True, False = 1, 0
# print(find_common([1, 2, 3, "hamza", True, 2,4, False], [1, 3,2, 4, "hamza", True,4, 0]))


# 15. Write a function that returns the factorial of a number.
def factorial(n: int) -> int:
    base: int = 1
    for i in range(2, n + 1):
        base *= i

    return base


# return the base
# print(factorial(0))


# 16. Create a function that checks whether a string is a palindrome.
def check_pall(s: str) -> str:
    # reversing the string
    new_str: str = ""

    # for i in range(len(s)-1, -1, - 1):
    #     print(s[i])

    # another one
    for ch in s[-1::-1]:
        new_str += ch

    if new_str.lower() == s.lower():
        return f"\nThe string '{s}' is a Palindrome."

    return f"\nThe string '{s}' is not a Palindrome."


# print(check_pall("Naman"))


# 17. Write a function to count vowels in a string.
def count_vowels(s: str) -> str:
    vow_counts: dict = {vow: 0 for vow in ["a", "e", "i", "o", "u"]}

    for ch in s:
        # if vowel
        if ch.lower() in vow_counts:
            # incrementing
            vow_counts[ch.lower()] += 1

    return f"Vowels count in '{s}':\n{j.dumps(vow_counts, indent=4)}"


# print(count_vowels("Arham"))


# 18. Create a dictionary and iterate over its keys and values.
def dic_opr() -> None:
    # creating a dictionary
    alpha: str = "abcdefghijklmnopqrstuvwxyz"
    d: dict = {n.capitalize(): r.randint(1, 100) for n in r.sample(alpha, 10)}

    for key, value in d.items():
        print(f"{key}: {value}.")


# dic_opr()


# 19. Write a function to remove all punctuation from a string.
def rem_punc(s: str) -> str:
    old: str = s
    new: str = ""
    punc: str = "!_-,.:;'"

    # immediate check
    if not any(n in s for n in punc):
        return f"\n No punctuations in {s}."

    # line by line checking
    for ch in s:
        # if exists then replace
        if ch not in punc:
            new += ch

    return f"Old: {old}, \nNew: {new}"


# print(rem_punc("hamza!!!"))


# 20. Write a function to capitalize the first letter of each word in a string.
def cap_word(s: str) -> str:
    old: str = s.strip()
    new: str = ""

    # first letter of first word
    new += old[0].capitalize()

    # capitalizing
    for i in range(1, len(old)):
        if old[i] == " " and i != len(old) - 1:
            new += " " + old[i + 1].capitalize()
        else:
            if old[i - 1] != " ":
                new += old[i]

    return f"Old: {old}, \nNew: {new.strip()}"


# print(
#     cap_word(
#         "                     my name is hamza and I'am a computer science student.           "
#     )
# )


# 21. Create a list comprehension to get squares of all even numbers in a range.
def lst_sqr(r: int = 10) -> str:
    res = [n**2 for n in range(r + 1) if n % 2 == 0]

    return f"Squares of all even numbers till {r}: \n {res}"


# print(lst_sqr(12))

# 22. Write a function to check if a string is an anagram.
"""
--- Anagram ---
    -> An anagram is a phrase or word created by rearranging 
    all the letters of another word, by using all the 
    letters exactly once.

    _ Examples _
    = Listen --  Silent.
    = Race   --  Care.

 (so, we have to take 2 strings and then compare them)

"""


def check_ana(s1: str, s2: str) -> str:
    if len(s1) != len(s2):
        return f"'{s1}' can't be anagram of '{s2}'."

    d1: dict = {}
    d2: dict = {}

    # saving the letters count of s1
    for ch in s1:
        # d1.setdefault(ch.lower(), 0)
        # d1[ch.lower()] += 1
        d1[ch.lower()] = d1.get(ch.lower(), 0) + 1

    # saving the letters count of s2
    for ch in s2:
        # d2.setdefault(ch.lower(), 0)
        # d2[ch.lower()] += 1
        d2[ch.lower()] = d2.get(ch.lower(), 0) + 1

    # only if counts are same
    if d1 == d2:
        return f"'{s1}' is an anagram of '{s2}'."

    return f"'{s1}' is not an anagram of '{s2}'."


# print(check_ana("silent", "listen"))

# 23. Create a nested dictionary to represent student records.
# creating base student record type


class Address(TypedDict):
    House_no: str
    Town: str
    famous_place: str


class Grades(TypedDict):
    Math: int
    Physics: int
    chemistry: int


class Feedback(TypedDict):
    Teachers: str
    Students: str
    Staff: str


class FocusOn(TypedDict):
    Discipline: str
    Anger: str
    Behavior: str
    skill_development: str
    religious_matters: str


class Student(TypedDict):
    Name: str
    father_name: str
    Age: int
    Address: Address
    Grades: Grades
    Feedback: Feedback
    focus_on: FocusOn


# type means it's a class not it's instance. It can accept any class
def build_from_hints(typ_hint: type) -> Student:
    hints: dict = get_type_hints(typ_hint)  # return fields and their type of objects
    # to fulfill mypy requirements
    # result: dict[str, Any] = {}  # actual dict where everything will save
    result: dict[str, Any] = {}  # actual dict where everything will save

    for field, typ in hints.items():
        # if the type is nested
        if hasattr(typ, "__annotations__"):
            print(f"\n--- Fill in '{field}' ---:")
            result[field] = build_from_hints(typ)  # recurse into it
        else:
            while True:
                # take the input if it is normal (str, int, bool,...)
                raw: str = (
                    input(f"\nEnter Your '{field}' must be ({typ.__name__}): ")
                    .strip()
                    .lower()
                )

                if not raw or (typ == str and raw.isdigit()):
                    print("Invalid Input\n")
                    continue

                try:
                    result[field] = typ(raw).title() if typ == str else typ(raw)
                    break
                except Exception:
                    print("Incorrect Input!\n")
                    continue

    return cast(Student, result)


def stud_rec(d: Student | None) -> None:
    if d is None:
        return

    print(f"\nRecord of '{d['Name'].title()}':")
    print(j.dumps(d, indent=4))


# stud_rec(build_from_hints(Student))  # mypy can't verify it


# 24. Write a function to flatten a nested list.
def flat_list(lis: list) -> list:
    result: list = []

    for ele in lis:
        # if type(ele) == list:
        if isinstance(ele, list):  # more pythonic
            # print(type(ele), ele)
            result += flat_list(ele)

        else:
            # print(type(ele), ele)
            result.append(ele)

    return result


def disply(ls: list) -> str:
    res: list = flat_list(ls)

    return f"Old List: {ls}\n New List: {res}"


# print(disply([1, 2, [3, 4], [5, [6, 7]]]))


# 25. Write a program to find the second highest number in a list.
def sec_high(lis: list[int]) -> str:

    if len(lis) < 2:
        return f"Atleast 2 elements are required!"

    base: int = lis[0]
    sec: int = lis[1]

    if all(n == base for n in lis):
        return f"All elements are same!"

    for n in lis[1:]:
        if base < n:
            sec, base = base, n

        elif sec < n:
            sec = n

    return f"Given List: {lis}\n Second Highest: {sec}."


# print(sec_high([5, 1]))
# 26. Create a function to rotate a list left by k positions.
def rot_list(lis: list, k: int) -> str:
    # edge cases
    if len(lis) <= 1:
        return f"List must have 2 or more elements(numbers)!"
    elif k == 0:
        return f"k = {k}, means no rotation needed."

    res: list = []
    k = k % len(lis)  # to ensure proper value K must not > len(lis)

    # getting first k elements
    first_ele: list = lis[:k]  # [start : stop] stop excluded
    last_ele: list = lis[k:]  # naturally runs upto the end element (includes k)

    res = last_ele + first_ele

    return f"Old {lis} \nNew {res}"


# print(rot_list([10, 20, 30, 40, 50], 3))


# 27. Write a function to find the missing number from a list of 1 to N.
def miss_num_det(lis: list[int]) -> str:
    N: int = len(lis) + 1  # as there always 1 number is missing
    expected_sum: int = N * (N + 1) // 2  # formula to calculate the correct sum
    actual_sum: int = 0

    # manually calculating actual sum
    for n in lis:
        actual_sum += n

    # for missing number
    res: int = expected_sum - actual_sum

    return f"Given List: {lis} \n Missing Number: {res}"


# print(miss_num_det([1, 2, 3, 4, 6]))


# 28. Write a program to remove all None values from a list.
def rem_Non(lis: list) -> str:
    # safety checks first to immediate exit
    if len(lis) == 0:
        return f"\nNo List found!"

    if None not in lis:
        return f"\nThe given list did not possess any None value!"

    # first getting the None values
    old: list = lis.copy()
    for (
        n
    ) in (
        old
    ):  # for edge cases [none, none,...] iteration and remove will skip consecutive values
        if n is None:
            lis.remove(n)  # iterating over copy and modifying original

    return f"Old List: {old} \n New List: {lis}"


# print(rem_Non([1,23,None, None]))


# 29. Write a function to merge two dictionaries and handle key collisions by summing values.
def merge_dict2(*args: dict) -> str:
    # resultant dictionary
    result: dict = {}

    # finding the common keys and summing their values:
    for n in args:
        for key, value in n.items():
            if key in result:
                # only straight add when both are integers
                if type(value) == type(result[key]) == int:
                    result[key] += value
                # otherwise state that sum isn't possible
                elif result[key] != "Can't sum":
                    result[key] = "Can't sum"
            else:
                result[key] = value

    return f"Old Dictionaries: {args} \n New Dictionary: {result}"


# print(
#     merge_dict2(
#         {"name": "hamza", "age": 22},
#         {"name": "1", "age": 0},
#         {"name": "khan", "age": 10},
#     )
# )


# 30. Create a function to find unique elements present in only one of two lists.
def uniq_ele(lis1: list, lis2: list) -> str:
    # edge cases

    if not lis1:
        return f"Old Lists: {lis1,lis2}\n New List: {sorted(lis2)}"

    elif not lis2:
        return f"Old Lists: {lis1, lis2} \n New List: {sorted(lis1)}"

    if all(n in lis2 for n in lis1):
        return f"Both lists are similar!"

    # finding the unique elements
    result: list = []
    old: list = lis2.copy()

    for n in lis1:
        # appending the unique one's
        if n not in lis2 and n not in result:
            result.append(n)
        # removing the duplicates from lis2 (fast trick)
        elif n in lis2:
            lis2.remove(n)

    result += lis2

    # for duplicates in result
    if any(result.count(x) > 1 for x in result):
        dup: dict = {n: result.count(n) for n in result if result.count(n) > 1}

        for n in result.copy():
            if n in dup:
                count: int = dup[n]
                if count > 1:
                    result.remove(n)
                    dup[n] -= 1

    return f"Old Lists: {lis1, old}\n New List: {sorted(result)}"


# print(uniq_ele([1, 2, 3], []))
