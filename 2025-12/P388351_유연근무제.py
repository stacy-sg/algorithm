def solution(schedules, timelogs, startday):
    def add_10(t):
        h = t // 100
        m = t % 100 + 10
        if m >= 60:
            h += 1
            m -= 60
        return h * 100 + m

    n = len(schedules)
    answer = 0

    for i in range(n):
        ok = True
        limit = add_10(schedules[i])

        for d in range(7):
            day = (startday + d - 1) % 7
            if day == 5 or day == 6:
                continue
            if timelogs[i][d] > limit:
                ok = False
                break

        if ok:
            answer += 1

    return answer