# Step 1: Creating a Dictionary
student = {
    "name": "Ritesh", 
    "age": 25,
    "enrolled_course": "Data Science",
    "Score": 88
}

print(student)


# Step 2: Access values
print(student["name"])                 # Ritesh
print(student.get("score"))            # 88
print(student.get("grade", "N/A"))     # Key dosen't exist; returns default


# Step 3: Update an existing value
student["score"] = 92
print(student)


# Step 4: Add new key
student["passed"] = True
print(student)


# Step 5: Delete Key
del student["enrolled_course"]
print(student)