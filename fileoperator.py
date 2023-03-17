import time , gc

filename = "trades.txt"
n = 20 # Number of lines to be deleted
i = 0
while True:
    with open(filename, "r") as file:
        lines = file.readlines()
        print(lines)

    if len(lines) > 20:
        print('cleared')
        with open(filename, "w") as file:
            file.writelines(lines[n:])

    i = i +1
    if i % 100 == 0:
        gc.collect()

    time.sleep(5)