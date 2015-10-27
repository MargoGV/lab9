x0 = 4
x1 = 4.25
for i in range(2, 31):
	x = 108-(815-1500/x0)/x1
	x0 = x1
	x1 = x
print(x)
