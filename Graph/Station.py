class Station:
    to = 0
    cost = 0
    nxt = None
    
    #lo que nosotros agregamos realmente, el resto se queda igual
    scooters = []
    name = ""
    location = ""

    #BFS
    prev = None
    #color: 0-blank, 1-gray, 2-black
    color = 0
    distance = -1

