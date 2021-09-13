def time_to_int(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

def int_to_time(time):
    h = time // 3600
    m = time % 3600 // 60
    s = time % 3600 % 60
    h, m, s = map(lambda x: x.zfill(2), map(str, [h, m, s]))
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    play_time = time_to_int(play_time)
    adv_time = time_to_int(adv_time)
    dp = [0] * (play_time + 1)

    for log in logs:
        start, end = log.split('-')
        start = time_to_int(start)
        end = time_to_int(end)
        dp[start] += 1
        dp[end] -= 1
    
    for i in range(1, play_time + 1):
        dp[i] += dp[i - 1]
    
    for i in range(1, play_time + 1):
        dp[i] += dp[i - 1]
    
    most_view, max_time = dp[adv_time - 1], 0 
    for i in range(adv_time, play_time):
        if most_view < dp[i] - dp[i - adv_time]:
            most_view = dp[i] - dp[i - adv_time]
            max_time = i - adv_time + 1
    return int_to_time(max_time)

play_time = "02:03:55"
adv_time = 	"00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))