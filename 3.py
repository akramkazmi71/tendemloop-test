a = 6
series = 1
if a%2 == 0:
    a -= 1
for i in range(a):
    if i == a-1:
        print(series)
    else:
        print(series, ' , ', end="")
    series += 2
print('code ran successfully')