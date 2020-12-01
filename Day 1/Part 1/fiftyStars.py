with open('input.txt') as expense_report:
    contents = []
    max_value = 0
    ks = 0
    startingV = 0
    for val in expense_report.read().split():
        contents.append(int(val))

    for i in range(len(contents)):
        for v in range(len(contents)):
            if contents[startingV] + contents[v] == 2020:
                print(contents[startingV], contents[v])
                print("Multiplied =", contents[startingV] * contents[v])
        startingV += 1



expense_report.close()






