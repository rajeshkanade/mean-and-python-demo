def process_list(lst):
    # Find min and max
    min_val = lst[0]
    max_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    print(f"Min : {min_val}, Max : {max_val}")

    # Reverse the list
    reversed_list = lst[::-1]
    print("Reversed List:", reversed_list)

    # Remove duplicates
    hash_list = []
    unique_list = []
    for i in lst:
        if i not in hash_list:
            hash_list.append(i)
            unique_list.append(i)
        else:
            continue
    print("Unique List:", unique_list)


# Main program
# Taking input from user
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# Calling the function
process_list(numbers)
