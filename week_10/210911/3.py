def calc_time(in_time, out_time):
    in_time, out_time = in_time.split(':'), out_time.split(':')
    i_time, o_time = int(in_time[0]) * 60 + int(in_time[1]), int(out_time[0]) * 60 + int(out_time[1])
    return o_time - i_time

def solution(fees, records):
    cars = dict()
    # 자동차들 기록
    for record in records:
        time, car, state = record.split()
        if state == 'IN':
            if cars.get(car, 0):
                cars[car][0] = time
            else:
                cars[car] = [time, 0]
        else:
            cars[car][1] += calc_time(cars[car][0], time)
            cars[car][0] = ''
    # 금액 기록
    answer = []
    import math
    for car in sorted(cars.keys(), key= lambda x: int(x)):
        time, fee = cars[car]
        if time:
            fee += calc_time(time, '23:59')
        base_fee, var_fee, div_fee, mul_fee = fees[1], fee - fees[0], fees[2], fees[3]
        if var_fee < 0:
            var_fee = 0
        final_fee = base_fee + math.ceil((var_fee) / div_fee) * mul_fee
        answer.append(final_fee)
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", \
            "06:00 0000 IN", \
            "06:34 0000 OUT", \
            "07:59 5961 OUT",\
            "07:59 0148 IN", \
            "18:59 0000 IN", \
            "19:09 0148 OUT", \
            "22:59 5961 IN", \
            "23:00 5961 OUT"]
print(solution(fees, records))

