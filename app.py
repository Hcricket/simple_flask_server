from flask import Flask,jsonify
app = Flask(__name__) 
students = [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
        {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
        {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
        {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
        {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
        {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
        {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
        {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
        {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
        {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
    ]



@app.route("/old_students/",methods=['GET'])
def old_students():
    result =[]
    for student in students:
      if student["age"]>20:
        result.append(student)
    return jsonify(result)

@app.route("/young_students/",methods=['GET'])
def young_students():
  young_students = []
  for student in students:
     if student["age"]<21:
        young_students.append(student)
  return jsonify( young_students )

@app.route("/advance_students",methods=['GET'])
def advance_students():
   advance_students = []
   for student in students:
      if student["age"]<21 and student["grade"]=="A":
          advance_students.append(student)
   return jsonify(advance_students)

@app.route("/student_names",methods=['GET'])
def student_names():
    student_names = []
    for student in students:
        student_names.append({"first_name":student["first_name"],
                      "last_name":student["last_name"] 
                      })
    return jsonify(student_names)

@app.route("/student_age",methods=['GET'])
def student_age():
    student_age = []
    for student in students:
       full_name = student["first_name"] + " " + student["last_name"]
       student_age.append({
            "student_name": full_name,
            "age" : student ["age"]      
       })
    return jsonify(student_age)

@app.route("/students/")
def all_students():
    return jsonify(students)

if __name__ == '__main__':

    app.run (debug=True,port=5500)