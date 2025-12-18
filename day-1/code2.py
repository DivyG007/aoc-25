
def lock_picker( combo ):

    pos = 50
    combo_list = combo
    count = 0

    for each in combo_list:

        if(each[0] == 'R'):
            pos += int(each[1:])
        elif (each[0] == 'L'):
            pos -= int(each[1:])

        flag = 0

        # if(pos == 0):
            # count += 1

        while( pos > 99):
            pos -= 100
            count += 1
            # if (flag == 0):
                # count -= 1
        
        while (pos < 0):
            pos += 100
            count += 1
            # if(pos == 0):
                # count -= 1
        
        # print(pos)

    return count

# data = input("enter:")\

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
result = lock_picker(data)
print(result)
