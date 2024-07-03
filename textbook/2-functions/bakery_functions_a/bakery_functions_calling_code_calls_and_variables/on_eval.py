from pedal.cait import parse_program

if "_" in student.data:
    _ = student.data["_"]
    if isinstance(_, str):
        if '"' in get_evaluation() or "'" in get_evaluation():
            gently("You should not be using a string value literal. Use the variable that you created before!")
        else:
            gently("That is not the right value!")
    elif _ == None:
        gently("It looks like you may have printed instead of entering the variable directly. No need to print - we're accessing the value directly!")
    elif _ == 10:
        if parse_program(get_evaluation()).body[0].value.ast_name == "Name":
            set_success()
        else:
            gently("You are not entering a variable.")
    else:
        gently("That is not the right value!")