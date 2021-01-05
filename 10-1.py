class Player:
    teamcolor = ""
    points = ""

def main():
    color = "Blue"
    points = 300
    player = Player()
    player.teamcolor = color
    player.points = points
    print("The ", color, " contender has ", points, " points!")

main()