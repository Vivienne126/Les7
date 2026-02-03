import random

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
chosen=random.choice(numbers)

user=int(input("GUESS THE NUMBER...(1-16)"))

if user==chosen:
    print("WOW... Great work... Right guess")
elif user>chosen:
    print("Close but wrong , a lower")
else:
    print("Close but wrong , a higher")
    print
print(chosen)

