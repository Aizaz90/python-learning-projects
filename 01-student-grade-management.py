students = [{"name":"Ali", "age": 20, "marks": 80}, {"name":"Hammad", "age": 19, "marks": 55} , {"name":"Aizaz", "age": 24, "marks":90}, 
          {"name":"Huzaifa", "age": 21, "marks": 67},{"name":"Nawaz", "age": 30, "marks": 76}, {"name": "Amaze" , "age": 21 , "marks": 77},
          { "name":"Wadood", "age": 27, "marks": 82} ,{"name":"Ali naazz", "age": 50, "marks": 40}, {"name":"Khami", "age": 26, "marks": 68},
          {"name":"Moez", "age": 24, "marks": 89}]

print(len(students))

for i in students:
     print(f"Name: {i['name']}, Age: {i['age']}, Marks: {i['marks']}")

passed_students = []
failed_students = []
for i in students:
     if i['marks'] > 70:
          passed_students.append(i)
          
     else:
         failed_students.append(i)

def get_marks(student):
     return student["marks"]

sorted_students = sorted(passed_students , key=get_marks , reverse= True)

print("\n--- Passed Students ---")
for i in sorted_students:
     print(f"Name : {i['name']}, Age: {i['age']}, Marks: {i['marks']} -> Pass")

sorted_failed = sorted(failed_students , key=get_marks, reverse=True)
print("\n--- Failed Students ---")
for i in sorted_failed:
        print(f"Name: {i['name']}, Age: {i['age']}, Marks: {i['marks']} -> Failed")

total_marks = 0
for i in students:
     total_marks += i["marks"]

avg_marks =total_marks/ len(students)
print(f"Total Marks: {total_marks}\n")
print(f"Average Marks: {avg_marks}")
print("DONE WITH THIS BASIC CODE")