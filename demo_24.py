# Global

global_value = 10
print(global_value)

def foo():
    global global_value
    print(global_value)
    global_value = 5
    print(global_value)

foo()

