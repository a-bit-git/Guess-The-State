States = ['Andhra-Pradesh','Arunachal-Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana',
        'Himachal-Pradesh','Jammu-Kashmir','Jharkhand','Karnataka','Kerala','Madhya-Pradesh',
        'Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim',
        'Tamil-Nadu','Telangana','Tripura','Uttar-Pradesh','Uttarakhand','West-Bengal']

Capitals = ['Amaravati','Itanagar','Dispur','Patna','Raipur','Panaji','Gandhinagar','Chandigarh',
            'Shimla','Srinagar','Ranchi','Bengaluru','Thiruvananthapuram','Bhopal','Mumbai','Imphal',
            'Shillong','Aizawl','Kohima','Bhubaneswar','Chandigarh','Jaipur','Gangtok','Chennai',
            'Hyderabad','Agartala','Lucknow','Dehradun','Kolkata']

Rank = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

print("""   >>>  GUESS THE STATE  <<<

      >>> GAME RULES <<<

(a) First letter must be capital
(b) Use hyphen in case where it is""")

import random
def state_to_capital(): 
    l=1
    while (len(Rank)!=0):
        c=random.choice(Rank)
        S=States[c]
        C=Capitals[c]
        print("______________________________________________________________________")
        print()
        print("........ Level :",l,"........")
        print()
        print("State-Name      <=>      Capital-Name")
        print()
        for i in range(0,len(S)):
            if(S[i]!="-"):
                print("_",end=" ")
            else:
                print("-",end=" ")
        print("  <=>  ",C)
        print()
        User=input("Enter the state name : ")
        print()
        if (User==S):
            print("Correct !!!")
            print("Points :",l*10)
            l+=1
        else:
            print("Fail !!!")
            print(f'"{C}" is the Capital of "{S}"')
            print("Points :",(l*10)-10)
            print()
            break
        Rank.remove(c)
    else:
        print("Congratulations, YOU WON THE GAME !!!")
    print("Your Total Score :", (l*10)-10)
state_to_capital()