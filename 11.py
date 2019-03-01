import random
l=["r","p","s"]
d={'r':'rock','p':'paper','s':'scissor'}
us=0
cs=0
while True:
	#TAKE INPUT FROM USER
	u=input("enter your choice,press n to discontinue")
	if u in d:
		print("user chooses ",d[u])
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
	if c in d:
		print("computer chooses", d[c])
    #compare the user and computer choice
	if u==c:
		print("tie")
	elif u=="r" and c=="p":
		cs=cs+1
		print("comp wins",cs)
	elif u=="s" and c=="r":
		cs=cs+1
		print("comp wins",cs)
	elif u=="p" and c=="s":
		cs=cs+1
		print("comp wins",cs)
	else:
		us=us+1
		print("user wins",us)
	