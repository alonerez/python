while True:
	pl1 = input("please choose : Rock-Paper-Scissors ").lower()
	pl2 = input("please choose : Rock-Paper-Scissors ").lower()

	if pl1 not in ["rock", "paper", "scissors"] or pl2 not in ["rock", "paper", "scissors"] :
		print ("input error, please choose 'rock' ,'paper' or 'scissors'")
		exit()
	if pl1 == pl2:
		print ("No winner, try again")
	elif ((pl1 == "rock" and pl2 == "scissors") or (pl1 == "paper" and pl2 == "rock") or (pl1 == "scissors" and pl2 == "paper")):
	# elif pl1 == "rock" and pl2 == "scissors":
		print ("Player 1  wins")
	elif ((pl2 == "rock" and pl1 == "scissors") or (pl2 == "paper" and pl1 == "rock") or (pl2 == "scissors" and pl1 == "paper")):
	# elif pl2 == "rock" and pl1 == "scissors":
		print ("Player 2  wins")
		
	ans = input ("Do you want to play again ? (yes/no) ")
	if ans != "yes":
		break	
