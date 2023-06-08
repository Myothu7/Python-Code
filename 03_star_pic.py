k = 2
for a in range(0, 6, 2):
    for b in range(0, k):
        print(end=" ")
    k = k - 1
    for c in range(a + 1):
        print('*', end="")
    print()

	
