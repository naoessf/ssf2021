from GPS import parsing

i = 0
while True:
    position = parsing()
    if position is None:
        pass
    elif position[0] == "$GNRMC":
        i += 1
        if position[4] == "V":
            print("Parsing Failed")
            print("Parsing Number({})".format(i))
        elif position[4] == "A":
            print("latitude : {}\tlongitude : {}\tship direction : {}".format(position[1], position[2], position[3]))
            print("Parsing Number({})".format(i))

# position[1] : latitude
# position[2] : longitude
# position[3] : ship direction
# position[4] : A : act, V : not act
