# Create a function that given a list of numbers as an input (nums_list) return True if the numbers are in consecutive order, return False if not.
# Example Input: [1,2,3,4,5]
# Example Output: True
# Example Input: [2,4,6,8,10]					
# Example Output: False
# Example Input: [10,11,12,13,14]
# Example Output: True

def number(nums_list):
    check = list(range(min(nums_list),max(nums_list)+1,1))
    print(check)
    if sorted(check) == nums_list:
        return True
    else:
        return False
print(number([2,4,6,8,10]))