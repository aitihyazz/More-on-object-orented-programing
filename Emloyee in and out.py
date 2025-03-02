class employee:
    def __init__(self):
        print("Constructor created")
    def __del__(self):
        print('destructor called')
def createobj():
    print("Making object")
    obj=employee()
    print("Function ended")
    return obj
print('calling create obj function')
obj=createobj()
print('Programe end')
