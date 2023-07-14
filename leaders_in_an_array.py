def leaders_in_array(nums_array: list) -> list:
    array_leaders: list[int] = []
    for index in range(0, len(nums_array) - 1):
        if nums_array[index] > max(nums_array[index + 1:]):
            array_leaders.append(nums_array[index])
    array_leaders.append(nums_array[-1])
    return array_leaders


try:
    print("Enter integer elements of an array separated by space to get the leaders in the array : ")
    numbers_array = list(map(int, input().split()))
    print("The leaders in an array are : ", leaders_in_array(numbers_array))
except ValueError:
    print("Invalid input. Please Enter only Integers separated by space")
