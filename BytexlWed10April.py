# claculate again
def win_changes_to_balance(string):
    str_count = 0
    hash_count = 0

    # count occurrence of '*' and '#'

    for char in string:
        if char == '*':
            str_count += 1
        elif char == '#':
            hash_count += 1

    # Calculate the absolute difference
    difference = abs(str_count - hash_count)
    return difference
# Example usage
input_string ="*##**#*##"
result = min_operations_to_make_valid(input_string)
print("Minimum operarons needed:", result)
