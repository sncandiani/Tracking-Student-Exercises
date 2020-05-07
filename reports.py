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
    def student_exercises(self): 
        """Retreiving student exercise associations"""
        with sqlite3.connect(self.db_path) as conn:
            # Create a dictionary containing exercises to change data structure
            exercises = dict()
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT 
	        e.Id as Exercise_Id, 
	        e.Name, 
	        s.Id as Student_Id, 
	        s.First_Name, 
	        s.Last_Name
            FROM Exercise as e 
            JOIN StudentExercises as se on se.Exercise_Id = e.Id
            JOIN Student as s on s.Id = se.Student_Id;
            """)
            student_exercises = db_cursor.fetchall()
            # iterate through rows
            for row in student_exercises:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'
                if student_name not in exercises:
                    #  ????????? IF VS ELSE STATEMENT WHAT DO THEY DO DIFFERENT
                    exercises[student_name] = [exercise_name]
                else:
                    # append student name to pre-existing exercise
                    exercises[student_name].append(student_name)
            # key and values in the dictionary
            for student_name, exercises in exercises.items():
                print(f"{student_name} is working on:")
                for exercise in exercises:
                    # starred list of the values which are the exercises
                    print(f'\t* {exercise}')
# ?????????? WHY ARE ONLY ONE OF MY INSTRUCTORS SHOWING UP AND WHY DO THEY ID'S NOT LINK IN THE SQL ):
    def instructor_assignments(self): 
        """Retreive assignments that instructors have given to students"""
        with sqlite3.connect(self.db_path) as conn:
            exercises = dict()
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT 
	        e.Id as Exercise_Id, 
	        e.Name, 
	        i.Id as Instructor_Id, 
	        i.First_Name, 
	        i.Last_Name
            FROM Exercise as e 
            JOIN StudentExercises AS se ON se.Exercise_Id = e.Id
            JOIN Instructor AS i on i.Id = se.Instructor_Id;
            """)
            instructor_assigned = db_cursor.fetchall()
            for row in instructor_assigned: 
                # naming data in list of tuples
                exercise_id = row[0]
                exercise_name = row[1]
                instructor_id = row[2]
                instructor_name = f'{row[3]} {row[4]}'
                # if the following key is not in exercises dictionary
                if instructor_name not in exercises: 
                    # instructor name is the key and exercise name is the value
                    exercises[instructor_name] = [exercise_name]
                else: 
                    # will append values to existing list 
                    exercises[instructor_name].append(exercise_name)
            
            for instructor_name, exercises in exercises.items(): 
                print(f"{instructor_name} has assigned:")
                for exercise in exercises: 
                    print(f'\t* {exercise}')

    def exercises_for_students(self): 
        """Retreiving student exercise associations based on exercises"""
        with sqlite3.connect(self.db_path) as conn:
            exercises = dict()
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT 
	        e.Id as Exercise_Id, 
	        e.Name, 
	        s.Id as Student_Id, 
	        s.First_Name, 
	        s.Last_Name
            FROM Exercise as e 
            JOIN StudentExercises as se on se.Exercise_Id = e.Id
            JOIN Student as s on s.Id = se.Student_Id;
            """)
            student_exercises = db_cursor.fetchall()
            for row in student_exercises:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'
                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)
    
            for exercise_name, students in exercises.items():
                print(f"{exercise_name} is being worked on by:")
                for student in students:
                    # starred list of the values which are the exercises
                    print(f'\t* {student}')

    def tracking_exercises(self): 
        """Advanced challenge for student/instructor/exercise associations"""
        with sqlite3.connect(self.db_path) as conn:
            exercises = dict()
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT 
	        e.Id, 
	        e.Name, 
	        s.Id, 
	        s.First_Name, 
	        s.Last_Name, 
	        i.Id,
	        i.First_Name, 
	        i.Last_Name
            FROM Exercise AS e 
            INNER JOIN StudentExercises AS se ON se.Exercise_Id = e.Id
            INNER JOIN Student AS s ON s.Id = se.Student_Id
            INNER JOIN Instructor AS i ON i.Id = se.Instructor_Id;
            """)
            student_detailed_exercises = db_cursor.fetchall()
            for row in student_detailed_exercises: 
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'
            if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
            else:
                    exercises[exercise_name].append(student_name)
    
            for exercise_name, students in exercises.items():
                print(f"{exercise_name} is being worked on by:")
                for student in students:
                    # starred list of the values which are the exercises
                    print(f'\t* {student}')
    
    
    



reports = StudentExerciseReports()

# print("####STUDENTS & COHORT NAME######")
# reports.all_students()
# print("####INSTRUCTORS & COHORT NAME######")
# reports.all_instructors()
# print("#####COHORTS#####")
# reports.all_cohorts()
# print("####EXERCISES######")
# reports.all_exercises()
# print("####JS EXERCISES######")
# reports.js_exercises()
# print("####PYTHON EXERCISES######")
# reports.python_exercises()
# print("####C SHARP EXERCISES######")
# reports.csharp_exercises()
# print("####STUDENT CURRENT EXERCISES######")
# reports.student_exercises()
reports.instructor_assignments()
# reports.exercises_for_students()
# reports.tracking_exercises()

