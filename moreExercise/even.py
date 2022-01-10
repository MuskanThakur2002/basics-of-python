# i=int(input("enter a number"))
# n=1
# count1=3
# count=3
# while i>=n:
#     if i%2==0 and count>0:
#         print("even", i)
#         count-=1
#     if i%2!=0 and count1>0:
#         print("odd", i)
#         count1+=1
#     i=i-1

i=int(input("enter a number"))
n=1
count=3
while i>=n:
    if i%2==0 and count>0:
        print("even", i)
        count-=1
    i=i-1

i=int(input("enter a number"))
n=1
count1=3
while i>=n:
    if i%2!=0 and count1>0:
        print("odd", i)
        count1-=1
    i=i-1