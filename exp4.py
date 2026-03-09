AIM

To write a Python program that demonstrates various list operations such as accessing elements, inserting new items, copying lists, extending lists, searching for elements, sorting, reversing, deleting elements, counting occurrences, and slicing lists.

ALGORITHM

Start the program.
Create a list containing different course names.
Display a specific element from the list using its index.
Take a new course name from the user and add it to the list.
Display all the elements of the list using a loop.
Create a copy of the list and display it.
Extend the list with another list of course names.
Search for a particular element and display its index position.
Sort the list in alphabetical order.
Reverse the order of the list.
Remove the last element using pop.
Count the number of times a specific element appears.
Display a portion of the list using slicing.
End the program.

SOURCE CODE

courses = ["Python", "Java", "C", "C++", "HTML", "CSS", "JavaScript", "SQL"]

print("Original List:", courses)

print("Element at index 2:", courses[2])

new_course = input("Enter a course to add: ")
courses.append(new_course)

print("List after adding new course:", courses)

print("Displaying all courses:")
for item in courses:
    print(item)

copy_list = courses.copy()
print("Copied List:", copy_list)

extra_courses = ["AI", "Machine Learning", "Data Science"]
courses.extend(extra_courses)
print("After extending:", courses)

position = courses.index("SQL")
print("Position of SQL:", position)

courses.sort()
print("Sorted List:", courses)

courses.reverse()
print("Reversed List:", courses)

removed_item = courses.pop()
print("After pop:", courses)

count_item = courses.count("Python")
print("Count of Python:", count_item)

print("Sliced List (2 to 6):", courses[2:6])

OUTPUT

Original List: ['Python', 'Java', 'C', 'C++', 'HTML', 'CSS', 'JavaScript', 'SQL']
Element at index 2: C
Enter a course to add: PHP
List after adding new course: ['Python', 'Java', 'C', 'C++', 'HTML', 'CSS', 'JavaScript', 'SQL', 'PHP']

Displaying all courses:
Python
Java
C
C++
HTML
CSS
JavaScript
SQL
PHP

Copied List: ['Python', 'Java', 'C', 'C++', 'HTML', 'CSS', 'JavaScript', 'SQL', 'PHP']

After extending: ['Python', 'Java', 'C', 'C++', 'HTML', 'CSS', 'JavaScript', 'SQL', 'PHP', 'AI', 'Machine Learning', 'Data Science']

Position of SQL: 7

Sorted List: ['AI', 'C', 'C++', 'CSS', 'Data Science', 'HTML', 'Java', 'JavaScript', 'Machine Learning', 'PHP', 'Python', 'SQL']

Reversed List: ['SQL', 'Python', 'PHP', 'Machine Learning', 'JavaScript', 'Java', 'HTML', 'Data Science', 'CSS', 'C++', 'C', 'AI']

After pop: ['SQL', 'Python', 'PHP', 'Machine Learning', 'JavaScript', 'Java', 'HTML', 'Data Science', 'CSS', 'C++', 'C']

Count of Python: 1

Sliced List (2 to 6): ['PHP', 'Machine Learning', 'JavaScript', 'Java']