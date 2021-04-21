# Artificial Intelligence
# Jokebed Aguirre

def stairs(cont):
    step = [0] * (cont + 2)
    step[0] = 1
    step[1] = 1
    step[2] = 2

    for i in range(3, cont + 1):
        step[i] = step[i - 1] + step[i - 2] + step[i - 3]

    return step[cont]

# Number of stair steps
cont = 5
print("Different ways to step-up the stairs:")
print(stairs(cont))
