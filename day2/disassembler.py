import dis
def mul(a,b):
    val=a*b
    return val
def sm(a,b):
    val=a+b
    return val
def forr():
    for i in range(1,3):
        return i
def main():

    ans1=mul(5,4)
    print(ans1)
    dis.dis(mul)
    dis.dis(sm)
    dis.dis(forr)
main()