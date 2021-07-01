import time

running = False


def changeRun_inserion(run):
    global running
    running = run



def insertion_sort(s,drawData, timeTick):
    for i in range(0,len(s)-1):
        drawData(s, ['yellow' if x == i  else 'red' for x in range(len(s))])
        time.sleep(timeTick)
        if s[i]>s[i+1]:
            s[i],s[i+1]=s[i+1],s[i]
            drawData(s, ['blue' if x == i or x ==
                             i+1 else 'red' for x in range(len(s))])
            time.sleep(timeTick)
            for j in range(i,0,-1):
                if s[j]<s[j-1]:
                    s[j],s[j-1]=s[j-1],s[j]
                    drawData(s, ['green' if x == j-1 else 'red' for x in range(len(s))])
                    time.sleep(timeTick)


# Step by step for insertion_sort
def insertion_sort_step(s,drawData):
    global running
    print(running)
    if(running):
        print("step called")
        print(running)
        for i in range(0,len(s)-1):
            drawData(s, ['yellow' if x == i else 'red' for x in range(len(s))])
            time.sleep(2)
            if(running):
                print("step2 called")
                if s[i]>s[i+1]:
                    s[i],s[i+1]=s[i+1],s[i]
                    drawData(s, ['blue' if x == i or x == i+1 else 'red' for x in range(len(s))])
                    time.sleep(2)
                    if(running):
                        print("step3 called")
                        for j in range(i,0,-1):
                            if s[j]<s[j-1]:
                                s[j],s[j-1]=s[j-1],s[j]
                                drawData(s, ['green' if x == j-1 else 'red' for x in range(len(s))])
                                time.sleep(2)
                                running = False