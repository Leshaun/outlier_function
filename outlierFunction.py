my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45, 82, 11, 54, 2, 16, 9, 100]

remove_this_many = len(my_list) // 10

my_list_sorted = sorted(my_list, reverse=True)

sum_of_90list = 0
items_in_90list = 0
for number in my_list_sorted[remove_this_many:]:
    try:
        sum_of_90list = sum_of_90list + number
        items_in_90list += 1
    except:
        print("Invalid list format")

average_of_90list = sum_of_90list / items_in_90list
pain_limit = average_of_90list * 2

for number in my_list:
    try:
        if number >= pain_limit:
            print("Large value: " + str(number) + "\nPosition: " + str(my_list.index(number) + 1))
    except:
        print("Invalid list format")
