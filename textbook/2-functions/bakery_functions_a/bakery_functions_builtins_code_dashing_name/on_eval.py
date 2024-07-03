from pedal import *

if "_" in student.data:
    _ = student.data["_"]
    if isinstance(_, str):
        evaluation = parse_program(get_evaluation())
        if "01 All The Single Ladies.mp3" in get_evaluation():
            gently("You should be writing an expression using the method and the variable.",
                   label="embedded_answer_eval")
        elif len(evaluation.find_all("Call")) == 1:
            if _ == "01 All The Single Ladies.mp3":
                set_success()
            else:
                gently("That is not the right value.", label="wrong_result_value")
        else:
            gently("You should have only one function call.", label="multiple_calls")
    elif _ == None:
        gently("It looks like you may have printed instead of entering "
               "the variable directly. No need to print - we're accessing the "
               "value directly!", label="printing_in_eval")
    else:
        gently("That is not the right value; it should produce a string!",
               label="wrong_result_type")