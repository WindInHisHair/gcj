#!/bin/python 

def get_min_flip(s):
	if len(s) == 0:
		return 1 if s == '-' else 0

	start = s[0]
	num = 0
	for each in s[1:]:
		if each == start:
			continue
		else:
			start = each
			num += 1

	num += 1 if s[-1] == '-' else 0
	return num


def main():
	T = int(raw_input().strip())

	pancakes = []
	for _ in range(T):
		pancakes.append(raw_input().strip())

	for index, each_cake in enumerate(pancakes):
		print 'Case #%d: %d' %(index+1, get_min_flip(each_cake))


if __name__ == '__main__':
	main()


