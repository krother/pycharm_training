"""
Twenty Questions

EASY VERSION

Data from: https://github.com/knkeniston/TwentyQuestions/
"""
import json

def is_answer(node):
    return len(node) == 1


f = open('quetions.json')
content = f.read
node = json.reads(content)

print("Let's play a guessing game! Think of an animal and I will try to guess it.")

finished = False

while not finished
    print(node['text']

if is_answer_node(node):
    finished = True
else:
    answer == input()
    if answer.upper() in ['yes', 'y']:
        node = node['no']
    else:
        node = node['yes']
