def Latitude(n):
    #List Latitude
    i = 0
    latitude = [0]
    for i in range(1, n+1):
        #Get Latitude of Destination
        lat = float(input("Latitude of Destination ({}) : ".format(i)))
        latitude.append(lat)
    return latitude

def Longitude(n):
    #List Longitude
    j = 0
    longitude = [0]
    for j in range(1, n+1):
        #Get Longitude of Destination
        long = float(input("Longitude of Destination ({}) : ".format(j)))
        longitude.append(long)
    return longitude