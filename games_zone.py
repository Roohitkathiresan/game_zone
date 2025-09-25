import csv

class gameCounter:
    def __init__(self,filename):
        self.filename=filename

    def newregis(self):
        while True:
            stopregis=input('are you the last person to register today (yes/no):')
            if stopregis=='no':
                newname = input('enter your name: ')
                newtype = input('enter your user type (student/faculty/guests): ')

                with open(self.filename,'a', newline="") as file:
                    writer=csv.writer(file)
                    new_entry=[newname,newtype,0]
                    writer.writerow(new_entry)
                print("registration successful!")
            else:
                break


class gameMachine:
    def __init__(self,filename):
        self.filename=filename

    def playgame(self):
        while True:
            stopgame=input('are you the last person to play games today (yes/no): ')
            if stopgame=='no':
                increname=input('enter your name: ')
                incretype=input('enter your user type (student/faculty/guests): ')
                rows = []

                with open(self.filename,'r',newline="") as file:
                    reader=csv.reader(file)
                    for i in reader:
                        if i and i[0]==increname:
                            if i[1]=='student' and int(i[2])<15:
                                i[2] = str(int(i[2])+1)
                            elif i[1]=='faculty' and int(i[2])<10:
                                i[2] = str(int(i[2])+1)
                            elif i[1] =='guests' and int(i[2])<5:
                                i[2] = str(int(i[2])+1)
                            else:
                                print('you have reached your limit , please come tomorrow')
                        rows.append(i)

                with open(self.filename, 'w', newline="") as file:
                    writer=csv.writer(file)
                    writer.writerows(rows)

                print('You can play your game now!')
            else:
                break

    def checkstatus(self):
        while True:
            stopcheck=input('are you the last person to check your status today (yes/no): ')
            if stopcheck=='no':
                name=input('Enter your name: ')

                with open(self.filename, 'r', newline="") as file:
                    reader=csv.reader(file)
                    for i in reader:
                        if i and i[0]==name:
                            if i[1]=='student' and int(i[2])<15:
                                print(15-int(i[2]), 'more games to play')
                            elif i[1]=='faculty' and int(i[2])<10:
                                print(10-int(i[2]), 'more games to play')
                            elif i[1] =='guests' and int(i[2])<5:
                                print(5-int(i[2]), 'more game to play')
                            else:
                                print("No more games left for you.")
                                break
                    else:
                        print('Your name is not registered, please register in our game system.')

filename='gamedata.csv'
counter=gameCounter(filename)
machine=gameMachine(filename)

regis=input("have you registered in the system (yes/no): ")
if regis=='yes':
    menu=int(input('enter 1 to play the game, enter 2 to check your status: '))
    if menu==1:
        machine.playgame()
    else:
        machine.checkstatus()
else:
    counter.newregis()