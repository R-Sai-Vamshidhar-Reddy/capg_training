class Example:
    def __init__(self,name):
        print(f"First Constructor: Hello {name}")     #it will override
    
    def __init__(self,age):
        print(f"First Constructor: age is {age}")           #it will execute

obj=Example(25)

