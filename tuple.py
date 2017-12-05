def get_many_result():
    return 1, 2, 3

ret = get_many_result()
print ret
a, b, c = get_many_result()
print a, b, c

import collections 
Student = collections.namedtuple('Student', 'name age sex')
tom = Student('tom', 18, 'm')
print tom.age
