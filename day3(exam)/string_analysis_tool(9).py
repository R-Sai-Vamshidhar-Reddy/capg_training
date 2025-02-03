def digits(n):
    cnt1=0
    for i in n:
        if(i.isdigit()):
            cnt1+=1
    print(f"No of digits in string are: {cnt1}")
def special_char(n):
    c=0
    for i in n:
        if(31<ord(i)<48) or (57<ord(i)<65 or (90<ord(i)<97) or (122<ord(i)<127)):
            c+=1
    print(f"No of special_characters in string are: {c}")
def vowels(n):
    cnt2=0
    for i in n:
        if(i in ("aeiouAEIOU")):
            cnt2+=1
    print(f"No of vowels in string are: {cnt2}")
def consonents(n):
    cnt3=0
    for i in n:
        if (i not in ("aeiouAEIOU")):
            cnt3+=1
    print(f"No of consonents in string are: {cnt3}")
def main():
    n=input("Enter the String: ")
    
    vowels(n)
    consonents(n)
    digits(n)
    special_char(n)
    print(f"the reverse of string is:{n[::-1]}")
main()