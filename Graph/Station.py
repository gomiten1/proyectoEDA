class Station:
    to = 0
    cost = 0
    nxt = None
    scooters = []
    name = ""
    ubicacion = ""

    #BFS
    prev = None
    #color: 0-blank, 1-gray, 2-black
    color = 0
    distance = -1

