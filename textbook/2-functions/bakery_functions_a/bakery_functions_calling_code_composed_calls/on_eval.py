from pedal.cait import parse_program

if "_" in student.data:
    _ = student.data["_"]
    if isinstance(_, str):
        if '"' in get_evaluation() or "'" in get_evaluation():
            gently("You are correctly using a string value literal. But you need to call your functions to convert them!")
        else:
            gently("That is not the right value!")
    elif _ == None:
        gently("It looks like you may have printed. No need to print here in the Evaluations/Shell/Console!")
    elif isinstance(_, (int, float)):
        evaluation = parse_program(get_evaluation())
        if not evaluation.find_all("Str"):
            gently("You should have a string value as the argument.")
        elif evaluation.find_all("Num"):
            gently("You shouldn't have any numbers in your evaluation.")
        elif len(evaluation.find_all("Call")) == 2:
            set_success()
        else:
            gently("You should have only two function calls.")
    else:
        gently("That is not the right value!")