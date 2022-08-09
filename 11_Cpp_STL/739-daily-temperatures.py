def daily_temperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    dates = []

    for i in range(n - 1, -1, -1):
        while dates and temperatures[dates[-1]] <= temperatures[i]:
            dates.pop()

        if dates:
            ans[i] = dates[-1] - i
        else:
            ans[i] = 0
        
        dates.append(i)
    
    return ans


# Test
print(daily_temperatures([73,74,75,71,69,72,76,73]))
# Output: [1,1,4,2,1,1,0,0]
print(daily_temperatures([30,40,50,60]))
# Output: [1,1,1,0]
print(daily_temperatures([30,60,90]))
# Output: [1,1,0]
