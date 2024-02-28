def largestTimeFromDigits(arr):
    def makeTime(h1, h2, m1, m2):
        hour = 10 * h1 + h2
        minute = 10 * m1 + m2
        if 0 <= hour < 24 and 0 <= minute < 60:
            return str(hour).zfill(2) + ":" + str(minute).zfill(2)
        else:
            return ""

    bestTime = ""
    for h1 in arr:
        for h2 in arr:
            if h1 * 10 + h2 < 24:
                for m1 in [d for d in arr if d != h1 and d != h2]:
                    for m2 in [d for d in arr if d != h1 and d != h2 and d != m1]:
                        time = makeTime(h1, h2, m1, m2)
                        if time and time > bestTime:
                            bestTime = time
    return bestTime

print(largestTimeFromDigits([0,0,0,0]))