# number of cases
case = int(input("Enter number of Cases: "))

# case validation
if case < 1 or case > 100:
    quit()


def equation(current_floor, total_floor, total_height):
    floor_height = total_height / total_floor
    current_height = floor_height * \
        (current_floor - 1)  # ground floor height = 0

    return current_height


place_holder_list = []

for i in range(case):
    current_floor, total_floor, total_height = map(int, input(
        "Enter Current Floor, Total Floor, and Total Height: ").split())
    # input validation
    if current_floor < 1 and total_height > 100 and current_floor > total_floor:
        quit()
    place_holder_list.append(
        equation(current_floor, total_floor, total_height))

for i in place_holder_list:
    print(f"Current floor is {i:0.2f} unit High")
