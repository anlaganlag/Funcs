def d(candies,num_people):
    ans = [0] * num_people
    i = 1
    while candies > 0:
        diff =min(i, candies)
        ans[i % num_people] += diff
        candies -= diff
        i += 1
    return ans

print(d(10,3))


