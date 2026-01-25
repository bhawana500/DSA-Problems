def tower_of_hanoi(n, a, b, c):
    if n == 0:
        return
    tower_of_hanoi(n-1, a, c, b)
    print("move ", n, "disk from", a , "to", c)
    tower_of_hanoi(n-1, b, a, c)
    
tower_of_hanoi(3, "a", "b", "c")