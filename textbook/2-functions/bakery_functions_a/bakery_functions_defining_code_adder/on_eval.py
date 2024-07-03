from pedal import *
from pedal.cait import parse_program
#from pedal.cait import find_function_calls

if "_" in student.data:
    _ = student.data["_"]
    if isinstance(_, (int, float)):
        evaluation = parse_program(get_evaluation())
        if find_function_calls("print", evaluation):
            gently("You should not be calling the `print` function.")
        elif not find_function_calls("add_together", evaluation):
            gently("You must call the `add_together` function. Remember the parentheses and the arguments!")
        else:
            set_success()
    else:
        gently("The function's result should be a number!")