Courses = ["Python","Java","c++","maths","anglais","Javascript"]
print("AU's Grading System")
course = input("Name of Course?")
if(course in Courses):
    print("you registered for this course.")  
    name = input("What is your name?")

    print("Hii " + name)     
    score = int(input("What is your test score?"))
    if(score<=40):
        print("Your grade is D")
    elif(score>40 and score<=55):
            print("Your grade is C")
    elif(score>55 and score<=70):
        print("Your grade is B")
    elif(score>70 and score<=100):
        print("Your grade is A")
else:
    print("You did not register for this course.")

    



