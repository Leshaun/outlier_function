my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45, 82, 11, 54, 2, 16, 9, 100]

remove_this_many = len(my_list) // 10

try:
    my_list_sorted = sorted(my_list, reverse=True)
    average_of_90list = sum(my_list_sorted[remove_this_many:]) / len(my_list_sorted[remove_this_many:])
    pain_limit = average_of_90list * 2
    for number in my_list:
        if number >= pain_limit:
            print("Large value: " + str(number) + "\nPosition: " + str(my_list.index(number) + 1))
except:
    print("Invalid list format")


