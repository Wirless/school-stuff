ourarray = []
def arr14():
	for number in range(5):
		number = int(input("Please enter a number"))
		ourarray.append(number)
	print(ourarray)


my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]

def average(mlist):
	x = 0
	calculate = len(mlist)
	for number in mlist:
		x += number
	print(x/calculate)
	
#average(my_list)

def print_rect(height):
	for num in range(height):
		print("*"*10)

#print_rect(5)

def print_rect2(height, width):
	for num in range(height):
		print("*"*width)

#print_rect2(8,3)

def print_rect3(height, width, symbol):
	for num in range(height):
		print(f"{symbol}"*width)
		
#print_rect3(8,3,'#')

def print_rect4(printwhat):
		printwhat
	
#print_rect4(print_rect3(8,3,'#'))


def num_box():
	for i in range(10):
		for j in range(10):
			print(j, end=' ')
		print()

#num_box()


def num_box2():
	for i in range(10):
		for j in range(10):
			print(i, end=' ')
		print()
#num_box2()

