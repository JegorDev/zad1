def calculate_fibonacci(index, previous_calculations):
    print("Previous calculations")
    print(previous_calculations)
    if index == 1 or index == 2:
        return 1

    # bottom_up = [None] * (index + 1)
    previous_calculations[1] = 1
    previous_calculations[2] = 1
    for i in range(3, index + 1):
        if i in previous_calculations:
            print(f"{i} calculated already")
            # bottom_up[i] = previous_calculations[i]
        else:
            print(f"Calculating {i} for the first time")
            calculated_value = previous_calculations[i - 1] + previous_calculations[i - 2]
            previous_calculations[i] = calculated_value
            previous_calculations[i] = calculated_value

    return previous_calculations[index], previous_calculations
