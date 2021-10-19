n = int(input())
count = 1
per = 0
now = 1
fibo = now
while count < n:
	fibo = per + now
	per = now
	now = fibo
	count += 1
print(fibo)