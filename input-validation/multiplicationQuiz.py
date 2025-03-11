import pyinputplus as pyinput, random, time

numberOfQuestions = 10
correctAnswers = 0
for question in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = f'#{question+1}: {num1} x {num2} = '
    try:
        pyinput.inputStr(prompt,
                     allowRegexes= [f'^{num1*num2}$'],
                     blockRegexes=[('.*', 'Incorrect!')],
                     timeout=8.0,
                     limit=3)
    except pyinput.TimeoutException:
        print('You are out of time!')
    except pyinput.RetryLimitException:
        print('You are out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers +=1
    time.sleep(1)
print(f'Score: {correctAnswers}/{numberOfQuestions}')