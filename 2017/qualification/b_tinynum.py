#!/bin/python 

def get_tiny_num(n):
	num = map(int, list(str(n)))

	for i in range(0, len(num)):
		

		if num[i] < num[i-1]:
			num[i-1] -= 1
			num[i] = 9


def main():
	t = int(raw_input().strip())
	n = [int(raw_input().strip()) for _ in range(t)]

	for i , v in enumerate(n):
		print 'Case #%d: %d' %(i+1, get_tiny_num(v))

if __name__ == '__main__':
	main()