def calculateLocation(latitude, longitude):

    def getLatitudeDirection(latitude):
        if latitude > 0:
            return "south"
        else:
            return "north"

    def getLongitudeDirection(longitude):
        if longitude > 0:
            return "east"
        elif longitude == 0:
            return "prime meridian"
        else:
            return "west"

    latitude_direction = getLatitudeDirection(latitude)
    longitude_direction = getLongitudeDirection(longitude)

    output_text = latitude_direction + "/" + longitude_direction
    return output_text

try:
    user_input = input("Enter latitude: ")

    latitude_str, longitude_str = user_input.split(",")
    latitude = float(latitude_str.strip())
    longitude = float(longitude_str.strip())

    calculateLocation(latitude, longitude)
except ValueError:
    print("Invalid input.")

# calculateLocation(latitude, longitude)
print(calculateLocation(latitude, longitude))