print("welcome to computer quiz")
inhuman = input("are you interested in quiz? ")
if inhuman != "yes" :
    quit()
print ("lets play")
score = 0

answer = input("what is full form of cpu? ")
if answer.lower() == "central processing unit" :
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what is rsa ")
if answer.lower()== "algorithm":
    print("correct")
    score += 1
else:
    print("incorrect")
print("you have "+ str(score) +" got this many solutions correct")
print("thank you for attending my quiz")




