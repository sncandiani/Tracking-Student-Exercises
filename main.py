from cohort import Cohort
from exercise import Exercise 
from instructor import Instructor 
from student import Student

daily_journal = Exercise("Daily Journal", "Javascript")
student_exercises = Exercise("Student Exercises", "Python")
perennial = Exercise("Capstone", "React")
nutshell = Exercise("Nutshell", "Javascript")

cohort_38 = Cohort("Cohort 38")
cohort_37 = Cohort("Cohort 37")
cohort_24 = Cohort("Cohort 24")
cohort_9 = Cohort("Evening Cohort 9")

bjork_g = Student("Bjork", "Guðmundsdóttir", "@bjorkg", cohort_9)
kate_bush = Student("Kate", "Bush", "@wutheringheights", cohort_38)
kurt_cobain = Student("Kurt", "Cobain", "@nirvana", cohort_37)
billy_holiday = Student("Billy", "Holiday", "@gloomybilly", cohort_24)

thom_yorke = Instructor("Thom", "Yorke", "@thomyorke", cohort_9, "Singing solemnly")
elizabeth_fraiser = Instructor("Elizabeth", "Frasier", "@pearlydewdropsdrop", cohort_38, "Yelling nonsense that is vaguely profound")
billy_corgan = Instructor("Billy", "Corgan", "@patrick", cohort_24, "Wailing")
bilinda_butcher = Instructor("Bilinda", "Butcher", "@bilindab", cohort_37, "A stare which reveals all")

bilinda_butcher.assign_exercise(kurt_cobain, perennial)
billy_corgan.assign_exercise(billy_holiday, nutshell)
elizabeth_fraiser.assign_exercise(kate_bush, student_exercises)
thom_yorke.assign_exercise(bjork_g, daily_journal)
