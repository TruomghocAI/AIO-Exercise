def compute_interest(money,period):
    result = (money + (money/period))**period
    return result

print(round(compute_interest(1,12),3))
print(round(compute_interest(1,365),3))
print(round(compute_interest(1,730),3))