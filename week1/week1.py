# Q1. Write a Python program to swap two variables of different types.
from typing import Any, List
import re
import random as r


def swap_nums(var1: Any, var2: Any):
    # num1, num2 = num2, num1 # 1. tuple unpacking

    # num1 = num2 # direct assigning (Doesn't wok)
    # num2 = num1

    # temp = num1  2. using temporary variable
    # num1 = num2
    # num2 = temp

    return var2, var1  # 3. tuple unpacking + return values


a, b = swap_nums(False, "kjkj")
# print(a,b)


"""
Important Question:

    Q.Why tuple unpacking works but direct assigning doesn't?
    Ans: Sequential assignment overwrites values, tuple unpacking preserves them by evaluating first and assigning later.
    -> it evalutes R.H.S first and create a temporary tuple to store right side values then assign it to left side
        line by line (kind of Simultaneously).
"""


# Q2. Take user input and display it back to the user.
def display_inp():
    user_inp = input("How have you been?")
    return user_inp


# print(display_inp())


# Q3. Write a program to check if a number is even or odd.
def check_even_odd():
    num = int(input("Enter your number: "))  # input always returns data in str
    rule = num % 2
    if rule == 0:
        print("Number is even!\n", rule)
    else:
        print("Number is odd!\n", rule)


# check_even_odd()


# Q4. Create a program that prints the multiplication table of a given number.
def print_table():
    num = int(input("Enter your number: "))
    if num == 0:
        print("Sorry! 0 is not valid")

    else:
        # num2 = 0  we already have i in loop
        for i in range(1, 11):
            # num2 +=  no need
            print(f"{num} x {i} = {num*i}")


# print_table()


def take_nums(word: str) -> List[int]:
    pattern: str = r"^\d+(\s*,\s*\d+)+$"
    msg: str = "Invalid! Enter at least 2 numbers.\n"
    while True:
        inp: str = input(f"Enter your numbers for {word} separated by (,): ").strip()
        if re.match(pattern, inp):
            return [int(i.strip()) for i in inp.split(",")]

        print(msg)


# Q5. Write a program to find the largest of three numbers.
def find_largest(nums: List[int]) -> tuple[str, int | None]:
    # it immediately terminates the function and print the statement
    if len(nums) == 0:
        return "No list found!", None

    larg_num = nums[0]  # take the first num to compare

    # if all the numbers are same
    if all(n == nums[0] for n in nums):
        return f"\nAll the numbers are equal in the list!", nums[0]

    for i in range(1, len(nums)):
        if larg_num < nums[i]:  # ignore if it is already large
            larg_num = nums[i]  # re-assign if it is small

    ind_large_num = nums.index(larg_num)

    return (
        f"\nI found it, {larg_num} at {ind_large_num} index is the largest number!",
        larg_num,
    )


"""
-> all():
    'Everyone must qualify'!

-> any():
    'Anyone can qualify'!
"""

# print(find_largest(take_nums("(for finding largest number)")))


# Q6. Convert temperature from Celsius to Fahrenheit.
def convert_temp():
    # validating the input
    while True:
        try:
            cel_temp = float(input("Enter your temperature(in Celsius): "))
            break

        except Exception as e:
            print("Enter a valid number please!\n")

    # converting into fahrenheit
    fah_temp = (cel_temp * 9 / 5) + 32

    # removing the 0 after decimal point
    cel_temp = int(cel_temp) if cel_temp.is_integer() else cel_temp
    fah_temp = int(fah_temp) if fah_temp.is_integer() else fah_temp

    # returning the final output
    return f"{cel_temp}\u00b0C = {fah_temp} F"


# print(convert_temp())


# Q7. Write a program to calculate the factorial of a number using a loop.
def factorial():
    # validating the number
    while True:
        try:
            num = int(input("Enter your number to calculate it's factorial: "))
            break
        except Exception as e:
            print("Enter a valid number!\n")

    # calculating factorial
    fact = num  # initial value
    for i in range(num - 1, 0, -1):
        result = fact * i
        print(f"{fact} * {i} = {result}.")
        fact = result

    return f"\nFactorial of {num} is {fact}."


# print(factorial())


# Q8. Create a program to count the number of vowels in a string.
def count_vowels():
    vowels = ["a", "e", "i", "o", "u"]  # array of valid vowels

    # taking valid string from user
    while True:
        inp = input("Enter your string(without spaces): ").lower().strip()
        if not inp.isalpha():
            print("Incorrect string!.\n")
            continue
        break

    # counting the vowels in given string
    counts = {vowels[i]: inp.count(vowels[i]) for i in range(len(vowels))}

    # printing the result
    print("\nThe number of vowels in your string are writtern below:\n")
    for key, val in counts.items():
        print(f"{key} : {val}.")

    tot_num = 0
    for i in counts.values():
        tot_num += i

    print(f"\nTotal no. of vowels: {tot_num}.")


# count_vowels()


# Q9. Write a Python script to reverse a given string.
def rev_str():
    # taking input
    while True:
        inp = input("Enter your string to reverse(without spaces): ")
        if not inp:
            print("Incorrect Input!\n")
        else:
            break

    # reversing the string
    new_str = []
    for i in range(len(inp) - 1, -1, -1):
        new_str.append(inp[i])

    # printing the final output
    return f"\nYour Old string: {[a for a in inp]}\nReversed string: {new_str}."


# print(rev_str())


# Q10. Check if a number is a palindrome.
def check_pallindrome():
    # taking input
    while True:
        try:
            inp = int(input("Enter your number(without spaces): "))
            break
        except Exception as e:
            print("Incorrect Input!\n")

    # checking if pallindrome
    # new_inp = ""
    # for i in range(len(inp) - 1, -1, -1):  -> good for strings
    #     new_inp += inp[i]

    new_inp = 0
    original_num = inp  # safe the number

    while inp > 0:
        last_digit = inp % 10  # extracting the last digit of every number
        new_inp = (
            new_inp * 10 + last_digit
        )  # increasing 1 new place and adding new digit
        inp //= 10  # eliminating the last digit

    if new_inp == original_num:
        return f"\nThe number '{original_num}' is pallindrome!"

    else:
        return f"\nThe number '{original_num}' is not pallindrome!"


# print(check_pallindrome())


# Q11. Write a program to find the sum of first N natural numbers.
def add_natural():
    # taking input
    while True:
        try:
            num = int(input("Enter your Natural number(without spaces): "))
            if num <= 0:
                print("Any natural number please!\n")
                continue
            break
        except ValueError:
            print(f"Incorrect Input!\n")

    # calculating sum
    # tot_sum = 0 -> fine but not efficient
    # for i in range(1, num + 1):
    #     tot_sum += i

    tot_sum = (
        num * (num + 1) // 2
    )  # -> formula from Guass's method. Mathematically Proven!
    word = "numbers" if num > 1 else "number"

    # printing the final message
    return f"\nThe sum of first '{num}' natural {word} is: '{tot_sum}'."


"""
1. Final Advice (Important for CS Students)

- Separate:

-> Business Logic (math calculation)

-> Presentation Logic (grammar / formatting)

- This is a professional programming habit and very important in real-world software development.


2. For a CS student aiming to become a Data Scientist, you should prefer:

-> Mathematical optimization

-> Proper exception handling

-> Strict input validation

-> Clean return formatting
"""

# print(add_natural())


# Q12. Create a number guessing game.
def num_guess_game():
    sec_num = r.randint(1, 10)  # generate a random number
    counts = 0

    while True:
        # taking a valid number from user
        while True:
            try:
                num = int(input("\nGuess a number between (1-10): "))
                break
            except ValueError:
                print("Incorrect Input! Please enter a number.\n")

        # unnecessary numbers check
        if num < 1 or num > 10:
            print("\nEnter between (1 - 10)!")
            continue

        counts += 1  # increase the counts

        # checking the user given number
        if sec_num == num:
            return f"\nCongratulations! You guessed it right in {counts} attempts."

        elif sec_num > num:
            print("\nTry a little higher!")  # no None bcz the function is running

        else:
            print("\nTry a little lower!")  # no None bcz the function is running


# print(num_guess_game())
# Q13. Write a program to print all prime numbers between a given range.
def prime_num():
    # taking a valid number from user
    while True:
        try:
            num = int(input("Enter a number to show prime numbers by it: "))
            if num < 2:
                print("Enter a valid positive number, 0, 1 are not prime!\n")
                continue
            break
        except ValueError:
            print("Incorrect Input! Please enter a number.\n")

    prime_list = []  # store all the prime numbers

    # finding all the prime numbers
    for i in range(2, num + 1):
        is_prime = True

        for x in range(2, int(i**0.5) + 1):
            if i % x == 0:  # check for divisors
                is_prime = False

        if is_prime:
            prime_list.append(i)

    # returning the final result
    word2 = "numbers" if len(prime_list) > 1 else "number"
    return (
        f"\nAll prime {word2} by {num}: {prime_list}.",
        f"\nTotal numbers count: {len(prime_list)}",
    )


"""
MAIN LOGIC:
-> A number is prime if no number from 2 to √n divides it.

-> That's the entire idea behind this code.
"""
# res = prime_num()
# res1, res2 = res  # tuple unpacking
# print(res1, res2)


# Q14. Check if a given year is a leap year or not.
# import calendar as cl -> cl.isleap(year) directly
def check_leap_year():
    # taking a valid year
    while True:
        try:
            year = int(input("Enter your year between(1 to 9999): "))
            if 0 < year <= 9999:
                break
            else:
                print("Enter between (1 to 9999).\n")

        except ValueError:
            print("Incorrect Input!\n")

    # checking the year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"\nThe year {year} is a leap year."
    else:
        return f"\nThe year {year} is not a leap year."


"""
<< Simple Memory Trick >>

> Think of it like this:

1. Divisible by 4 → Leap year.
2. Divisible by 100 → Not leap year.
3. Divisible by 400 → Leap year again.
"""

# print(check_leap_year())

# Q15. Create a program to print the Fibonacci series up to N terms.
"""
The Fibonacci series is a sequence of numbers where:
    Each number is the sum of the two numbers before it.
"""


def print_fib_ser():
    # taking a valid number
    while True:
        try:
            n = int(input("Enter your number to see Fibonacci Series by it: "))
            if n <= 0:
                print("Invalid number! (must be > 0).\n")
                continue
            elif n in [1, 2]:
                return "0" if n == 1 else "0, 1"
            break
        except ValueError:
            print("Incorrect Input!\n")

    # printing Fabonacci series by num
    tot_terms = [0, 1]
    for i in range(n - 2):
        new_term = tot_terms[-1] + tot_terms[-2]
        tot_terms.append(new_term)

    return f"\nFibonacci Series till {n}th term: {tot_terms}"


# print(print_fib_ser())


# 16. Write a program to find GCD of 2 numbers.
"""
- The GCD of two or more numbers is the largest number that divides all of them without leaving a remainder.

"Euclidean Algorithm ⭐ (Most Important)":
    * GCD(a, b) = GCD(b, a mod b).
    - Keep applying this until the remainder becomes 0. The last non-zero number is your GCD

"""


def take_input(prompt: str) -> int:
    msg = "Enter a valid positive number please!\n"
    while True:
        try:
            val = int(input(prompt).strip())
            if val < 0:
                print(msg)
                continue
            return val  # safely return

        except ValueError:
            print(msg)


def calc_gcd(a: int, b: int) -> int:
    if b == 0:
        print(f"\n(b is already 0) So,")
    else:
        while b:
            mod: int = a % b
            print(f"{a} % {b} = {mod}")
            a, b = b, mod

    return a


def print_gcd() -> str:
    a = take_input("Enter your 1st Positive number(for GCD): ")  # ignores the
    b = take_input("Enter your 2nd Positive number(for GCD): ")  # - sign
    spc_msg = "\nGCD is undefined for (0,0)"

    # special case
    if a == b == 0:
        return spc_msg

    res = calc_gcd(a, b)

    return f"\nThe GCD of {a} and {b} is {res}."


# print(print_gcd())

# 17. Write a program to find LCM of 2 or more numbers.
"""LCM stands for Least Common Multiple.
The LCM of two or more numbers is the smallest number that is divisible by all of them.
"""


def find_lcm() -> str:
    a: int = take_input("Enter your 1st positive number: ")
    b: int = take_input("Enter your 2nd positive number: ")
    spc_msg = "\nGCD is undefined for (0, 0). So, LCM is also undefined."

    # special case
    if a == b == 0:
        return spc_msg

    # showing formula
    print("\nLCM(a,b) = |a x b| / GCD(a,b)")

    # printing GCD
    print(f"\n\tFor GCD({a}, {b}):")
    res = calc_gcd(a, b)

    gcd: int = int(res)
    lcm = (a * b) // gcd  # // to ignore after . number

    return f"\nThe LCM of {a} and {b} is {lcm}."


# print(find_lcm())


# 18. Check whether a character is a vowel or consonant?
def check_char() -> str:
    vowels: str = "aeiou"
    while True:
        char: str = input("Enter your character: ").strip().lower()
        # only 1 character
        if len(char) > 1:
            print("Only one character at a time please!\n")
            continue
        # if it is a valid character
        if not char.isalpha():
            print("Enter any valid character please!\n")
            continue
        # safely end the loop
        break

    if char in vowels:
        return "\n\tIt is a vowel!"

    else:
        return "\n\t It is a consonant!"


# print(check_char())


# 19. Write a program to calculate the sum of digits of a number.
def dig_sum() -> str:
    while True:
        num: str = input("Enter your number to sum its digits: ")
        ln: int = len(num)

        if ln == 1:
            print("The number must have 2 or more digits!\n")
            continue
        elif not num.isdigit():
            print("Enter a valid number! \n")
            continue
        break

    total: int = int(num[0])

    for i in range(1, ln):  # loop runs len(num) -1 times (which is default).
        result: int = total + int(num[i])  # now the num behaves like a list
        print(f"{i}. {total} + {num[i]} = {result}")
        total = result

    return f"\nThe sum is: {total}."


# print(dig_sum())

# 16.2 Calculate the GCD of all the given number


def get_gcd_result() -> str:
    gcd_nums: List[int] = take_nums("GCD")

    # check for 0
    if all(n == 0 for n in gcd_nums):
        return "\nAll the numbers are 0. So, the GCD is 0."

    # calculating GCD using previous function
    result: int = gcd_nums[0]
    for n in gcd_nums[1:]:
        print(f"\n\tCalculating GCD of {result} and {n}:")
        result = calc_gcd(result, n)  # repeating the process for other numbers

    return f"\nThe GCD of {gcd_nums} = {result}."


# print(get_gcd_result())

# 17.2 Calculate the LCM of more then 2 numbers.


def get_lcm_results() -> str:
    lcm_nums: List[int] = take_nums("LCM")

    # check for all zero numbers
    if any(n == 0 for n in lcm_nums):
        return "\nLCM is 0. Since one or more numbers are zero, the LCM is 0 by convention."

    # calculating
    result: int = lcm_nums[0]
    for i in lcm_nums[1:]:
        gcd: int = calc_gcd(result, i)  # finds GCD between 2 nums
        new_lcm = (result * i) // gcd  # calculates their LCM
        print(f"\nLCM of {result} and {i} = {new_lcm}.\n")
        result = new_lcm

    return f"\nThe LCM of {lcm_nums} = {result}."


# print(get_lcm_results())
# 20. Create a program to find the second largest number in a list.


def sec_largest() -> str:
    nums = take_nums("(finding 2nd largest number)")  # take input at least 2 numbers

    # if all numbers are same
    if all(n == nums[0] for n in nums):
        return f"\nAll the numbers are equal to {nums[0]}."

    first: int = nums[0]
    second: int | None = None
    # second: int = nums[1] # wrong

    # safety check
    if second is None:
        return "\nNo 2nd largest found."

    for i in range(1, len(nums)):
        if nums[i] == first:
            pass
        elif nums[i] > first:
            second = first  # sent first to back
            first = nums[i]  # bring that number to first

        elif nums[i] < first and (second is None or nums[i] > second):
            second = nums[i]

    return f"\n2nd largest number is {second} at {nums.index(second)} index."


# print(sec_largest())


# 21. Write a program to count the number of digits in an integer.
def count_dig() -> str:
    # return a positive number
    num: int = take_input("Enter your number positive: ")

    # len of digits
    ln_dig: int = len(str(num))

    word: str = "are" if ln_dig > 1 else "is"
    return f"\nNumber of digits in your number {num} {word}, {ln_dig}."


# print(count_dig())


# 22. Create a program to print all Armstrong numbers between 1 to 1000.
"""
-> Armstrong Number:
        'AKA Narcissistic Number is a number that equals the sum of its own digits each raised
        to the power of the number of digits.
        e.g. 153 -- 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
"""

# print("\n\tArmstrong Numbers: 1 - 1000")


def get_Armstrong(to: int = 1000) -> str:
    armstg_nums: List[int] = []
    for i in range(to + 1):
        num_sum: int = 0  # to safe the sum

        # convert the number into string for looping
        str_num: str = str(i)

        # loop to sum the digits of a number
        for n in str_num:
            # raising every digit to the number of digits
            num_sum += int(n) ** len(str_num)

        # if the sum = to the number (Armstrong)
        if num_sum == i:
            armstg_nums.append(i)

    return f"\nThe number of Armstrong Numbers between 1 - {to} are: {armstg_nums}."


# print(get_Armstrong())

# -> Without the inner loop


def get_Armstrong_eff(to: int = 1000) -> str:
    armstg_nums: List[int] = []
    for i in range(to + 1):
        # convert the number into string for looping
        str_num: str = str(i)

        # break the digits, raise them to the number of digits, add them
        # num_sum: int = sum([int(n)**len(str_num) for n in str_num]) # List comprehension (slow)

        # generator
        num_sum: int = sum(int(n) ** len(str_num) for n in str_num)

        # if the sum = to the number (Armstrong)
        if num_sum == i:
            armstg_nums.append(i)

    return f"\nThe number of Armstrong Numbers between 1 - {to} are: {armstg_nums}."


# print(get_Armstrong_eff())


# 23. Write a Python program to print a pattern of stars in a triangle.
def get_stars(row: int | None = None):
    if not row or row <= 0:
        print(f"\nInvalid input!")
        return

    for i in range(1, row + 1):
        print(" " * (row - i) + "*" * (2 * i - 1))
        #         spaces    +   stars


# get_stars()


# Q25. Write a program to display the ASCII value of a character.
def get_chr_num() -> str | int:
    msg: str = "Enter any valid ASCII number between 0 - 127 or a valid character!\n"
    asc_val: str | int = 0
    while True:
        try:
            inp: str = input(
                "Enter your character or number to print it's number or character: "
            )

            # check if it is not a combo of str and int and must be a character
            if len(inp) == 1:
                return inp

            # check if it is a valid number
            asc_val = int(inp)

        except ValueError:
            print(msg)

        else:
            # only check it it is a number
            if 0 <= asc_val <= 127:
                return asc_val
            else:
                print("Enter any number between 0 - 127!\n")


def get_ascii_val() -> str | None:
    res: str | int = get_chr_num()

    # for int values
    if type(res) == int:
        return f"\nThe character having ASCII value {res} is {chr(res)}."

    # safety check
    if not type(res) == str:
        return None

    # finally for characters
    return f"\nThe ASCII value of {res} is {ord(res)}."


# print(get_ascii_val())


# Q26. Convert a decimal number to binary using loops.
def convert_dec_bin() -> str:
    msg: str = "Enter any positive number please!\n"
    # taking the number
    while True:
        try:
            usr_num: int = int(input("Enter your number:"))
            if usr_num == 0:
                return f"\nThe binary number of 0 is 0"

            elif usr_num < 0:
                print(msg)

            else:
                break

        except ValueError:
            print(msg)

    # converting the number into binary form
    bin_list: List[str] = []  # store the binary numbers
    old: int = usr_num  # store the original number

    while usr_num:
        bin_num: int = usr_num % 2  # return 0 or 1 (binary)
        bin_list.insert(0, str(bin_num))  # put it in the list (reverse order)
        usr_num //= 2

    res: str = "".join(bin_list)  # join the list into a string
    return f"\nThe binary number of {old} is {res}"


# print(convert_dec_bin())


# Q27. Create a program to find the square root of a number.
"""
=> By using Newton's Method:
- The idea: make a guess, then keep improving it using this formula:
- You repeat this until the guess is "close enough" to the real answer (within a tiny tolerance like 0.00001).
    It converges very fast — each iteration roughly doubles the number of correct digits.

    next_guess = (guess + n / guess) / 2
    where:
        guess : 1 or n/2
        n : The number you want to find the square root of.
"""


def calc_sqrt() -> str:
    msg: str = "Enter any positive number please!\n"
    # taking the number
    while True:
        try:
            usr_num: int = int(input("Enter your number(for square root): "))
            if usr_num == 0:
                return f"\nThe square root of 0 is 0"

            elif usr_num < 0:
                print(msg)

            else:
                break

        except ValueError:
            print(msg)

    # calculating
    guess: float = 1.0
    tolerance: float = 0.00001  # minimum value
    next_guess: float | int = 0
    while True:
        # getting more closer
        next_guess = (guess + usr_num / guess) / 2
        # checking the difference
        if abs(guess - next_guess) < tolerance:
            break
        guess = next_guess

    # convert into integer when the answer in also an integer
    result = int(next_guess) if next_guess.is_integer() else round(next_guess, 2)

    return f"\nThe square root of {usr_num} is {result}."


# print(calc_sqrt())


# Q28. Write a program to find the sum of all even numbers in a list.
def even_sum() -> str:
    num_list: List[int] = []
    msg: str = "Enter at least 2 positive number!\n"
    while True:
        try:
            inp: int = int(input("Enter Your numbers(0 to exit): "))

            if inp == 0:
                if len(num_list) >= 2:
                    print(f"\nList: {num_list}")
                    break
                else:
                    print(msg)

            elif inp < 0:
                print(msg)

            else:
                print(f"Added {inp} successfully!\n")
                num_list.append(inp)

        except ValueError:
            print(msg)

    # calculating
    result: int = 0
    for n in num_list:
        if n % 2 == 0:
            result += n

    return (
        f"Sum of even numbers in your list: {result}"
        if result
        else "\nNo even number exists in your list!"
    )


# print(even_sum())


# Q29. Create a program to check whether a number is prime or not.
def check_prime() -> str:
    msg: str = "Enter any positive number >= 2!\n"
    while True:
        try:
            num: int = int(input("Enter your number(to check is it prime or not): "))
            if num >= 2:
                break

            print(msg)
        except ValueError:
            print(msg)

    # finding if it is prime or not
    is_prime: bool = True  # to counter edge cases
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            is_prime = False
            break  # exit early

    word: str = "a" if is_prime else "not a"
    return f"\n{num} is {word} prime number!"


# print(check_prime())


# Q30. Write a program to display the cube of the number up to an integer.
def print_cube() -> None:
    msg: str = "Enter any positive number please!\n"
    while True:
        try:
            num: int = int(input("Enter your number:"))
            if num > 0:
                break
            print(msg)
        except ValueError:
            print(msg)

    # calculating
    for n in range(1, num + 1):
        print(f"{n}\u00B3 = {int(n)**3}")


print_cube()
