# The first column is what your opponent is going to play: 
# A for Rock, B for Paper, and C for Scissors. The second column--

# The second column, you reason, must be what you should play in response: 
# X for Rock, Y for Paper, and Z for Scissors.

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
                    case "X": # Rock
                        score = draw + rock
                    case "Y": # Paper
                        score = win + paper
                    case "Z": # Scissors
                        score = lose + scissors
            case "B": # Paper
                match me:
                    case "X": # Rock
                        score = rock + lose
                    case "Y": # Paper
                        score = paper + draw
                    case "Z": # Scissors
                        score = scissors + win
            case "C": # Scissors
                match me:
                    case "X": # Rock
                        score = rock + win
                    case "Y": # Paper
                        score = paper + lose
                    case "Z": # Scissors
                        score = scissors + draw
        
        total = total + score
print(total)