import json

ADMIN_PASSWORD = "sara"

pwd = input("Admin Password: ")
if pwd != ADMIN_PASSWORD:
    print("❌ Wrong password")
    exit()
try:
    with open("students.json", "r") as f:
        students = json.load(f)
except:
    students = {}
while True:
    reg_no = input("Register Number (or 'q' to stop): ")

    if reg_no.lower() == "q":
        break

    if not reg_no.isdigit():
        print("❌ Only numbers allowed")
        continue

    if reg_no in students:
        print("❌ Register number already exists")
        continue

    name = input("Student Name: ")
    students[reg_no] = name
    print("✅ Student added")
    
#save
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

print("📁 All students saved successfully")
