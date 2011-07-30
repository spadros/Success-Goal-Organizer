import os

def ReadAnything(x):
    filename = x + ".txt"
    f = open (filename, "r")
    f.flush
    x = f.read()
    if x.startswith("CalTrue") == True:
        x = str.splitlines(x)
        x.remove(x[0])
        f.close
        print "______________________________________"
        for item in range(len(x)):
            print x[item]
    else:
        x = str.splitlines(x)
        f.close
        print "Note reads:"
        print "______________________________________"
        for item in range(len(x)):
            print x[item]



def WriteAnything(x):
    filename = x + ".txt"
    description = []
    print "Note will end on last line that is empty (after the first two lines)."
    description.append(raw_input("First line (after this, enter for new line)\n"))
    description.append(raw_input())
    description.append(raw_input())
    if description[2] == '':
        f = open (filename, "w")
        f.flush()
        f.write(description[0])
        f.write("\n")
        f.write(description[1])
        f.close
    else:
        length = 2
        while description[length] !='' :
            length = len(description)
            description.append(raw_input())
        f = open (filename, "w")
        f.flush()
        f.write(description[0])
        for item in range(1, len(description)-1):
            f.write("\n")
            f.write(description[item])
        f.close
        
def ShowNotes():
    print "Current Notes"
    print 
    files = os.listdir(".")
    files.remove(files[0])
    length = len(files)-1
    for item in range (0, length):
        test = files[item]
        test = test.endswith(".txt")
        if test == True:
            print files[item]
    print "__________________________________"
    print
    print


def ShowReminders():
    f = os.listdir(".")
    for item in range (0, len(f)-1):
        if f[item].endswith(".txt"):
            filename = str(f[item])
            r = open(filename, "r")
            r = r.readline()
            if r.startswith("CalTrue") == True:
                r = r.split(" ")
                r.remove("CalTrue")
                print
                print"Note", item
                print 
                print f[item]
                print "At", r[0], r[1]
                print "On", r[2], r[3]

def NeedReminder(x):
    x = x + ".txt"
    q = raw_input("Should I add this to the calendar? y/n \n")
    if q == "y":
        w = open(x, 'r+')
        c = w.read()
        c = str.splitlines(c)
        hour = raw_input("At what hour?\n")
        minute = raw_input("At what minute?\n")
        month = raw_input("In what month?\n")
        day = raw_input("On what day?\n")
        change = str("CalTrue" + " " + hour + " " + minute + " " + month + " " + day)
        c.insert(0, change)
        k = open(x, "w")
        for item in range (0, len(c)):
            k.write(c[item])
            k.write("\n")
        k.close()

def WriteAnythingOLD(x):
        filename = x + ".txt"
        goals = [0, 0]
        goals [0] = raw_input("Title(s): \n")
        goals [1] = raw_input("Description(s):\n ")
        weekday = raw_input("What weekday?\n")
        informaltime = raw_input("Around when?\n")
        f = open (filename, "w")
        f.flush()
        f.write(weekday)
        f.write("\n")
        f.write(informaltime)
        f.write("\n")
        f.write(goals[0])
        f.write("\n")
        f.write(goals[1])

def LoadAnything():
    ncommand = raw_input("(r)ead or (w)rite or (w) for new or (sh)ow reminders or (c)ancel: ")
    if ncommand == "r" or ncommand == "w":
        x = raw_input("Note name?\n")
    if ncommand == "r":
        ReadAnything(x)
    if ncommand == "w":
        WriteAnything(x)
        NeedReminder(x)
    if ncommand == "c":
        return
    if ncommand == "sh":
        ShowReminders()

def NeedAlarm():
    print "Do you want this tracked by the alarm feature? \n"
    ycommand = raw_input("(Displayed at load)\n (y)es or (n)o")
    if ycommand == "y":
        return True
    if ycommand == "n":
        return False

# Alarmfeature()
# Display all notes feature
# Potential organizing by date

on = 1
while on != 0:
    print "GOAL MANAGER v1.01"
    print
    print
    ShowNotes()
    LoadAnything()
    
