CREATE TABLE Cohort (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL
);

CREATE TABLE Student (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    First_Name TEXT NOT NULL, 
    Last_Name TEXT NOT NULL, 
    Slack_Handle TEXT NOT NULL, 
    Cohort_Id INTEGER,
    FOREIGN KEY(Cohort_Id) REFERENCES Cohort(Id)
);

CREATE TABLE Instructor (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    First_Name TEXT NOT NULL, 
    Last_Name TEXT NOT NULL, 
    Slack_Handle TEXT NOT NULL, 
    Specialty TEXT NOT NULL,
    Cohort_Id INTEGER,
    FOREIGN KEY(Cohort_Id) REFERENCES Cohort(Id)
);

CREATE TABLE Exercise (
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL, 
    Language TEXT NOT NULL 
);


CREATE TABLE StudentExercises ( 
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Student_Id INTEGER,
	Exercise_Id INTEGER,
	FOREIGN KEY(Student_Id) REFERENCES Student(Id),
	FOREIGN KEY(Exercise_Id) REFERENCES Exercise(Id)
);

INSERT INTO COHORT (Name)
	VALUES ('Cohort 38');
INSERT INTO COHORT (Name)
	VALUES ('Cohort 39');
INSERT INTO COHORT (Name)
	VALUES ('Cohort 40');


INSERT INTO EXERCISE (Name, Language)
	VALUES ('Daily Journal', 'Javascript');
INSERT INTO EXERCISE (Name, Language)
	VALUES ('Student Exercises', 'Python');
INSERT INTO EXERCISE (Name, Language)
	VALUES ('Perennial', 'Javascript React');
INSERT INTO EXERCISE (Name, Language)
	VALUES ('Nutshell', 'HTML & CSS');
INSERT INTO EXERCISE (Name, Language)
	VALUES ('Chicken Dolphin', 'Ruby');
INSERT INTO EXERCISE (Name, Language)
	VALUES ('Chicken Monkey', 'Javascript');

INSERT INTO INSTRUCTOR 
	(First_Name, Last_Name, Slack_Handle, Specialty, Cohort_Id)
		VALUES 
			('Bilinda', 'Butcher', '@bilindab', 'Singing', 1);
INSERT INTO INSTRUCTOR 
	(First_Name, Last_Name, Slack_Handle, Specialty, Cohort_Id)
		VALUES 
			('Kevin', 'Shields', '@kshield', 'Guitar playing', 2);
INSERT INTO INSTRUCTOR 
	(First_Name, Last_Name, Slack_Handle, Specialty, Cohort_Id)
		VALUES 
			('Elizabeth', 'Frasier', '@elizafree', 'Spouting Nonsense', 3);

INSERT INTO STUDENT 
		(First_Name, Last_Name, Slack_Handle, Cohort_Id)
			VALUES 
				('Kim', 'Gordon', '@kgordon', 1);
INSERT INTO STUDENT 
		(First_Name, Last_Name, Slack_Handle, Cohort_Id)
			VALUES 
				('Sally', 'Gordon', '@sgordon', 1);
INSERT INTO STUDENT 
		(First_Name, Last_Name, Slack_Handle, Cohort_Id)
			VALUES 
				('Devi', 'Evers', '@devers', 2);
INSERT INTO STUDENT 
		(First_Name, Last_Name, Slack_Handle, Cohort_Id)
			VALUES 
				('Josie', 'Juniper', '@jjunie', 2);
INSERT INTO STUDENT 
		(First_Name, Last_Name, Slack_Handle, Cohort_Id)
			VALUES 
				('Frank', 'Wright', '@fwright', 3);
INSERT INTO STUDENT 
		(First_Name, Last_Name, Slack_Handle, Cohort_Id)
			VALUES 
				('Freddy', 'Nietzsche', '@fneitzsche', 3);
INSERT INTO STUDENT 
		(First_Name, Last_Name, Slack_Handle, Cohort_Id)
			VALUES 
				('Klaus', 'Klee', '@klee', 3);

INSERT INTO StudentExercises
	(Student_Id, Exercise_Id)
		VALUES
			(1, 1);
INSERT INTO StudentExercises
	(Student_Id, Exercise_Id)
		VALUES
			(2, 3);
INSERT INTO StudentExercises
	(Student_Id, Exercise_Id)
		VALUES
			(4, 2);










