#Exercise 8 — The Vowel DNA Test
#Topics: Strings · Sets · Loops

#Combine your full name + your mother's full name + the street you grew up on into one string. Find: total characters (no spaces), unique letters as a set, vowel percentage, the most repeated letter, and whether the string contains all 5 vowels.

# Store the full name as a string
full_names = "Emmanuel Princess Chinemerem Emmanuel Chinwendu Nnenna Umuokpara Obehie"

# Display the original full names
print(full_names)

# Remove all spaces from the string
full_names2 = full_names.replace(" ", "")
print(full_names2)

# Count the total number of characters after removing spaces
total = len(full_names2)
print(total)

# Define the vowels to check for
vowels = "aeiou"

# Variable to count the number of vowels
total_characters = 0

# Loop through each letter in the string (converted to lowercase)
for letter in full_names2.lower():

    # Check if the letter is a vowel
    if letter in vowels:

        # Increase the vowel count by 1
        total_characters = total_characters + 1

# Display the total number of vowels
print(total_characters)

# Calculate the percentage of vowels in the string
percentage = (total_characters / total) * 100

# Display the vowel percentage
print(percentage)

# Find all unique letters in the string
unique_letters = set(full_names2.lower())

# Display the unique letters
print(unique_letters)

# Check if all vowels (a, e, i, o, u) are present in the string
present_vowels = set(vowels).issubset(set(full_names2.lower()))

# Display True if all vowels are present, otherwise False
print(present_vowels)

# Find the letter that appears the most times
most_repeated = max(
    set(full_names2.lower()),
    key=full_names2.lower().count)

# Display the most repeated letter
print(most_repeated)