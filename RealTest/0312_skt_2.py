import math


def Numbering(square, Runner, number):
    # print("현재 위치  y:", Runner["y"], 'x:', Runner["x"])
    # print("추가할 숫자", number)
    square[Runner["y"]][Runner["x"]] = number


def Move(Runner, square, clockwise):
    states = {0: "RIGHT", 1: "DOWN", 2: "LEFT", 3: "UP"}
    if(states[Runner["state"]] == "RIGHT"):
        if(square[Runner["y"]][Runner["x"]+1] > 0):
            # print("곂치니까 시계방향으로 돌리자", "현재 상태", Runner["state"])
            Runner["state"] = (Runner["state"] + 1*clockwise) % 4
            Runner["y"] = Runner["y"]+1*clockwise
        else:
            Runner["x"] = Runner["x"]+1
    elif(states[Runner["state"]] == "DOWN"):
        if(square[Runner["y"]+1][Runner["x"]] > 0):
            # print("곂치니까 시계방향으로 돌리자", "현재 상태", Runner["state"])
            Runner["state"] = (Runner["state"] + 1*clockwise) % 4
            Runner["x"] = Runner["x"]-1*clockwise
        else:
            Runner["y"] = Runner["y"]+1
    elif(states[Runner["state"]] == "LEFT"):
        if(square[Runner["y"]][Runner["x"]-1] > 0):
            # print("곂치니까 시계방향으로 돌리자", "현재 상태", Runner["state"])
            Runner["state"] = (Runner["state"] + 1*clockwise) % 4
            Runner["y"] = Runner["y"]-1*clockwise
        else:
            Runner["x"] = Runner["x"]-1
    elif(states[Runner["state"]] == "UP"):
        if(square[Runner["y"]-1][Runner["x"]] > 0):
            # print("곂치니까 시계방향으로 돌리자", "현재 상태", Runner["state"])
            Runner["state"] = (Runner["state"] + 1*clockwise) % 4
            Runner["x"] = Runner["x"]+1*clockwise
        else:
            Runner["y"] = Runner["y"]-1


def solution(n, clockwise):
    # n*n 매트릭스를 0으로 채운다.
    square = [[0 for i in range(n)] for i in range(n)]
    number = 1
    goalNumber = math.ceil(n*n/4)
    # Runner 위치, 상태
    Runners = [
        {"x": 0, "y": 0, "state": 0 if clockwise else 1},
        {"x": n-1, "y": 0, "state": 1 if clockwise else 2},
        {"x": n - 1, "y": n-1, "state": 2 if clockwise else 3},
        {"x": 0, "y": n-1, "state": 3 if clockwise else 0}
    ]
    clockwise = 1 if clockwise else -1

    # print(Runners)
    while True:
        Numbering(square, Runners[0], number)
        Move(Runners[0], square, clockwise)
        Numbering(square, Runners[1], number)
        Move(Runners[1], square, clockwise)
        Numbering(square, Runners[2], number)
        Move(Runners[2], square, clockwise)
        Numbering(square, Runners[3], number)
        Move(Runners[3], square, clockwise)
        if(number == goalNumber):
            break
        else:
            number = number+1

    return square


ans = solution(5, False)

for x in ans:
    print(x)
