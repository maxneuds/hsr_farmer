class PathBug(Exception): pass

def exit():
    raise PathBug

def loop():
    try:
        print(1)
        exit()
        print(2)
    except PathBug:
        print(3)

loop()