def my_sum(x, y):
    return x + y

raw_data = [i for i in range(5)]
print sum(raw_data)

print reduce(my_sum, raw_data)
