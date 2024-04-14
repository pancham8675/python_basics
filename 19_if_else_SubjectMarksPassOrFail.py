#Find if the student is pass

sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("Sorry, you are fail because you have scored less than 33 marksin one of the subjects.")
elif(((sub1+sub2+sub3)/3)<40):
    print("Sorry, you failed because your total percentage is less than 40%")
else:
    print("Congratulations! You are pass with",((sub1+sub2+sub3)/3),"%")

