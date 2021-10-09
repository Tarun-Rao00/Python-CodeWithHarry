import random

randNo = random.randint(0,1000)

def game():
    return randNo

score = game()
with open('HiScore.txt', 'r') as f:
    hiscorestr = f.read()
    

if hiscorestr=='':
    with open('HiScore.txt', 'w') as f:
        f.write(str(score))
    print('NEW HIGH SCORE!!!')
elif score>int(hiscorestr):
    with open('HiScore.txt', 'w') as f:
        f.write(str(score))
    print('NEW HIGH SCORE!!!')


print(f'Your Score is {score}')





