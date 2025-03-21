# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random, os
from pathlib import Path
# The quiz data. Keys are states and values are their capitals.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 
            'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

states = list(capitals.keys())

path = Path('./myFiles/randomQuizes/')
if not path.exists():
    os.makedirs(path)
    
for fileNumber in range(35):
    newQuizFile = open(mode='w', file=path / f'capitalsquiz{fileNumber+1}.txt')
    newQuizAnswersFile = open(mode='w', file=path / f'capitalsquiz_answers{fileNumber+1}.txt')
    header = 'Name:\n\nDate:\n\nPeriod:\n\n'+' '*20+f'State Capitals Quiz (Form {fileNumber+1})\n\n'
    newQuizFile.write(header)
    random.shuffle(states)
    for questionNumber in range(len(states)):
        question = f'{questionNumber+1}. What is the capital of {states[questionNumber]}?\n\n'
        correctAnswer = capitals[states[questionNumber]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        random.shuffle(wrongAnswers)
        wrongAnswers = wrongAnswers[:3]
        wrongAnswers.append(correctAnswer)
        answers = wrongAnswers
        random.shuffle(answers)
        responseBody = ''
        for i in range(len(answers)):
            responseBody += f'\t{'ABCD'[i]}. {answers[i]}\n\n'
        newQuizFile.write(question + responseBody)
        newQuizAnswersFile.write(f'{questionNumber+1}. {'ABCD'[answers.index(correctAnswer)]}\n\n')
    newQuizFile.close()
    newQuizAnswersFile.close()
    