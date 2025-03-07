#using *args

class Example:
    def __init__(self,*args):
        if(len(args)==1):
            print(f"First argument: {args[0]}")
        elif(len(args)==2):
            print(f"firt arg + Second arg: {args[0]}-{args[1]}")

obj1=Example("sai")
obj2=Example("sai",25)
