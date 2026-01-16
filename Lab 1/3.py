# Perceptron implementation for AND and OR gates

def step_function(x):
    return 1 if x >= 0 else 0


def perceptron(x1, x2, w1, w2, b):
    weighted_sum = x1*w1 + x2*w2 + b
    return step_function(weighted_sum)


# Input combinations
inputs = [(0,0), (0,1), (1,0), (1,1)]

print("AND Gate Output")
for x1, x2 in inputs:
    output = perceptron(x1, x2, w1=1, w2=1, b=-1.5)
    print(f"{x1} AND {x2} = {output}")

print("\nOR Gate Output")
for x1, x2 in inputs:
    output = perceptron(x1, x2, w1=1, w2=1, b=-0.5)
    print(f"{x1} OR {x2} = {output}")
