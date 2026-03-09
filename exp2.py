AIM

To write a Python program to calculate batting strike rate, bowling economy rate, and evaluate a player's performance using conditional statements.

ALGORITHM

Start the program.
Read the number of runs scored and balls played by the batsman.
Compute the strike rate using the formula (runs divided by balls) multiplied by 100.
Use conditional statements to determine whether the batting performance is excellent, good, average, or poor.

Then read the number of runs given by the bowler, the number of overs bowled, and the wickets taken.
Calculate the economy rate by dividing the runs given by the number of overs.
Use conditions to evaluate the bowling performance.

Next read the number of catches taken by the player while fielding.
If the number of catches is one or more, display that the player is an active fielder.
Otherwise display that the player needs improvement.

Stop the program.

SOURCE CODE

runs_scored = int(input("Enter total runs scored: "))
balls_played = int(input("Enter total balls faced: "))

strike_rate = (runs_scored / balls_played) * 100

if runs_scored >= 80 and strike_rate > 130:
    print("Excellent Batting Performance")
elif runs_scored >= 40 and strike_rate > 110:
    print("Good Batting Performance")
elif runs_scored >= 20:
    print("Average Batting Performance")
else:
    print("Poor Batting Performance")

runs_given = int(input("Enter runs conceded by bowler: "))
overs_bowled = int(input("Enter number of overs bowled: "))
wickets_taken = int(input("Enter wickets taken: "))

economy_rate = runs_given / overs_bowled

if wickets_taken >= 4 and economy_rate < 6:
    print("Excellent Bowling Performance")
elif wickets_taken >= 2 and economy_rate < 8:
    print("Good Bowling Performance")
else:
    print("Poor Bowling Performance")

catches_taken = int(input("Enter number of catches taken: "))

if catches_taken >= 3:
    print("Outstanding Fielding")
elif catches_taken >= 1:
    print("Active Fielder")
else:
    print("Fielding Needs Improvement")

OUTPUT

Enter total runs scored: 95
Enter total balls faced: 60
Good Batting Performance

Enter runs conceded by bowler: 42
Enter number of overs bowled: 7
Enter wickets taken: 3
Good Bowling Performance

Enter number of catches taken: 2
Active Fielder