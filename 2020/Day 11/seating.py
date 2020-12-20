
with open("input.txt") as file:
    data = file.readlines()
    data = [list(line.strip()) for line in data]

def get_num_occupants():
    count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "#":
                count += 1
        return count


def get_adjectent_count(row, col):
    count = 0
    currentRow = data[row]

    # check left
    if currentRow[col -1] == "#":
        count += 1

    # check right
    if col + 1 <= len(currentRow):
        if currentRow[col+1] == "#":
            count += 1

    # above
    if row-1 >= 0:
        aboveRow = data[row-1]
        if aboveRow[col] == "#":
            count += 1

        if col-1 >= 0:
            if aboveRow[col-1] == "#":
                count += 1

        if col+1 <= len(aboveRow):
            if aboveRow[col+1] == "#":
                count += 1

    # below
    if row+1 >= 0:
        belowRow = data[row+1]
        if belowRow[col] == "#":
            count += 1

        if col-1 >= 0:
            if belowRow[col-1] == "#":
                count += 1

        if col+1 <= len(belowRow):
            if belowRow[col+1] == "#":
                count += 1
    return count

def run_rules():
    newSeating = []

    for row in range(len(data)):
        currentRow = data[row]
        newRow = []

        for col in range(len(currentRow)):
            if currentRow[col] == ".":
                newRow.append(".")
                continue

            adjectentcount = get_adjectent_count(row, col)

            if currentRow[col] == "L" and adjectentcount == 0:
                newRow.append("#")

            elif currentRow[col] == "#" and adjectentcount >= 4:
                newRow.append("L")

            else:
                newRow.append(currentRow[col])
        newSeating.append(newRow)

    for i in range(len(data)):
        data[i] = newSeating[i]

def get_final_count():
    prev = data.copy()

    run_rules()

    while data != prev:
        prev = data.copy()
        run_rules()

    return get_num_occupants()

print(get_final_count())