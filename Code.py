# Question 1
x = input("Enter Two Numbers: ").split()
print(int(x[0])**int(x[1]))

# Question 2
y = input("Enter the List of Numbers: ").split()
newlist = [z for z in y if int(z)%3 == 0]
print(newlist)
