#!/bin/python



def get_switch_num(engines, input_str):

    used_set = set()
    total = len(engines)
    total_sw = 0
    for each_input in input_str:

        if each_input not in  used_set:
            used_set.add(each_input)

        if len(used_set) == total:
            used_set = set([each_input])
            total_sw += 1

    return total_sw



def main():
    n = int(raw_input().strip())
    for i in range(n):

        tc_idx = i + 1
        engine_nums = int(raw_input().strip())

        engines = [raw_input().strip() for _ in range(engine_nums)]
        input_nums = int(raw_input().strip())

        input_str = [raw_input().strip() for _ in range(input_nums)]

        switch = get_switch_num(engines, input_str)
        print 'Case #{}: {}'.format(tc_idx, switch)


if __name__ == '__main__':
    main()
