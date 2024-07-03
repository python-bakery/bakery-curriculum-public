from bakery import assert_equal
from bakery_canvas import get_submissions, Submission



assert_equal(render_assignment('annie', 679554, 7), 'Assignment not found: 7')
assert_equal(render_assignment('annie', 679554, 299650), '299650: Introduction\nGroup: Homework\nModule: Module 1\nGrade: 10.0/10 (A)')
assert_equal(render_assignment('annie', 679554, 553716), '553716: Basic Addition\nGroup: Homework\nModule: Module 2\nGrade: 14.0/15 (A)')
assert_equal(render_assignment('annie', 679554, 805499), '805499: Basic Subtraction\nGroup: Homework\nModule: Module 2\nGrade: 19.0/20 (A)')
assert_equal(render_assignment('annie', 134088, 937202), '937202: Technology in the outdoor classroom\nGroup: Homework\nModule: Module 2\nGrade: (missing)')
assert_equal(render_assignment('jeff', 386814, 24048), '24048: HOMEWORK 3\nGroup: Assignments\nModule: MODULE 1\nGrade: 58.0/100 (F)')