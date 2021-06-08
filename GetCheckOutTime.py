def get_checkout_time(customers, registers):
    tills = {}
    if registers == 1:
	    return sum(customers)
    if len(customers) <= registers:
    	return max(customers)
    for i in range(registers):
    	tills[i] = customers[i]
    for j in range(registers, len(customers)):
    	next_open = min(tills, key=tills.get)
    	tills[next_open] += customers[j]
    return max(tills.values())

print(get_checkout_time([5, 1, 3], 1))
print(get_checkout_time([10, 3, 4, 2],2))