
total = int(input("Enter the no. of bananas: "))
distance = int(input("Enter the distance you want to cover: "))
load_capacity = int(input("Enter the max Load capacity of your camel: "))
lose=0
start = total
for i in range(distance):
    while start>0:
        start = start-load_capacity
        
        if start==1:
            lose = lose-1
        lose = lose+2
    lose = lose - 1
    start=total-lose
    if start==0:
      break
print(start)
