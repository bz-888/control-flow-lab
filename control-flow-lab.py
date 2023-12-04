# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

print("================================================================")
print("Exercise 01")
print("================================================================")

vowel = ["a", "e", "i", "o", "u"]

letter = input("Please enter a letter from the alphabet (a-z or A-Z): ").lower()

if letter in vowel:
    print(f"The letter {letter} is a vowel!")
else:
    print(f"The letter {letter} is a consonant!")



# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

print("================================================================")
print("Exercise 02")
print("================================================================")

phrase = ""

while phrase != "quit":

    phrase = input("Please enter a word or phrase: ").lower()

    if phrase == "quit":
        print("Quit was entered. I will stop asking for a word or phrase.")
    else:
        print(f"What you entered was {len(phrase)} characters long!")



# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

print("================================================================")
print("Exercise 03")
print("================================================================")

age_string = input("Input a dog's age: ")
age_integer = int(age_string)

if age_integer < 3:
    dog_years = age_integer * 10
else:
    dog_years = 20 + (age_integer - 2) * 7

print(f"The dog's age in dog years is {dog_years}!")



# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("================================================================")
print("Exercise 04")
print("================================================================")

print("Enter the lengths of three side of a triangle: ")
a = input("a: ")
b = input("b: ")
c = input("c: ")

if a == b == c:
    triangle_type = "equilateral"
elif a == b:
    triangle_type = "isosceles"
elif b == c:
    triangle_type = "isosceles"
elif c == a:
    triangle_type = "isosceles"
else:
    triangle_type = "scalene"

print(f"A triangle with sides of {a}, {b} & {c} is a(n) {triangle_type} triangle!")


# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

print("================================================================")
print("Exercise 05")
print("See below for the first 50 terms of the fibonacci sequence.")
print("================================================================")

num_0 = 0

for term in range(50):
    if term == 0:
        print(f"term: {term} / number: {num_0}")
        num_2_ago = 0
        num_1_ago = 0
        num_0 += 1
    elif term == 1:
        print(f"term: {term} / number: {num_0}")
        num_1_ago = num_0
    else:
        num_0 = num_1_ago + num_2_ago
        print(f"term: {term} / number: {num_0}")
        num_2_ago = num_1_ago
        num_1_ago = num_0




# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

print("================================================================")
print("Exercise 06")
print("================================================================")

month_str = input("Enter the month of the year (Jan - Dec): ")

all_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

while not(month_str in all_months):
    month_str = input("Enter a valid month of the year (Jan - Dec): ").capitalize()

day_str = input("Enter the day of the month: ")
day_int = int(day_str)

winter_months = ["Dec", "Jan", "Feb", "Mar"]
spring_months = ["Mar", "Apr", "May", "Jun"]
summer_months = ["Jun", "Jul", "Aug", "Sep"]
fall_months = ["Sep", "Oct", "Nov", "Dec"]

if month_str in winter_months:
    if month_str == "Dec":
        if day_int >= 21:
            season = "winter"
        else:
            season = "fall"
    elif month_str == "Mar":
        if day_int <= 19:
            season = "winter"
        else:
            season = "spring"
    else:
        season = "winter"
elif month_str in spring_months:
    if month_str == "Jun":
        if day_int <= 20:
            season = "spring"
        else:
            season = "summer"
    else:
        season = "spring"
elif month_str in fall_months:
    if month_str == "Sep":
        if day_int <= 21:
            season = "summer"
        else:
            season = "fall"
    else:
        season = "summer"
else:
    season = "fall"

print(f"{month_str} {day_int} is in {season}!")
    
    



