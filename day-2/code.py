
def invalid_checker(ranges):
    total = 0
    for each in ranges:
        each_range = each.split('-')

        for each2 in range(int(each_range[0]),int(each_range[1])+1):
            s = str(each2)
            if( len(s)%2 == 0 ):
                if( s[:len(s)//2] == s[len(s)//2:]):
                    total += each2

    return total

with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

result = invalid_checker(text.split(','))
print(result)