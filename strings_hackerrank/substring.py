def count_substring(string, sub_string):
    count = 0
    # Loop through the string one character at a time
    for i in range(len(string)):
        # Check if the string starting at 'i' matches the sub_string
        if string[i:].startswith(sub_string):
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)