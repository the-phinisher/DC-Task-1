import numpy as np
from itertools import permutations

print("--Part A--")
n = int(input("Enter the no. of dimensions of the vectors: "))

y_hat = np.random.random(n)
y = np.random.randint(0, 2, n)
O = - np.average(y * np.log2(y_hat) + (1-y) * np.log2(1 - y_hat))
print("y = {}".format(y), "y_hat = {}".format(y_hat), "Cross-Entropy loss = {}".format(O),sep='\n\n', end='\n')

print("--Part B--")
class Sum_Finder:
    def __init__(self, inputs):
        self.inputs = inputs
        self.inputs_length = len(inputs)

    def find_sum(self, target):
        self.count = 1
        output =  {self.count:self.found(i,j) for i in range(self.inputs_length) for j in range(self.inputs_length) if self.inputs[i] + self.inputs[j] == target}
        return output
    
    def found(self, i, j):
        self.count += 1
        return [i, j]

    def change_inputs(self, inputs):
        self.inputs = inputs
        self.inputs_length = len(inputs)


if __name__ == "__main__":
    x = Sum_Finder([10,20,10,40,50,60,70])
    target = 50
    x.find_sum(target)
