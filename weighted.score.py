grade = int(input("Input the score you got from the assignment "))
outof = int(input("Input the total grade out of the assignment "))
weight = int(input("Input the weighing of the assignment as a whole number (20% would be 20) "))

ans = (((grade / outof) * 100) * (weight / 100)) # An automatic calculation of the grade, by dividing the output, and multiplying by its weight.
print(ans,"%") # No rounding to show an accurate score for the user. User can choose if they want to round it themselves.
