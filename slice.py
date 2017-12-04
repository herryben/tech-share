slice_list = []
# slice_list = [i for i in range(10) ]
for i in range(10):
    slice_list.append(i)

print slice_list

print len(slice_list)

print slice_list[0], slice_list[-1], slice_list[0: 2:], type(slice_list[0: 2])
