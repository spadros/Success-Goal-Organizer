def ReadAnything(x):
    filename = x + ".txt"
    f = open (filename, "r")
    f.flush
    x = f.read()
    x = str.splitlines(x)
    f.close
    print x

ReadAnything("Primonthly")
