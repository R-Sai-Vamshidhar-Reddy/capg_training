class Example:
    def __init__(self,**kwargs):
        if "name" in kwargs and "age" in kwargs:
            print(f"Hello {kwargs["name"]} ,you are {kwargs["age"]} years old")
        elif "name" in kwargs:
            print(f"your name is {kwargs["name"]}")
obj=Example(name="Sai")