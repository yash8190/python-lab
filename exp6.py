AIM

To implement basic dictionary operations in Python such as accessing values, displaying keys and values, checking length, modifying entries, copying dictionaries and iterating through dictionary elements.

ALGORITHM

Start the program.
Create a dictionary contacts containing person names as keys and their mobile numbers as values.
Use a for loop with items() to display each name and phone number.
Ask the user to enter a name to search in the dictionary.
Check whether the entered name exists in the dictionary.
If the name exists, display the phone number of that person.
Otherwise display a message saying the contact is not available.
Display the phone number using the get() function.
Display all the values using values().
Display all the keys using keys().
Display all the key–value pairs using items().
Update one of the values in the dictionary using update().
Display the dictionary after the update.
Delete one element using del.
Display the dictionary after deletion.
Remove another element using pop().
Display the dictionary after the pop operation.
End the program.

SOURCE CODE

contacts = {
            "Rahul": "9876543210",
            "Anita": "9123456780",
            "Karan": "9988776655",
            "Meera": "9090909090",
            "Arjun": "9812345678",
            "Pooja": "9700012345"
           }

for person, number in contacts.items():
    print(person, ":", number)

search_person = input("Enter name to search: ")

if search_person in contacts:
    print(search_person + "'s phone number is", contacts[search_person])
else:
    print("Contact not found")

print("\n--- Dictionary Functions ---")

print("Using get():", contacts.get("Rahul"))
print("Values:", contacts.values())
print("Keys:", contacts.keys())
print("Items:", contacts.items())

contacts.update({"Meera": "9998887776"})
print("After update:", contacts)

del contacts["Karan"]
print("After delete:", contacts)

contacts.pop("Pooja")
print("After pop:", contacts)

OUTPUT

Rahul : 9876543210
Anita : 9123456780
Karan : 9988776655
Meera : 9090909090
Arjun : 9812345678
Pooja : 9700012345

Enter name to search: Rahul
Rahul's phone number is 9876543210

--- Dictionary Functions ---

Using get(): 9876543210
Values: dict_values(['9876543210', '9123456780', '9988776655', '9090909090', '9812345678', '9700012345'])
Keys: dict_keys(['Rahul', 'Anita', 'Karan', 'Meera', 'Arjun', 'Pooja'])
Items: dict_items([('Rahul', '9876543210'), ('Anita', '9123456780'), ('Karan', '9988776655'), ('Meera', '9090909090'), ('Arjun', '9812345678'), ('Pooja', '9700012345')])

After update: {'Rahul': '9876543210', 'Anita': '9123456780', 'Karan': '9988776655', 'Meera': '9998887776', 'Arjun': '9812345678', 'Pooja': '9700012345'}

After delete: {'Rahul': '9876543210', 'Anita': '9123456780', 'Meera': '9998887776', 'Arjun': '9812345678', 'Pooja': '9700012345'}

After pop: {'Rahul': '9876543210', 'Anita': '9123456780', 'Meera': '9998887776', 'Arjun': '9812345678'}