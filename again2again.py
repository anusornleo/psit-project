"""get rich"""
def main(text):
    """find txt have over 2"""
    count_a = 0
    lstxt = sorted(text.replace('.', ' ').split())
    for i in lstxt:
        count = 0
        for j in i:
            if j in "aeiou":
                count += 1
        if count >= 2:
            print(i)
            count_a += 1
    if count_a == 0:
        print("Nope")
main(input())
