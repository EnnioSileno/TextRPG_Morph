class Player:
    pass

class Map:
    pass

Commands = {
    "help": print_help,
    "quit": quit_game,
    "pickup": pickup,
    "forward": forward,
    "backward": backward,
    "right": right,
    "left": left,
    "fight": fight,
    "save": save,
    "load": load,
    "rest": rest,
    "run": run_away,
    }


def print_help(p, m):
    print(Commands.keys())



if __name__ == "__main__":
    p = Player(name)
    map = Map()
    print("Type 'help' to list all available commands!\n")
    while True:
        command = input("> ").lower.split(" ")
        if command[0] in Commands:
            Commands[command[0]](p, map)
        else:
            print("You run around in circles and don't know what to do.")