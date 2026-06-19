#Exercise 4 — Phone Contact Deduplicator
#Topics: Lists · Sets · Strings · Loops

#Create a list of at least 15 contact names from your own phone. Deliberately repeat 5 with slight variations (e.g. "Tunde" and "tunde " with a trailing space). Write a program that cleans whitespace, normalises case, detects duplicates using sets, and prints a cleaned contact list with a duplicate report.
#
# phonebook contains contacts saved in a phone
phonebook = ( "precious", "Precious", "Treasure", "treasure",
    "george", "George", "chisom", "Chisom",
    "promise", "Promise", "Princess", "princess",
    "mAra", "mara", "MARA", "vicky", "Vicky")

# Empty list to store corrected names without duplicates
final_list = []

# Empty set to store names that appear more than once using the for loop
duplicates = set()

# Loop through each contact in the phonebook
for entry in phonebook:

    # Remove extra spaces and convert the name to title case
    # e.g., "mAra" becomes "Mara"
    corrected = entry.strip().title()

    # Check if the corrected name is already in final_list
    if corrected in final_list:

        # If yes, add it to duplicates
        duplicates.add(corrected)

    else:

        # If no, add it to final_list
        final_list.append(corrected)

# Display the corrected list of unique contacts
print("Corrected list:", final_list)

# Display the names that had duplicates
print("Duplicates:", duplicates)