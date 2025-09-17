from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample student data
students = [
    {"id": 1, "name": "Shravani"},
    {"id": 2, "name": "Anjali"}
]

# Home route
@app.route('/')
def home():
    return "🎓 Student API is Running!"

# GET all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# POST a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = {
        "id": students[-1]["id"] + 1 if students else 1,
        "name": data["name"]
    }
    students.append(new_student)
    return jsonify(new_student), 201

# Run the app
if __name__== '__main__':
    app.run(debug=True)
   
