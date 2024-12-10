from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from pymongo import MongoClient

# Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['students']
students = db['students']


def serialize_student(student):
    student['_id'] = str(student['_id'])  # Convert ObjectId to string
    return student

@app.route('/students', methods=['GET'])
def get_students():
    query = {"age": {"$gt": 18}}
    results = students.find(query)
    student_list = [serialize_student(student) for student in results]  # Serialize all students
    return jsonify(student_list)

@app.route('/students', methods=['POST'])
def insert_students():
    student_data = request.json
    students.insert_one(student_data)
    return jsonify({"message": "Student added successfully"}), 201

# Route for the front-end page to display the form
@app.route('/')
def index():
    return render_template('index1.html')

# Route to update student age
@app.route('/students/update', methods=['PUT'])
def update_student_age():
    data = request.get_json()
    name = data.get('name')
    new_age = data.get('age')
    
    # Find the student by name
    student = students.find_one({'name': name})
    
    if student:
        # Update the student's age
        students.update_one(
            {'_id': student['_id']},
            {'$set': {'age': new_age}}
        )
        return jsonify({'message': 'Student age updated successfully'}), 200
    else:
        return jsonify({'message': 'Student not found'}), 404

# Route to delete a student
@app.route('/students/delete', methods=['DELETE'])
def delete_student():
    data = request.get_json()
    name = data.get('name')
    
    # Find the student by name
    student = students.find_one({'name': name})
    
    if student:
        # Delete the student
        students.delete_one({'_id': student['_id']})
        return jsonify({'message': 'Student deleted successfully'}), 200
    else:
        return jsonify({'message': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)