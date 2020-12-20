with open("input.txt") as file:
    data = file.readline()
    data = [line.strip() for line in file]


def find_path():
    yAxis = 0
    xAxis = 0
    heading = "E"
    rotation = 90

    for line in data:

        action = line[:1]
        value = int(line[1:])

        if action == "N":
            yAxis += value
            continue

        if action == "S":
            yAxis -= value
            continue

        if action == "W":
            xAxis -= value
            continue

        if action == "E":
            xAxis += value
            continue

        if action == "R" or action == "L":
            heading, rotation = find_angle(heading, action, value, rotation)

        if action == "F":
            if heading == "N":
                yAxis += value

            if heading == "S":
                yAxis -= value

            if heading == "W":
                xAxis -= value

            if heading == "E":
                xAxis += value

    return xAxis, yAxis
    #return abs(xAxis) + abs(yAxis)


def find_angle(heading, action, value, rotation):
    if action == "R":
        if rotation <= 360:
            rotation += value
            if rotation < 90:
                heading = "N"
            elif rotation < 180:
                heading = "E"
            elif rotation < 225:
                heading = "S"
            elif rotation < 360:
                heading = "W"
        else:
            rotation = 0
            rotation += value
            if rotation < 90:
                heading = "N"
            elif rotation < 180:
                heading = "E"
            elif rotation < 225:
                heading = "S"
            elif rotation < 360:
                heading = "W"

    if action == "L":
        if rotation >= -360:
            rotation += value
            if abs(rotation) < 90:
                heading = "N"
            elif abs(rotation) < 180:
                heading = "E"
            elif abs(rotation) < 225:
                heading = "S"
            elif abs(rotation) < 360:
                heading = "W"
        else:
            rotation = 0
            rotation += value
            if abs(rotation) < 90:
                heading = "N"
            elif abs(rotation) < 180:
                heading = "E"
            elif abs(rotation) < 225:
                heading = "S"
            elif abs(rotation) < 360:
                heading = "W"

    return heading, rotation


path = find_path()
print(path)


