#!/bin/python


def check_num(n):
	if n == 0:
		return 'INSOMNIA'
	digit = [False for _ in range(10)]

	i = 1
	the_num = n
	while True:
		num = map(int, list(str(the_num)))

		for index in num:
			digit[index] = True
		if all(digit):
			break
		i += 1
		the_num = i *n
	return the_num




def main():
	T = int(raw_input().strip())
	N = []
	for _ in range(T):
		N.append(int(raw_input().strip()))

	for index in range(T):
		n = N[index]
		print 'Case #%s: %s' %(index+1, check_num(n))


if __name__ == '__main__':
	main()


