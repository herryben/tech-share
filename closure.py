def outter(j):
    def inner(i):
         return j + i
    return inner

rec_inner = outter(100)

print rec_inner 
print rec_inner(2)
print rec_inner(3) #no state

def log(func):
    def _log():
        print 'before funciton'
        res = func()
        print 'after funciton'
	return res
    return _log

@log
def cal():
     print 'this is cal'

cal()
