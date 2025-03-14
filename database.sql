CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    batch_year INT
);

CREATE TABLE performance (
    student_id INT,
    subject VARCHAR(50),
    marks_obtained INT,
    total_marks INT,
    attendance FLOAT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
