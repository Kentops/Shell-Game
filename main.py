'''
1/31/2024
A game where you bet money on a cup and ball trick
'''
import check_input
import random

def main():
  keepGoing = True
  money = 100

  
  print("Find the ball to double your bet!")
  while money > 0 and keepGoing == True:
    #Game loop
    print("You have $" + str(money) + ".")
    bet = check_input.get_int_range("Bet amount? ",1,money)
    print("  ___     ___     ___")
    print(" /   \\   /   \\   /   \\")
    print("/  1  \\ /  2  \\ /  3  \\")
    print("------- ------- -------")

    guess = check_input.get_int_range("Where is the ball? ",1,3)
    ballLocation = random.randint(1,3)

    #Printing the ball location
    if(ballLocation == 1):
      print("  ___     ___     ___")
      print(" /   \\   /   \\   /   \\")
      print("/  o  \\ /     \\ /     \\")
      print("------- ------- -------")
    elif(ballLocation==2):
      print("  ___     ___     ___")
      print(" /   \\   /   \\   /   \\")
      print("/     \\ /  o  \\ /     \\")
      print("------- ------- -------")
    else:
      print("  ___     ___     ___")
      print(" /   \\   /   \\   /   \\")
      print("/     \\ /     \\ /  o  \\")
      print("------- ------- -------")

    #Calculate result
    if ballLocation == guess:
      print("Congratulations!")
      money += bet 
    else:
      money -= bet
      print("Sorry... You Lose.")
      if(money <= 0):
        print("You're out of money! Game Over!")
        return
    
         
    #Ask the player if they wish to continue
    keepGoing = check_input.get_yes_no("Play again? (Y/N) ")


main()