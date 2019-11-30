"""
ID: riyatha1
LANG: PYTHON3
TASK: milk
"""
fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')
(total, farmers) = fin.readline().split(" ")
total = int(total)
data = []
answer = 0
for i in fin:
	(x, y) = i.split(" ")
	temp_data = (int(x), int(y))
	data.append(temp_data)
	temp_data = ()
data.sort()
#print(data)
for i in data:
	price = i[0]
	amount = i[1]
	if amount < total:
		answer += amount * price
		total -= amount
	else:
		answer += price * total
		total = 0
		break
fout.write (str(answer) + '\n')
fout.close()
