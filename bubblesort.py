import time

running = False
varx = 0
vary = 0

def changeRun(run):
    global running
    running = run


def bubble_sort(data, drawData, timeTick):
    for i in range(len(data)):
        for j in range(len(data)-i):
            drawData(data, ['yellow' if x == j or x == j +
                     1 else 'red' for x in range(len(data))])
            time.sleep(timeTick)
            a = data[j]
            if a != data[-1]:
                b = data[j+1]
                if(a > b):
                    data[j], data[j+1] = b, a
                    drawData(data, ['green' if x == j or x ==
                             j+1 else 'red' for x in range(len(data))])
                    time.sleep(timeTick)


def bubble_sort_step(data, drawData):
    global running,varx,vary
    if(running):
        for i in range(len(data)):
            print("1st for")
            print(varx)
            print(i)
            for j in range(varx,len(data) - i):
                if(running):
                    print("2nd for,j=",j)
                    drawData(data, ['yellow' if x == j or x ==
                                j+1 else 'red' for x in range(len(data))])
                    time.sleep(2)
                    a = data[j]
                    if a != data[-1]:
                        b = data[j+1]
                        print("before comp")
                        if(a > b):
                            print("afttr comp")
                            data[j], data[j+1] = b, a
                            drawData(
                                data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])    
                            running = False
                    if j>=len(data)-1: varx = 0
        varx+=1    