def say_hello():
    return 'hello'
print say_hello()

def say_hello_patch():
    return 'hello python'
print say_hello_patch()

say_hello = say_hello_patch

print say_hello()
