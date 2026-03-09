AIM

To perform basic string operations in Python such as reversing a string, finding its length, checking whether it is a palindrome, converting letter cases, counting vowels, and verifying if a substring exists.

ALGORITHM

Start the program.
Store a string in a variable.
Display the reversed string using slicing.
Find the length of the string using the len() function.
Check whether the string is equal to its reversed form to determine if it is a palindrome.
Convert the string into uppercase and lowercase.
Use a loop to count the number of vowels in the string.
Check whether a specific substring is present in the string.
Display all the results.
Read a number from the user.
Use a loop to calculate and display the factorial values step by step.
Stop the program.

SOURCE CODE

text = "PYTHONPROGRAM"

print(text[::-1])

length = len(text)
print(length)

if text == text[::-1]:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")

print(text.upper())
print(text.lower())

v = "aeiouAEIOU"
vowel_count = 0

for letter in text:
    if letter in v:
        vowel_count += 1

print("Total vowels:", vowel_count)

part = "GRAM"

if text.count(part) > 0:
    print("Substring found")
else:
    print("Substring not found")

num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    fact = fact * i
    print(fact)
    i += 1


OUTPUT

MARGORPNOHTYP
13
It is not a Palindrome
PYTHONPROGRAM
pythonprogram
Total vowels: 3
Substring found
Enter a number: 6
1
2
6
24
120
720