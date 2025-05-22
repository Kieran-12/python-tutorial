lst1 = input().split(",")
lst2 = input().split(",")
print(lst1, lst2)
length1 = len(lst1)
length2 = len(lst2)

if lst1[0] == "" and lst2[0] == "":
    print("True")
else:
    if length1 < length2 or lst2[0] == "":
        print("False")
    else:
        for i in range(0, length1):
            numbers = lst1[i : i + length2]
            print(numbers)
            if len(numbers) == length2:
                if numbers == lst2:
                    print("True")
                    break
                else:
                    continue
            else:
                print("False")
