
def looper(num, size):
    flag = 0
    for i in range(0,len(num)-size,size):
        if(num[i:i+size] != num[i+size:i+size*2]):
            flag = 1

    if flag == 0:
        print(int(num))
        return int(num)
    else:
        return 0

def invalid_checker(ranges):
    total = 0
    for each in ranges:
        each_range = each.split('-')

        for each2 in range(int(each_range[0]),int(each_range[1])+1):
            s = str(each2)
            for i in range(1,len(s)//2+1):
                if( s[:i] == s[i:i*2]):
                    k = looper(s, i)
                    if(k != 0):
                        total += k
                        break
    return total

with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

result = invalid_checker(text.split(','))
print(result)