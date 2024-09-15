name = input ("type your name : ")
print("welcome",name,"to this adventure!")

answer = input("you are on a dirt road, it has come to an end and you can go  ? ")

if answer == "left":
    answer= input("you came to a river, you walk around it or swin accross ? Type walk to walk around and swim to swim accross : ")

    if answer == "swim":
        print("you swim accross and were eaten by an alligator.")
    
    elif answer == "walk":
        print("you walked for for many miles, ran out of water any you lost the game.")
    else:
        print('not a vaild option. You lose.')

elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back) ?")
    
    if answer == "back":
        print("you go back and lose.")
    
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. Do you talk to them (yes/no) ? ")

        if answer == "yes":
            print("you talk to the stranger and they give you gold.")

        elif answer == "no":
            print("you ingore the stranger and they are offended and you lose.")
        
        else:
            print('not a vaild option. you lose.')
    else:
        print('not a vaild option. You lose.')

else:
    print('Not a vaild option. You lose.')


print("Thank you for typing", name)