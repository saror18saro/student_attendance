import json
from datetime import date
try:
    with open("students.json", "r") as f:
        students = json.load(f)
except:
    print("❌ No students file found")
    exit()

if not students:
    print("❌ No students available")
    exit()

today = str(date.today())
class_name = "Data_Analysis_Class"
try:
    with open("attendance.json", "r") as f:
        attendance = json.load(f)
except:
    attendance = {}
attendance.setdefault(today, {})
attendance[today].setdefault(class_name, {})

print("\n📋 Taking Attendance (Present / Absent)\n")

for reg_no, name in students.items():
    while True:
        status = input(f"{reg_no} - {name} (P/A): ").strip().upper()

        if status == "P":
            status = "Present"
            break
        elif status == "A":
            status = "Absent"
            break
        else:
            print("❌ Enter only P or A")
    attendance[today][class_name][reg_no] = {
        "name": name,
        "status": status
    }
with open("attendance.json", "w") as f:
    json.dump(attendance, f, indent=4)

print("\n✅ Attendance saved (Present & Absent both stored)")
