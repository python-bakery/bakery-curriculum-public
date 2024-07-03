"""
Fall 2022 Canvas final project
UD CS1 Bakery
"""
from bakery_canvas import get_courses, get_submissions, Submission
from bakery import assert_equal
from datetime import datetime
import matplotlib.pyplot as plt

####################################################################################
# Part 1 Functions

def count_courses(user_token: str) -> int:
    """ Count the number of courses for this user """
    courses = get_courses(user_token)
    count = 0
    for course in courses:
        count += 1
    return count

def find_cs1(user_token: str) -> int:
    """ Find the first course with CISC in their code """
    courses = get_courses(user_token)
    for course in courses:
        if "CISC1" in course.code:
            return course.id
    return 0

def find_course(user_token: str, course_id: int) -> str:
    """ Retrieves the name of the course with the given ID """
    courses = get_courses(user_token)
    for course in courses:
        if course.id == course_id:
            return course.name
    return "no course found"

def render_courses(user_token: str) -> str:
    """ Join user's courses together into a single multi-line string """
    courses = get_courses(user_token)
    result = ""
    for course in courses:
        result += str(course.id) + ": " + course.code + "\n"
    return result

####################################################################################
# Part 2 Functions

def total_points(user_token: str, course_id: int) -> int:
    """ Get all of the points possible for the assignments in the course """
    submissions = get_submissions(user_token, course_id)
    total = 0
    for submission in submissions:
        total = total + submission.assignment.points_possible
    return total

assert_equal(total_points('annie', 679554), 420)
assert_equal(total_points('annie', 386814), 700)
assert_equal(total_points('annie', 100167), 1060)
assert_equal(total_points('jeff', 679554), 420)
assert_equal(total_points('jeff', 386814), 700)
assert_equal(total_points('troy', 394382), 100)

def count_comments(user_token: str, course_id: int) -> int:
    """ Count the number of comments in all the submissions for the course """
    submissions = get_submissions(user_token, course_id)
    total = 0
    for submission in submissions:
        for comment in submission.comments:
            total = total + 1
    return total

assert_equal(count_comments('annie', 679554), 14)
assert_equal(count_comments('annie', 386814), 1)
assert_equal(count_comments('annie', 4182), 9)
assert_equal(count_comments('annie', 394382), 0)
assert_equal(count_comments('jeff', 394382), 0)
assert_equal(count_comments('jeff', 100167), 30)
assert_equal(count_comments('jeff', 134088), 14)
assert_equal(count_comments('troy', 394382), 0)

def ratio_graded(user_token: str, course_id: int) -> str:
    """ Get the number of graded and total assignments in a course, as a string """
    submissions = get_submissions(user_token, course_id)
    graded = 0
    total = 0
    for submission in submissions:
        if submission.grade:
            graded += 1
        total += 1
    return str(graded) + "/" + str(total)


assert_equal(ratio_graded('annie', 679554), '10/10')
assert_equal(ratio_graded('annie', 386814), '7/7')
assert_equal(ratio_graded('annie', 100167), '52/56')
assert_equal(ratio_graded('annie', 134088), '6/11')
assert_equal(ratio_graded('jeff', 394382), '1/1')
assert_equal(ratio_graded('jeff', 100167), '52/56')

def average_score(user_token: str, course_id: int) -> float:
    """ Calculate the average score of the assignments in the course. """
    submissions = get_submissions(user_token, course_id)
    score = 0.0
    points = 0.0
    for submission in submissions:
        if submission.grade:
            score += submission.score
            points += submission.assignment.points_possible
    if not points:
        return 0.0
    return score / points

assert_equal(average_score('annie', 679554), 0.95)
assert_equal(average_score('annie', 386814), 0.97)
assert_equal(average_score('annie', 394382), 1.0)
assert_equal(average_score('jeff', 386814), 0.7)
assert_equal(average_score('jeff', 394382), 0.7)
assert_equal(average_score('troy', 394382), 0.8)

def average_weighted(user_token: str, course_id: int) -> float:
    """ Calculate the average weighted score of the assignments in the course. """
    submissions = get_submissions(user_token, course_id)
    score = 0.0
    points = 0.0
    for submission in submissions:
        if submission.grade:
            weight = submission.assignment.group.weight
            score += submission.score * weight
            points += submission.assignment.points_possible * weight
    if not points:
        return 0.0
    return score / points

assert_equal(average_weighted('annie', 679554), 0.9471)
assert_equal(average_weighted('annie', 386814), 0.97)
assert_equal(average_weighted('jeff', 4182), 0.7343)

def average_group(user_token: str, course_id: int, group_name: str) -> float:
    """ Calculate the average score of the assignments in the group. """
    submissions = get_submissions(user_token, course_id)
    score = 0.0
    points = 0.0
    for submission in submissions:
        if submission.grade and submission.assignment.group.name.lower() == group_name.lower():
            score += submission.score
            points += submission.assignment.points_possible
    if not points:
        return 0.0
    return score / points

assert_equal(average_group('annie', 679554, 'exam'), 0.935)
assert_equal(average_group('annie', 679554, 'project'), 0.0)
assert_equal(average_group('annie', 4182, 'exam'), 1.03)
assert_equal(average_group('annie', 134088, 'homework'), 0.938)

def find_assignment(submissions: list[Submission], assignment_id: int) -> Submission:
    """ Find a given submission using its assignment ID """
    for submission in submissions:
        if submission.assignment.id == assignment_id:
            return submission
    return None

def render_assignment(user_token: str, course_id: int, assignment_id: int) -> str:
    """ Finds the given assignment in the list and returns it as a string. """
    submissions = get_submissions(user_token, course_id)
    submission = find_assignment(submissions, assignment_id)
    if not submission:
        return "Assignment not found: " + str(assignment_id)
    if submission.grade:
        grade = "Grade: "+str(submission.score) + "/" + str(submission.assignment.points_possible) + " ("+submission.grade+")"
    else:
        grade = "Grade: (missing)"
    return (str(submission.assignment.id)+": " + submission.assignment.name +"\n"+
            "Group: " + submission.assignment.group.name + "\n" +
            "Module: " + submission.assignment.module + "\n" +
            grade)


assert_equal(render_assignment('annie', 679554, 7), 'Assignment not found: 7')
assert_equal(render_assignment('annie', 679554, 299650), '299650: Introduction\nGroup: Homework\nModule: Module 1\nGrade: 10.0/10 (A)')
assert_equal(render_assignment('annie', 679554, 553716), '553716: Basic Addition\nGroup: Homework\nModule: Module 2\nGrade: 14.0/15 (A)')
assert_equal(render_assignment('annie', 679554, 805499), '805499: Basic Subtraction\nGroup: Homework\nModule: Module 2\nGrade: 19.0/20 (A)')
assert_equal(render_assignment('annie', 134088, 937202), '937202: Technology in the outdoor classroom\nGroup: Homework\nModule: Module 2\nGrade: (missing)')
assert_equal(render_assignment('jeff', 386814, 24048), '24048: HOMEWORK 3\nGroup: Assignments\nModule: MODULE 1\nGrade: 58.0/100 (F)')

def render_all(user_token: str, course_id: int) -> str:
    """ Returns all the assignments in the course as one string. """
    submissions = get_submissions(user_token, course_id)
    result = ""
    for submission in submissions:
        result += str(submission.assignment.id) + ": " + submission.assignment.name
        if submission.grade:
            result += " (graded)\n"
        else:
            result += " (ungraded)\n"
    return result

assert_equal(render_all('annie', 679554), '299650: Introduction (graded)\n553716: Basic Addition (graded)'
                                          '\n805499: Basic Subtraction (graded)\n749969: Basic Multiplication'
                                          ' (graded)\n763866: Basic Division (graded)\n979025: Midterm 1 '
                                          '(graded)\n870878: Logarithms (graded)\n126393: Antiderivatives '
                                          '(graded)\n122494: Actual Sorcery (graded)\n683132: Final Exam (graded)\n')
assert_equal(render_all('annie', 386814), '806809: HOMEWORK 1 (graded)\n212220: HOMEWORK 2 (graded)\n24048: '
                                          'HOMEWORK 3 (graded)\n982248: HOMEWORK 4 (graded)\n269027: HOMEWORK '
                                          '5 - COPY 1 (graded)\n476501: HOMEWORK 7 (graded)\n654144: HOMEWORK 8'
                                          ' FINAL (graded)\n')
assert_equal(render_all('troy', 394382), '711675: Practical (graded)\n')



####################################################################################
# Part 3 Functions

def plot_scores(user_token: str, course_id: int):
    """ Plots the distribution of fractional scores in the course """
    submissions = get_submissions(user_token, course_id)
    peak = sum_points_weighted(user_token, course_id)
    if not peak:
        return
    points = []
    for sub in submissions:
        if sub.grade and sub.assignment.points_possible:
            points.append(sub.score / sub.assignment.points_possible * 100)
    #plt.hist(points)
    #plt.title(f"Distribution of Scores ({user_token}, {course_id})")
    #plt.xlabel("Score")
    #plt.ylabel("Number of Assignments")
    #plt.show()
    return [points]


def days_apart(first_date: str, second_date: str) -> int:
    """ Determines the days between `first` and `second` date. """
    first_date = datetime.strptime(first_date, "%Y-%m-%dT%H:%M:%S%z")
    second_date = datetime.strptime(second_date, "%Y-%m-%dT%H:%M:%S%z")
    difference = second_date - first_date
    return difference.days


def plot_earliness(user_token: str, course_id: int):
    """ Plots the distribution of earliness of assignments """
    submissions = get_submissions(user_token, course_id)
    dates = []
    for sub in submissions:
        if sub.submitted_at and sub.assignment.due_at:
            dates.append(days_apart(sub.submitted_at, sub.assignment.due_at))
    #plt.title(f"Distribution of Days Submitted Early ({user_token}, {course_id})")
    #plt.xlabel("Earliness (days)")
    #plt.ylabel("Number of Submissions")
    #plt.hist(dates)
    #plt.show()
    return [dates]

def plot_points(user_token: str, course_id: int):
    """ Plots the relationship between points possible and the weighted points possible """
    submissions = get_submissions(user_token, course_id)
    peak = sum_points_weighted(user_token, course_id)
    if not peak:
        return
    points = []
    weighted = []
    for sub in submissions:
        points.append(sub.assignment.points_possible)
        weighted.append(sub.assignment.points_possible * sub.assignment.group.weight / peak)
    #plt.scatter(points, weighted, alpha=.2)
    #plt.title(f"Relationship of Points Possible with Weighted ({user_token}, {course_id})")
    #plt.xlabel("Points Possible")
    #plt.ylabel("Weighted Points Possible")
    #plt.show()
    return [[points, weighted]]


import matplotlib.pyplot as plt
from bakery_canvas import get_submissions

def sum_points_weighted(user_token: str, course_id: int) -> int:
    " Add up the weighted points possible for all assignments"
    submissions = get_submissions(user_token, course_id)
    total = 0
    for sub in submissions:
        total += sub.assignment.points_possible * sub.assignment.group.weight / 100
    return total


def predict_grades(user_token: str, course_id: int):
    """
    Create three running sum graphs that show the maximum weighted points possible,
    the maximum possible weighted score that can still be earned, and the minimum
    possible weighted score that can still be earned.
    """
    submissions = get_submissions(user_token, course_id)
    highs = []
    lows = []
    points = []
    running_score_low = 0
    running_score_high = 0
    running_points = 0
    peak = sum_points_weighted(user_token, course_id)
    if not peak:
        return
    for sub in submissions:
        if sub.grade:
            running_score_low += sub.score * sub.assignment.group.weight
            running_score_high += sub.score * sub.assignment.group.weight
        else:
            running_score_high += sub.assignment.points_possible * sub.assignment.group.weight
        running_points += sub.assignment.points_possible * sub.assignment.group.weight
        points.append(running_points / peak)
        highs.append(running_score_high / peak)
        lows.append(running_score_low / peak)
    #plt.plot(points, label="Maximum")
    #plt.plot(highs, label="Highs")
    #plt.plot(lows, label="Lows")
    #plt.xlabel("Assignments")
    #plt.ylabel("Grade")
    #plt.title(f"Points over Time ({user_token}, {course_id})")
    #plt.legend()
    #plt.show()
    return [points, highs, lows]

####################################################################################
# Main Functions

HELP_TEXT = """
exit > Exit the application
help > List all the commands
course > Change current course
points > Print total points in course
comments > Print how many comments in course
graded > Print ratio of ungraded/graded assignments
score_unweighted > Print average unweighted score
score > Print average weighted score
group > Print average of assignment group, by name
assignment > Print the details of a specific assignment, by ID
list > List all the assignments in the course
scores > Plot the distribution of grades in the course
earliness > Plot the distribution of the days assignments were submitted early
compare > Plot the relationship between assignments' points possible and their weighted points possible
predict > Plot the trends in grades over assignments, showing max ever possible, max still possible, and minimum still possible
"""
def execute(command: str, user_token: str, course_id: int) -> int:
    """ Execute the given command, returning a new course ID """
    if command == "course":
        print(render_courses(user_token))
        target_id = int(input("What course do you want to print?"))
        print("Changed to", find_course(user_token, target_id))
        return target_id
    elif command == "exit":
        return 0
    elif command == "help":
        print(HELP_TEXT)
    elif command == "points":
        print(total_points(user_token, course_id))
    elif command == "comments":
        print(count_comments(user_token, course_id))
    elif command == "graded":
        print(ratio_graded(user_token, course_id))
    elif command == "score_unweighted":
        print(average_score(user_token, course_id))
    elif command == "score":
        print(average_weighted(user_token, course_id))
    elif command == "group":
        group_name = input("What group should I analyze?")
        print(average_group(user_token, course_id, group_name))
    elif command == "assignment":
        assignment_id = input("What assignment ID do you want to look at?")
        print(render_assignment(user_token, course_id, assignment_id))
    elif command == "list":
        print(render_all(user_token, course_id))
    elif command == "scores":
        plot_scores(user_token, course_id)
    elif command == "earliness":
        plot_earliness(user_token, course_id)
    elif command == "compare":
        plot_points(user_token, course_id)
    elif command == "predict":
        predict_grades(user_token, course_id)
    return course_id

def main(user_token: str):
    """ Repeatedly get user input and execute the command """
    courses = get_courses(user_token)
    if not courses:
        return
    course_id = find_cs1(user_token)
    if not course_id:
        course_id = courses[0].id
    while course_id > 0:
        command = input("What do you want to do? (type `help` to list commands)")
        course_id = execute(command, user_token, course_id)

#if __name__ == '__main__':
#    main('annie')