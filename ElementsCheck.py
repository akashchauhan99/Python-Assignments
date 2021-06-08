from collections import Counter

def ElementCheck(listCheck):
    first = listCheck[0].lower()
    second = listCheck[1].lower()

    counter_First = Counter(first)
    counter_second = Counter(second)

    for ch in counter_second:
        if counter_First[ch] != counter_second[ch]:
            return False
    return True

listval1 = ["hello", "Hello"]
listval2 = ["hello", "hey"]
listval3 = ["Alien", "line"]

print(ElementCheck(listval1))
print(ElementCheck(listval2))
print(ElementCheck(listval3))
