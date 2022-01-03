if __name__ == "__main__":
    hour, minute = map(int, input().split()) # H, M 입력 받음.

    total_minute = hour * 60 + minute # 분 단위로 바꿈
    total_minute -= 45 # 원하는 시간 = total_minute - 45

    result_hour = total_minute // 60 % 24 # 원하는 hour = 전체 시간을 60으로 나눈 몫 mod 24
    result_minute = total_minute % 60 # 원하는 hour = (전체 시간 - 전체 hour) mod 60
    
    print(result_hour, result_minute) # 결과 출력