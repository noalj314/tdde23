def sum_all_numbers(the_list):
    if type(the_list[0]) == str:
        return the_list[1:]
    elif type(the_list[0]) == list:
        return sum_all_numbers(the_list[1:])
    elif type(the_list[0]) == int:
        the_sum += the_sum + the_list[0]



sum_all_numbers(["a", "b", ["c", 3, 4, [5, "d"], 10], 9])