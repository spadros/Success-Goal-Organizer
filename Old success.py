def NewPriMonthly():
    PriMonthly = [raw_input("Primary Monthly Task title: "), raw_input("Primary Monthly Task Description: ")]
    f = open ("Prdimonthly.txt", "w")
    f.flush()
    f.write(PriMonthly[0])
    f.write("\n")
    f.write(PriMonthly[1])
    f.close

def ReadPriMonthly():
    f = open ("Primonthly.txt", "r")
    f.flush
    PriTitle = f.read()
    PriTitle = str.splitlines(PriTitle)
    f.close
    print "Your Primary Goal for this month is: "
    print PriTitle [0]
    print "Your action plan to do it is:"
    print PriTitle [1]

def NewSecMonthly():
    SecMonthly = [raw_input("Secondary Monthly Task title: "), raw_input("Secondary Monthly Task Description: ")]
    f = open ("Secmonthly.txt", "w")
    f.flush()
    f.write(SecMonthly[0])
    f.write("\n")
    f.write(SecMonthly[1])
    f.close

def ReadSecMonthly():
    f = open ("Secmonthly.txt", "r")
    f.flush
    SecMonthly = f.read()
    SecMonthly = str.splitlines(SecMonthly)
    f.close
    print "Your Secondary Goal for this month is: "
    print SecMonthly [0]
    print "Your action plan to do it is:"
    print SecMonthly [1]

def NewTertMonthly():
    TertMonthly = [raw_input("Tertiary Monthly Task title: "), raw_input("Tertiary Monthly Task Description: ")]
    f = open ("Tertmonthly.txt", "w")
    f.flush()
    f.write(TertMonthly[0])
    f.write("\n")
    f.write(TertMonthly[1])
    f.close

def NewPriWeekly():
    PriWeekly = [raw_input("Primary Weekly Task title: "), raw_input("Primary Weekly Task Description: ")]
    f = open ("Priweekly.txt", "w")
    f.flush()
    f.write(PriWeekly[0])
    f.write("\n")
    f.write(PriWeekly[1])
    f.close

while True:
    command = raw_input("What would you like to do? ")
    if command == "npm":
        NewPriMonthly()
    if command == "rpm":
        ReadPriMonthly()

