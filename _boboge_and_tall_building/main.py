# number of cases
t = int(input())

# case validation
if t < 1 or t > 100:
    quit()


def equation(n, m, k):
    floor_hight = k / m
    bobogo_hight = floor_hight * (n - 1)

    return bobogo_hight


place_holder_list = []

for i in range(t):
    n, m, k = map(int, input().split())
    # input validation
    if n < 1 and k > 100 and n > m:
        quit()
    place_holder_list.append(equation(n, m, k))

for i in place_holder_list:
    print(i)
