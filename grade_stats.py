grades =input("please enter the grades here: ")


def print_grades(grades):
    a = []
    for grade in grades:
        if grade != ",":
            grade = int(grade)
            a.append(grade)
    return a
a = (print_grades(grades))
print(a)

def grades_sum(a):
    total = 0
    for grade in a:
        total += int(grade)
    return total

def do_something(q1):
    if q1 == "average":
        print (grades_average(a))
        keep_going(str(input("Can I help you with anything else?")))
    elif q1 == "variance":
        print (grades_variance(a))
        keep_going(str(input("Can I help you with anything else?")))
    elif q1 == "standard deviation":
        print (grades_std_deviation(variance))
        keep_going(str(input("Can I help you with anything else?")))
    else:
        print("Sorry, I don't know how to find the "+ str(q1)+". ")

def grades_average(a):
    sum_of_grades = grades_sum(a)
    average = sum_of_grades / float(len(a))
    return average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average-score)**2
        x = variance / len(scores)
    return x

variance = grades_variance(a)


def grades_std_deviation(x):
    return x ** 0.5



def keep_going(x):
    if x == "yes":
        do_something(str(input("what do you want to do with the grades? ")))
    if x == "no":
        print('Thank you for your time with me!')
    else:
        print ("Please enter yes or no.")
        return keep_going(str(input("Can I help you with anything else?")))


do_something(str(input("what do you want to do with the grades? ")))
