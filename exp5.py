AIM

To write a Python program to demonstrate tuple operations such as accessing elements, finding length, counting values, locating index, identifying maximum and minimum values, sorting elements, reversing order, and iterating through the tuple.

ALGORITHM

Start the program.
Create a tuple studentdata containing student details like Name, Age, City, and Phone number.
Display a heading studentdata and a separator line.
Use a for loop to read each row in the tuple.
Display the student details (Name, Age, City, Phone number) in a formatted structure.
Print another separator line.
Create another tuple numbers = (5, 15, 25, 35, 15).
Display the tuple.
Access and print the first element using index numbers[0].
Access and print the last element using index numbers[-1].
Find and display the length of the tuple using len().
Find and display the maximum value using max().
Find and display the minimum value using min().
Find and display the sum of all elements using sum().
Sort the tuple using sorted() and display the result.
Count the occurrences of 15 using count().
Find the index position of 25 using index().
Terminate the program.

SOURCE CODE

studentdata = (("Name", "Age", "City", "Phone"),
               ("Rahul", 21, "Mumbai", 9876543210),
               ("Sneha", 23, "Delhi", 9123456780))

print("studentdata")
print("-" * 40)

for record in studentdata:
    print(record[0], "|", record[1], "|", record[2], "|", record[3])

print("-" * 40)

numbers = (5, 15, 25, 35, 15)

print("Tuple:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("Length:", len(numbers))
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted tuple:", sorted(numbers))

print("Count of 15:", numbers.count(15))
print("Index of 25:", numbers.index(25))

OUTPUT

studentdata
----------------------------------------
Name | Age | City | Phone
Rahul | 21 | Mumbai | 9876543210
Sneha | 23 | Delhi | 9123456780
----------------------------------------
Tuple: (5, 15, 25, 35, 15)
First element: 5
Last element: 15
Length: 5
Maximum value: 35
Minimum value: 5
Sum: 95
Sorted tuple: [5, 15, 15, 25, 35]
Count of 15: 2
Index of 25: 2