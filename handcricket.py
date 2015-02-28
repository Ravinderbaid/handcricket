import random

typ = [0,1,2,3,4,5,6,7,8,9,10]
rans = -1
bats = 0
flags = 1
print 'Toss'
bat1 = 0
toss = int(raw_input('1->Odd 2->Even?'))
score = random.choice(typ)+int(raw_input('Enter the toss score(0-10)'))
if(score % 2 == 0):
	flags = 2
if(flags == toss):
	bat1 = int(raw_input('1->Batting 2->Bowling'))
if(bat1 == 1):
	print "Its your turn to bat buddy"
	score = 0
	while(bats!=rans):
		bats = int(raw_input('Enter the run'))
		if(bats>10):
			print "Enter run less than 10"
		else:
			rans = random.choice(typ)
			print rans
			if (bats == rans):
				print "Out!!"
				print "Its your turn to bowl now"
				print "Your score is ",score
			else:
				score = score + bats
	total=0
	while(total<=score):
		bats = int(raw_input('Enter the run'))
		rans = random.choice(typ)
		print rans
		if (bats == rans):
			print "Out!!"
			print "You won by ",(score-total)
			print "Your score is ",total
			exit()
		else:
			total = total + rans
	else:
		print "You lost"
else:
	print "Its your turn to bowl!!"
	score = 0
	while(bats!=rans):
		bats = int(raw_input('Enter the run'))
		rans = random.choice(typ)
		print rans
		if (bats == rans):
			print "Out!!"
			print "Its your turn to bat now"
			print "Your score is ",score
		else:
			score = score + rans
	total=0
	while(total<=score):
		bats = int(raw_input('Enter the run'))
		if(bats>10):
			print "Enter run less than 10"
		else:
			rans = random.choice(typ)
			print rans
			if (bats == rans):
				print "Out!!"
				print "You lost by ",(score-total)
				print "Your score is ",total
				exit()
			else:
				total = total + bats
	else:
		print"You won"
