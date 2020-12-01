with open('input.txt') as expense_report:
    contents = []
    max_value = 0
    ks = 0
    startingV = 0
    for val in expense_report.read().split():
        contents.append(int(val))

    while startingV <= len(contents):
        for i in range(len(contents)):
            for v in range(len(contents)):
                if 2020 - contents[startingV] == contents[v] + contents[i]:
                    print(contents[startingV] * contents[v] * contents[i])
                    break
        startingV += 1



expense_report.close()






