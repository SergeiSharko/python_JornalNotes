count = 0

def counter():
    global count
    count += 1
    return count

def resetCounter():
    global count
    count = 0
    return count