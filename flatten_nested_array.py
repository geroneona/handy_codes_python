no_arr_within_arr_ind = 1
clean_arr = []

arr = [1,[2,[3,4]],5,69,[99,66],[0,2,4,6,8,[999666]]]

print(arr)

while no_arr_within_arr_ind != 0:
    break_ind = 0
    for i in range(len(arr))[::-1]:
        if type(arr[i]) == list:
            temp_arr = arr.pop(i)
            for idx in range(len(temp_arr))[::-1]:
                if type(temp_arr[idx]) == int:
                    clean_arr.append(temp_arr[idx])
                    temp_arr.pop(idx)
                elif type(temp_arr[idx]) == list:
                    popped_array = temp_arr.pop(idx)
                    arr.append(temp_arr)
                    arr.append(popped_array)
                    break_ind = 1
                    break
        else:
            clean_arr.append(arr[i])
            arr.pop(i)
        if arr == []:
            no_arr_within_arr_ind = 0
        if break_ind == 1:
            break

print(clean_arr[::-1])