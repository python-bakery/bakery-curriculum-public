
if "_" in student.data:
    _ = student.data["_"]
    if _ == 5:
        if '+' in get_evaluation():
            guidance("Good! Notice how the expression evaluated and then printed the result below the box?"
                     " That's not like the code we had in the editor, which didn't seem to do anything, "
                     "right? Well, in both cases, the expression WAS evaluated. In the editor, the result was"
                     " thrown away, but in the Evaluate box it was printed out instead!"
                     " Now, let's try running the `print(4+5)` line in the Evaluate box.",
                    label="step_2_completed", title="Step 2 Completed")
        else:
            gently("It seems like you might not be doing the actual math operation `2+3` in the Evaluate box. "
                   "Do not just use `5`, have Python do the math for you!", label="missing_math", title="Missing Math")
    elif _ == None:
        ensure_function_call('print')
        if student.raw_output:
            if student.raw_output.strip()[-1] == '9':
                set_success(message="Great! Hopefully you saw how the word `None` also appeared? That's why we shouldn't `print` "
                            "in the Evaluate console. Just rememnber, if you want text to appear from the editor, you need to "
                           "print at the end of your program. But if you want text to appear from the Evalaute area, then you "
                           "should NOT use `print`. We'll learn more about that weird `None` later.")
            else:
                gently("You should be printing the result of `4+5`. Just copy and paste the second line of the program we gave you!")
        else:
            gently("You need to use the `print` function to print something!")
    else:
        guidance("Notice how only one value was actually printed on the console? Now click the [Evaluate] button. Inside the box, enter the expression `2+3` and then press Enter.",
                 title="Part 2")
else:
    guidance("Notice how only one value was actually printed on the console? Now click the [Evaluate] button. Inside the box, enter the expression `2+3` and then press Enter.",
         title="Part 2")