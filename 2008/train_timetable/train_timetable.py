#!/bin/python
from datetime import datetime, timedelta


def _get_arr_and_dep(station_time):

    return [map(lambda x: datetime.strptime(x, '%H:%M'), raw_input().strip().split(' ')) for e in range(station_time)]


def calcuate_trains(_required, _ready):

    # # used = set()
    # start = len(_required)
    # for e_requ in _required:
    #     for e_ready in _ready:
    #         # if e_ready <= e_requ and e_ready not in used:
    #             # import ipdb; ipdb.set_trace()
    #             used.add(e_ready)
    #             start -= 1
    #             break
    start = len(_required)
    _ready.reverse()
    for each in _required:
        import ipdb;ipdb.set_trace()
        if each <= _ready[-1]:
            _ready.pop()
            start -= 1

    return start


def get_started_train(a_time, b_time, time_table):
    a_started, b_started = 0, 0

    get_requied = lambda x: [e[0] for e in x]
    get_ready = lambda x: [datetime.strptime(each, '%H:%M')
                           for each in [(e[1] + timedelta(minutes=time_table)).strftime('%H:%M') for e in x]]
    a_required, b_required = map(get_requied, [a_time, b_time])

    a_ready, b_ready = map(get_ready, [a_time, b_time])

    map(lambda x: x.sort(), [a_required, a_ready, b_ready, b_required])

    import ipdb;ipdb.set_trace()
    a_started, b_started = map(lambda x: calcuate_trains(*x), [[a_required, b_ready], [b_required, a_ready]])

    return a_started, b_started



def main():
    t = int(raw_input().strip())


    for i  in range(t):

        time_table = int(raw_input().strip())

        a, b = map(int, raw_input().strip().split())

        station_a_time, station_b_time = map(_get_arr_and_dep, [a, b])

        start_from_a, start_from_b = get_started_train(station_a_time, station_b_time, time_table)

        print 'Case #{}: {} {}'.format(i+1, start_from_a, start_from_b)



if __name__ == '__main__':
    main()