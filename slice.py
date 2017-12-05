slice_list = []
# slice_list = [i for i in range(10) ]
for i in range(10):
    slice_list.append(i)

print slice_list

print len(slice_list)

print slice_list[0], slice_list[-1], slice_list[0: 2:], type(slice_list[0: 2]), slice_list[::-1]

class Myseq:
    my_list = [ i for i in range(5) ]

    def __getitem__(self, index):
        return self.my_list[index]

    def __len__(self):
        return len(self.my_list)

my_list = Myseq()
print my_list[0: 3], len(my_list) 
