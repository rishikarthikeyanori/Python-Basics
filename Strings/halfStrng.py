s=input("enter the string: ")
print(len(s.strip()))
choice=int(input("enter whether to swap first or 2nd half: "))
mid=len(s)//2


if choice==1:
    first=""
    for ch in s[:mid]:
        if ch.isupper():
            first+=ch.lower()
        else:
            first+=ch.upper()
    print(first+s[mid:])
        #swap logic for 1st half


elif choice==2:
    second=""
    for ch in s[mid:]:
        if ch.isupper():
            second+=ch.lower()
        else:
            second+=ch.upper()
    print(s[:mid]+second)
            #swap logic for second half

else:
    print("not a valid input")

