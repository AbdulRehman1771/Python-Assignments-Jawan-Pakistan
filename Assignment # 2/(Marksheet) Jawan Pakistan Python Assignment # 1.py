percentage = 100;
if percentage == 100:
    print("Brilliant! You have achieved a Historical Milestone.")
elif percentage < 100 and percentage > 79:
    print("Congratulations! You have got Grade A+.")
elif percentage < 80 and percentage > 69:
    print("Congratulations! You have got Grade A.")
elif percentage < 70 and percentage > 59:
    print("Great! You have got Grade B.")
elif percentage < 60 and percentage > 49:
    print("Good! You have got Grade C.")
elif percentage < 50 and percentage > 39:
    print("You have got Grade D.")
elif percentage < 40 and percentage > 32:
    print("Improve your studies, You have got Grade E.")
elif percentage < 33 and percentage > 0:
    print("Bad! You are Fail.")
elif percentage == 0:
    print("Fail!")
else:
    print("Please enter a correct percentage.")