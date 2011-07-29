global goal
goal = [0, 0]

global command
command = 0
def ReadAnything(x):
    filename = x + ".txt"
    f = open (filename, "r")
    f.flush
    x = f.read()
    x = str.splitlines(x)
    f.close
    print "\n \n \n \n"
    print "Title: ", x[0]
    print "Description: ", x[1]

def WriteAnything(x, y):
    filename = x + ".txt"
    f = open (filename, "w")
    f.flush()
    f.write(y[0])
    f.write("\n")
    f.write(y[1])
    
def PrimaryMonthly():
    command = raw_input("Would you like to (r)ead or (w)rite: ")
    if command == "r":
        ReadAnything("PrimaryMonthly")
    if command == "w":
        goal = [0,0]
        goal [0] = raw_input("Goal title: ")
        goal [1] = raw_input("Goal description: ")
        WriteAnything("PrimaryMonthly", goal)

def SecondaryMonthly():
    command = raw_input("Would you like to (r)ead or (w)rite: ")
    if command == "r":
        ReadAnything("SecondaryMonthly")
    if command == "w":
        goal = [0, 0]
        goal [0] = raw_input("Goal title: ")
        goal [1] = raw_input("Goal description: ")
        WriteAnything("SecondaryMonthly", goal)

def TertiaryMonthly():
    command = raw_input("Would you like to (r)ead or (w)rite: ")
    if command == "r":
        ReadAnything("TertiaryMonthly")
    if command == "w":
        goal = [0, 0]
        goal [0] = raw_input("Goal title: ")
        goal [1] = raw_input("Goal description: ")
        WriteAnything("TertiaryMonthly", goal)


def PrimaryWeekly():
    command = raw_input("Would you like to (r)ead or (w)rite: ")
    if command == "r":
        ReadAnything("PrimaryWeekly")
    if command == "w":
        goal = [0, 0]
        goal [0] = raw_input("Goal title: ")
        goal [1] = raw_input("Goal description: ")
        WriteAnything("PrimaryWeekly", goal)

def SecondaryWeekly():
    command = raw_input("Would you like to (r)ead or (w)rite: ")
    if command == "r":
        ReadAnything("SecondaryWeekly")
    if command == "w":
        goal = [0, 0]
        goal [0] = raw_input("Goal title: ")
        goal [1] = raw_input("Goal description: ")
        WriteAnything("SecondaryWeekly", goal)

def TertiaryWeekly():
    command = raw_input("Would you like to (r)ead or (w)rite: ")
    if command == "r":
        ReadAnything("TertiaryWeekly")
    if command == "w":
        goal = [0, 0]
        goal [0] = raw_input("Goal title: ")
        goal [1] = raw_input("Goal description: ")
        WriteAnything("TertiaryWeekly", goal)

def PrimaryDaily():
    command = raw_input("Would you like to (r)ead or (w)rite: ")
    if command == "r":
        ReadAnything("PrimaryDaily")
    if command == "w":
        goal = [0, 0]
        goal [0] = raw_input("Goal title: ")
        goal [1] = raw_input("Goal description: ")
        WriteAnything("PrimaryDaily", goal)

def SecondaryDaily():
    command = raw_input("Would you like to (r)ead or (w)rite: ")
    if command == "r":
        ReadAnything("SecondaryDaily")
    if command == "w":
        goal = [0, 0]
        goal [0] = raw_input("Goal title: ")
        goal [1] = raw_input("Goal description: ")
        WriteAnything("SecondaryDaily", goal)

def TertiaryDaily():
    command = raw_input("Would you like to (r)ead or (w)rite: ")
    if command == "r":
        ReadAnything("TertiaryDaily")
    if command == "w":
        goal = [0, 0]
        goal [0] = raw_input("Goal title: ")
        goal [1] = raw_input("Goal description: ")
        WriteAnything("TertiaryDaily", goal)

def command(x):
    if x == "PrimaryMonthly":
        PrimaryMonthly()
        return
    if x == "SecondaryMonthly":
        SecondaryMonthly()
        return
    if x == "TertiaryMonthly":
        TertiaryMonthly()
        return
    if x == "PrimaryWeekly":
        PrimaryWeekly()
        return
    if x == "SecondaryWeekly":
        SecondaryWeekly()
        return
    if x == "TertiaryWeekly":
        TeritaryWeekly()
        return
    if x == "PrimaryDaily":
        PrimaryDaily()
        return
    if x == "SecondaryDaily":
        SecondaryDaily()
        return
    if x == "TertiaryDaily":
        PrimaryDaily()
        return
    if x == "quit":
        on = 0



on = 1
while on != 0:
    print "\n\n\n\nCatagory goal followed with no spaces by timeframe. \n I.E. PrimaryMonthly or TertiaryDaily \n Caps are important"
    y = raw_input("Command: ")
    command(y)
