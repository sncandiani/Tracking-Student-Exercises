import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercise
from instructor import Instructor



class StudentExerciseReports():
    
    """Methods for reports on the Student Exercises database"""
    
    def __init__(self):
        self.db_path = "/Users/sofiac/backEndWorkspace/intro/exercises/Tracking-Student-Exercises/studentExercises.db"
    

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            # Row_factory is a method in conn which needs cursor and row parameters
            # Lambda is an anonymous function
            # Numbers are based on order of selection in execution
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.Cohort_Id,
                c.Name
            FROM Student s
            JOIN Cohort c on s.Cohort_Id = c.Id
            ORDER BY s.Cohort_Id
            """)

            all_students = db_cursor.fetchall()

            # Function __repr__ returns their first and last name and which cohort they are in
            # for student in all_students:
            #     print(student)
            # The following is the same as the for loop 
            [print(student) for student in all_students]
    def all_instructors(self): 
        """Retreive all instructors and their respective cohorts"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row [5]
            )
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT i.Id, 
            i.First_Name, 
            i.Last_Name, 
            i.Slack_Handle, 
            i.Cohort_Id,
            c.Name
            FROM Instructor i
            JOIN Cohort c on i.Cohort_Id = c.Id
            """)

            all_instructors = db_cursor.fetchall()

            [print (i) for i in all_instructors]

    def all_cohorts(self): 
         """Retrieve all cohorts"""
         with sqlite3.connect(self.db_path) as conn:
             conn.row_factory = lambda cursor, row: Cohort(
                row[0]
            )
             db_cursor = conn.cursor()
             db_cursor.execute("""
             SELECT c.name FROM Cohort AS c
             """)
             all_cohorts = db_cursor.fetchall()
            #  Cohort has a __repr__ function that returns the string rather than the object
             [print(c) for c in all_cohorts]
    
    def all_exercises(self): 
        """Retreive all exercises"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[0]
            )
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT e.name FROM Exercise AS e  
            """)
            all_exercises = db_cursor.fetchall()
            [print(e) for e in all_exercises]

    def js_exercises(self): 
        """Retreive only javascript exercises"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[0]
            )
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT e.name
            FROM Exercise AS e
            WHERE language = "Javascript"
            """)
            js_exercises = db_cursor.fetchall()
            [print(e) for e in js_exercises]
    
    def python_exercises(self): 
        """Retreive only python exercises"""
        with sqlite3.connect(self.db_path) as conn:
            # Makes tuple into object
            conn.row_factory = lambda cursor, row: Exercise(
                row[0]
            )
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT e.name 
            FROM Exercise e
            WHERE language = "Python" 
            """)
            python_exercises = db_cursor.fetchall()
            [print(e) for e in python_exercises]

    def csharp_exercises(self): 
        """Retreive only c# exercises"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[0]
            )
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT e.name 
            FROM Exercise e
            WHERE language = "C#" 
            """)
            csharp_exercises = db_cursor.fetchall()
            [print(e) for e in csharp_exercises]
    
    



reports = StudentExerciseReports()
print("####STUDENTS & COHORT NAME######")
reports.all_students()
print("####INSTRUCTORS & COHORT NAME######")
reports.all_instructors()
print("#####COHORTS#####")
reports.all_cohorts()
print("####EXERCISES######")
reports.all_exercises()
print("####JS EXERCISES######")
reports.js_exercises()
print("####PYTHON EXERCISES######")
reports.python_exercises()
print("####C SHARP EXERCISES######")
reports.csharp_exercises()

