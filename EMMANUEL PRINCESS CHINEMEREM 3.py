#Exercise 6 — Class Attendance Tracker
#Topics:Sets · Loops · Conditions

#Create a set of all students in your class (at least 10 names). Then create separate sets for students who attended Monday, Tuesday, and Wednesday. Use set operations to find who attended all 3 days, who missed at least one, who only came once, and who never attended at all.

# Set containing the names of all students in the class
Classgroup = { "Emmanuel", "Yusuf", "Joshua", "Jonathan",
    "Gabriel", "Festus", "Michael", "Felicia",
    "Cynthia", "Rochas", "Oscar"}

# Students who attended on Monday
Monday = { "Jonathan", "Joshua", "Cynthia", "Rochas", "Oscar"}

# Students who attended on Tuesday
Tuesday = {"Emmanuel", "Cynthia", "Rochas", "Gabriel", "Felicia"}

# Students who attended on Wednesday
Wednesday = {"Felicia", "Emmanuel", "Jonathan", "Joshua", "Cynthia"}

# Find students who attended ALL three days
# '&' means intersection (common elements)
always_present = Monday & Tuesday & Wednesday

# Find students who attended at least one day
# '|' means union (combine all elements without repetition)
any_day = Monday | Tuesday | Wednesday

# Find students who never attended any class
# '-' means difference (elements in Classgroup but not in any_day)
always_absent = Classgroup - any_day

# Find students who attended only one of the three days
# '^' means symmetric difference
only_oneday = Monday ^ Tuesday ^ Wednesday

# Display students who attended all three days
print("3 days present:", always_present)

# Display students who attended only one day
print("only one day present:", only_oneday)

# Display students who never attended
print("never attended:", always_absent)