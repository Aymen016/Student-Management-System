<p align="center">
  <img src="https://github.com/user-attachments/assets/56051ea0-4bb9-4bfe-b202-4e445e72c854" alt="Image 1" width="40%" />
  <img src= "https://github.com/user-attachments/assets/cfcfc0c8-1820-46eb-a8dc-448842143c07" alt="Image 2" width="40%" />
</p>



# 📝 Student Management System

## 🚀 Overview
This project implements a basic **Student Management System** using **Flask** as the web framework and **MongoDB** as the database. The application provides CRUD (Create, Read, Update, Delete) operations to manage student data.🎓

---

## 🛠️ Task 1: MongoDB Operations

### 1️⃣ Create a `students` Collection
- A MongoDB collection named `students` was created to store student data.📂

### 2️⃣ Insert Student Data
- Sample student documents were inserted into the `students` collection with fields like:
    ```json
    {
      "name": "John Doe",
      "age": 20,
      "grade": "A"
    }
    ```

### 3️⃣ Query All Students Older Than 18
- MongoDB query was used to retrieve all students whose age is greater than 18:
    ```json
    { "age": { "$gt": 18 } }
    ```

### 4️⃣ Update a Student’s Age
- The age of a specific student was updated using MongoDB’s `update_one` method.🔄

### 5️⃣ Delete a Student by Name
- A student document was deleted based on their `name` field.🗑️

---

## 🎯 Functionalities of the Application

### ➕ Add Student
- A form is provided to insert new student records into the database.📝

### 📋 View Students
- Displays all students in the `students` collection with filtering and sorting options.🔍

### 🖊️ Update Student Age
- Updates the `age` field of a specific student.🕒

### ❌ Delete Student
- Deletes a student record based on their name.🚮

---

## 💻 How to Run the Application

### 🛠️ Install Required Dependencies
Run the following command to install dependencies:
```bash
pip install flask pymongo
```

## 🌐 Set Up MongoDB
1. Ensure MongoDB is running locally or on a cloud platform (e.g., MongoDB Atlas).🌍
2. Update the connection string in the Flask application to point to your MongoDB instance.🔗

---

## 🚀 Run the Flask Application
Run the following command to start the application:
```bash
flask run
```
---

## 🌟 Access the Application
Open your browser and navigate to:

👉 http://localhost

---

## 👨‍💻 Contributor
Aymen016
GitHub Profile 🚀

---
## 📜 License
This project is licensed under the MIT License.

🎉 Happy Coding! ✨
