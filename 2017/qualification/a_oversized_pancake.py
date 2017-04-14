#!/bin/python 


def oversized_flipper(pancake):
	c, k = pancake
	k = int(k)
	if len(c) == k:
		if all([each == '+' for each in c]) or all([each == '-' for each in c]):
			return 1 if all([each == '-' for each in c]) else 0
		else:
			return 'IMPOSSIBLE'

	cake = list(c)
	res , i = 0, 0
	while True:
		if k == len(cake[i:]):
			if all([each == '+' for each in cake[i:]]):
				return res
			elif all([each == '-' for each in cake[i:]]):
				return res +1
			else:
				return 'IMPOSSIBLE'
		elif k > len(cake[i:]):
			return res if all([e == '+' for e in cake[i:]]) else 'IMPOSSIBLE'

		if cake[i] == '+':
			i += 1
			continue

		for e in range(i, i+k):
			cake[e] = '+' if cake[e] == '-' else '-'
		res += 1
		i += 1



def main():
	T = int(raw_input().strip())

	pancakes = [raw_input().strip().split() for _ in range(T)]

	for i, v in enumerate(pancakes):

		print 'Case #%s: %s' %(i+1, oversized_flipper(v))


if __name__ == '__main__':
	main()