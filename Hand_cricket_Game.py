import random


class Cricket:
    def __init__(self,usr):
        self.user = usr
        self.score = 0
        if count==1:
            print(f'\n{scneed+1} to win\n')
        if self.user == 'Computer':
            print('Computer:Select Bat')
            print('You:Select Ball')
        else:
            print('You:Select Bat')
            print('Computer:Select Ball')

        while True :
            if self.user == 'Computer':
                self.run  = random.randint(1,6)
                r = int(input())
            else:
                self.run = int(input())
                r = random.randint(1,6)
            if self.run not in [1,2,3,4,5,6]:
                print('Select from 1 to 6')
            if self.run == r:
                print(f'{self.user}:Out! Final score is {self.score}\n')
                break
            else:
                self.score +=self.run
                if scneed ==0 and count==0 :
                    print(f'{self.user}:score is {self.score}')
                else:
                    var = (scneed+1)-self.score
                    if(var > 0):
                        print(f'{self.user}:score is {self.score}\t\t\t{var} is needed')
                    else:
                        print(f'{self.user}:score is {self.score}')
                        break

print(f'\n\n{'*'*20}Welcome to Hand Cricket Game{'*'*20}')
print('Rule:')
print('''1.Toss\nStart with a toss to decide who bats first. The winner of the toss gets to choose whether tobat or bowl.''')
print('2.Batting\nThe batsman uses their finger as run from 1 to 6')
print('3.Bowler\nThe bowler uses their finger as bowling from 1 to 6')
print('4.Score\nWe are summing the run of the batsman')
print('5.Wicket/Out\nBowler finger and batsman finger are same then it is out')







print(f"\n\n{'*'*20}Toss Time{'*'*20}")
print("\nSelecting 'Head' write 'H'\nSelecting 'Tail' write 'T'")
toss  = input('You:Enter the choice:')
tossed = random.choice('HT')
select = random.choice(['Bat','Ball'])
count = 0
if toss.upper() == tossed :
    print('\nYou:win the toss\n')
    choice = input("You:select 'Bat' or 'Ball':")
    if choice.lower() == 'bat':
        scneed = 0
        y = Cricket('You')
        scneed = y.score
        count +=1
        c = Cricket('Computer')
        if y.score > c.score:
            print('You:Congratulation!,You Win the match\n')
        elif y.score < c.score:
            print('Computer:Win the match')
            print('You:Loss the match\n')
        else:
            print(f'{"*"*10}Match Draw{"*"*10}\n')
        print('\nComputer:Play again')
    elif choice.lower() == 'ball':
        scneed = 0
        c = Cricket('Computer')
        scneed = c.score
        count +=1
        y = Cricket('You')
        if y.score > c.score:
            print('You:Congratulation!,You Win the match\n')
        elif y.score < c.score:
            print('Computer:Win the match')
            print('You:Loss the match\n')
        else:
            print(f'{"*"*10}Match Draw{"*"*10}\n')
        print('\nComputer:Play again')
    else:
        print("Select coorect option 'Bat' or 'Ball")

else:
    print('\nComputer:Win the toss\n')
    
    if select == 'Bat' :
        scneed = 0
        c = Cricket('Computer')
        scneed = c.score
        count +=1
        y = Cricket('You')
        if y.score > c.score:
            print('You:Congratulation!,You Win the match\n')
        elif y.score < c.score:
            print('Computer:Win the match')
            print('You:Loss the match\n')
        else:
            print(f'{"*"*10}Match Draw{"*"*10}\n')
        print('\nComputer:Play again')
    else:
        scneed = 0
        y = Cricket('You')
        scneed = y.score
        count +=1
        c = Cricket('Computer')
        if y.score > c.score:
            print('You:Congratulation!,You Win the match\n')
        elif y.score < c.score:
            print('Computer:Win the match')
            print('You:Loss the match\n')
        else:
            print(f'{"*"*10}Match Draw{"*"*10}\n')
        print('\nComputer:Play again')


