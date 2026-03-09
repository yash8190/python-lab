# AIM
# To study and implement different Python operators and verify algebraic identities,
# bitwise relationships, and arithmetic operations like addition and subtraction.

# ALGORITHM
# 1. Start the program.
# 2. Declare two integer variables x and y with values 125 and 340.
# 3. Display a heading for algebraic identity verification.
# 4. Evaluate several algebraic formulas and print whether they are True or False.
# 5. Display a heading for bitwise operator relationships.
# 6. Apply bitwise operators such as AND, OR, and XOR and verify their relations.
# 7. Display a heading for addition verification.
# 8. Verify addition using bitwise operator formulas.
# 9. Display a heading for subtraction verification.
# 10. Verify subtraction using different bitwise expressions.
# 11. Print all evaluated results on the screen.
# 12. End the program.

# SOURCE CODE

x = 125
y = 340

print("Checking Algebraic Identities:\n")

print((x + y)**2 == (x**2 + 2*x*y + y**2))
print((x - y)**2 == (x**2 - 2*x*y + y**2))
print((x + y) + (x - y) == 2*x)
print((x**3 - y**3) == (x - y) * (x**2 + x*y + y**2))
print((x + y)**3 == (x**3 + y**3 + 3*x*y*(x + y)))

print("\nChecking Bitwise Operator Relationships:\n")

print((x | y) == ((x ^ y) | (x & y)))
print((x ^ (x & y)) == ((x | y) ^ y))
print((y ^ (x & y)) == ((x | y) ^ x))
print((x ^ y) == ((x | y) ^ (x & y)))

print("\nAddition Verification:\n")

print((x + y) == ((x ^ y) + 2*(x & y)))
print((x + y) == ((x | y) + (x & y)))

print("\nSubtraction Verification:\n")

print((x - y) == ((x ^ (x & y)) - (y ^ (x & y))))
print((x - y) == (((x | y) ^ y) - ((x | y) ^ x)))
print((x - y) == ((x ^ (x & y)) - ((x | y) ^ x)))

# OUTPUT
# Checking Algebraic Identities:
#
# True
# True
# True
# True
# True
#
# Checking Bitwise Operator Relationships:
#
# True
# True
# True
# True
#
# Addition Verification:
#
# True
# True
#
# Subtraction Verification:
#
# True
# True
# True