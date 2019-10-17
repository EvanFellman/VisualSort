import random
import math
from time import sleep
import os

os.system('mode con: cols=128 lines=17')

speed = 0.05

def plot(array,f,l):
    out = ""
    sleep(speed)
    for i in range(20):
      out+="\n"
    #acc = [math.floor(math.sqrt(x) * max(array)) for x in array]
    acc = list(map((lambda x: (math.floor((x / max(array)) * 15)) + 1), array))
    for i in range(max(acc),0,-1):
        out += "\n"
        for x in range(len(acc)):
            if acc[x] >= i:
                if x >= f and x < l:
                    out += "▓"
                else:
                    out += "█"
            else:
                out += "░"
    print(out)
def oddEven(list):
    global speed
    speed = 0.075
    #plot(list)
    x,done = 0,False
    while not done:
        done = True
        x = (x + 1) % 2
        for i in range(x,len(list) - 1,2):
            plot(list,i,i+2)
            if list[i] > list[i + 1]:
                list[i] , list[i + 1] = list[i + 1] , list[i]
                done = False
    return list

def bubbleSort(list):
    global speed
    speed = 0.1
    flag = True
    while flag:
        flag = False
        for i in range(len(list) - 1):
            plot(list,i,i+2)
            if list[i] > list[i + 1]:
                list[i],list[i+1] = list[i+1],list[i]
                flag = True
    return list

def merge(left,right):
    global speed
    speed = 0.5
    out = []
    if len(left) == 0:
        out = right
    elif len(right) == 0:
        out = left
    else:
        if left[0] < right[0]:
            out = [left[0]] + merge(left[1::],right)
        else:
            out = [right[0]] + merge(left,right[1::])
   #plot(out)
    return out
hi = []
#printMe = []

def quickSort(list,uno,dos):
    global speed
    speed = 0.5
    global hi
    if len(list) <= 1:
        return list
    key = list[0]
    left = []
    right = []
    for i in list[1::]:
        if i <= key:
            left += [i]
        else:
            right += [i]
    hi = hi[:uno:] + left + [key] + right + hi[dos::]
    plot(hi,uno,dos)
    left = quickSort(left,uno + 1,uno + 1 +len(left))
    right = quickSort(right,uno + 1 + len(left),uno + 1 + len(left) + len(right))
    return left + [key] + right

def mergeSort(list,uno,dos):
    global hi
    #print(str(list))
    if len(list) < 2:
        return list
    elif len(list) == 2:
        if list[0] > list[1]:
            hi[uno:dos] = [list[1],list[0]]
            return [list[1], list[0]]
        else:
            return list
    else:
        left = mergeSort(list[:len(list) // 2:],uno,uno + (len(list) // 2))
        right = list[len(list) // 2::]
        hi = (hi[:uno:] + left + right + hi[dos::])
        plot(hi,uno,dos)
        right = mergeSort(list[len(list) // 2::],uno + (len(list) // 2),uno + len(list))
        hi = (hi[:uno:] + left + right + hi[dos::])
        plot(hi,uno,dos)
        #print("-" * 50)
        #print(left, right)
        return merge(left,right)

def findMin(list,uno):
    i = uno + 1
    min = list[uno]
    minIndex = uno
    while i < len(list):
        if list[i] < min:
            min = list[i]
            minIndex = i
        i = i + 1
    return [min,minIndex]

def selectionSort(uno):
    global hi
    global speed
    speed = 1
    if uno == len(hi) - 1:
        return hi
    min,minIndex = findMin(hi,uno)
    plot(hi,minIndex,minIndex+1)    
    hi = hi[:uno:] + [min] + hi[uno:minIndex:] + hi[minIndex + 1::]
    plot(hi,uno,uno+1)
    return selectionSort(uno + 1)
 
print("Pick a sorting system")
flag = True
hi = [random.randint(0,50) for x in range(0,128)]
while flag:
    inp = input("[oddeven, merge, bubble, selection]")
    inp = inp.lower()
    if inp == "quicksort":
        plot(hi, 0, -1)
        hi = quickSort(hi,0,len(hi))
        flag = False
    elif inp == "oddeven":
        plot(hi, 0, -1)
        hi = oddEven(hi)
        flag = False
    elif inp == "merge":
        plot(hi, 0, -1)
        hi = mergeSort(hi,0,len(hi))
        flag = False
    elif inp == "bubble":
        plot(hi,0,-1)
        hi = bubbleSort(hi)
        flag = False
    elif inp == "selection":
        plot(hi,0,-1)
        hi = selectionSort(0)
        flag = False


#hi = [1,2,3,4,5,7,0,0,0,0,0,0,0,00,0,0,0,0,00,0,0,0,0,00,0,0,0,0,0,1,2,3,3,4,9,6,8,9]
##plot(hi)
plot(hi,0,-1)
while True:
    pass