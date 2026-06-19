#Exercise 1 — Your Name, Your Cipher
#Topics: Strings · Variables · Loops

#Store your full name in a variable. Write a program that shifts every letter forward by the number of characters in your first name (wrapping Z → A). Print the encrypted version, then write the reverse function to decrypt it back.

# Store the full name as a string
myFullname = ("Emmanuel Princess Chinemerem")

# Display the full name
print(myFullname)

# Split the full name into separate words using spaces as separators
names = myFullname.split()
print(names)

# Extract the second name (index 1)
firstname = names[1]
print(firstname)

# Print the number of letters in the second name
print(len(firstname))

# Store the length of the second name in a variable called count
count = len(firstname)
print(count)

# Loop through each character in the full name and print it
for letter in myFullname:
    print(letter)

# Loop through each character and print its ASCII/Unicode value
# ord() converts a character to its corresponding number
for letter in myFullname:
    print(ord(letter))

# Encrypt each character by shifting its ASCII value by 'count'
for letter in myFullname:

    # Convert the character to its ASCII value
    number = ord(letter)

    # Add the value of count to the ASCII number
    result = number + count

    # Convert the new ASCII value back to a character
    newletter = chr(result)

    # Print the encrypted character
    print(newletter)

# Encrypt the name using Caesar Cipher
# This shifts only letters and leaves spaces unchanged
for letter in myFullname:

    # Check if the character is an alphabet
    if letter.isalpha():

        # Determine whether the letter is uppercase or lowercase
        base = ord('A') if letter.isupper() else ord('a')

        # Shift the letter by 'count' positions and wrap around the alphabet
        result = (ord(letter) - base + count) % 26 + base

        # Convert back to a character and print on the same line
        print(chr(result), end="")

    else:
        # Print spaces or other non-letter characters unchanged
        print(letter, end="")