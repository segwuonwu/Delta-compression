import numpy as np

def deltaCompression(sequence):
    arr = sequence.split()
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    decoding = np.cumsum(arr)
    return ' '.join(map(str, decoding))

test = '-123 -11 6 14 -1 -3 4 9 1 5 -6 3 -10 155 -7 0 14 -9 15 3 11 -1 -10 -8 5'
print(test)
print(deltaCompression(test))