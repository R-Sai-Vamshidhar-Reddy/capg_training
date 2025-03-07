def display(ans):
    for key,value in ans.items():
        print(f"{key} - {value} times")
def count_words(n):
    dit={}
    lst=n.split()
    for i in lst:
        if(i not in dit):
            dit[i]=1
        else:
            dit[i]+=1
    return dit
def main():
    sentence=input("enter the sentence to check the word count:\n")
    ans=count_words(sentence)
    display(ans)
main()