import random
l=["r","p","s"]
us=0
cs=0
d={'r':'rock','p':'paper','s':'scissor'}
while True:
	#TAKE INPUT FROM USER
	u=input("enter your choice,press n to discontinue")
	#to exit()
	if u=='n':
		print("game over")
		print("user score:",us)
		print("computer score:",cs)
		if us>cs:
			print("user wins")
		elif cs>us:
			print("computer wins")
		else:
			print("it is tie")
		exit()
	#input from computer
	c=random.choice(l)
	print("computer chooses", c)
    #compare the user and computer choice
	if u==c:
		print("tie")
	elif u=="r" and c=="p":
		cs=cs+1
		print("comp wins",cs)
	elif u=="r" and c=="s":
		us=us+1
		print("user wins",us)
	elif u=="s" and c=="r":
		cs=cs+1
		print("comp wins",cs)
	elif u=="s" and c=="p":
		us=us+1
		print("user wins",us)
	elif u=="p" and c=="s":
		cs=cs+1
		print("comp wins",cs)
	elif u=="p" and c=="r":
		us=us+1
		print("user wins",us)