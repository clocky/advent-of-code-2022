# The first column is what your opponent is going to play: 
# A for Rock, B for Paper, and C for Scissors. The second column--

# Anyway, the second column says how the round needs to end: 
# X means you need to lose, 
# Y means you need to end the round in a draw, and 
# Z means you need to win. 
# Good luck!

rock: int = 1
paper: int = 2
scissors: int = 3

lose: int = 0
draw: int = 3
win: int = 6

with open("day2.txt", "r") as f:
    total: int = 0 
    for game in f.read().splitlines():
        score: int = 0
        plays = game.split()
        me = plays[1]
        opponent = plays[0]

        match opponent:
            case "A": # Rock
                match me:
                    case "X": # Lose
                        score = lose + scissors
                    case "Y": # Draw
                        score = draw + rock
                    case "Z": # Win
                        score = win + paper
            case "B": # Paper
                match me:
                    case "X": # Lose
                        score = lose + rock
                    case "Y": # Draw
                        score = draw + paper
                    case "Z": # Win
                        score = win + scissors
            case "C": # Scissors
                match me:
                    case "X": # Lose
                        score = lose + paper
                    case "Y": # Draw
                        score = draw + scissors
                    case "Z": # Win
                        score = win + rock
        
        total = total + score
print(total)