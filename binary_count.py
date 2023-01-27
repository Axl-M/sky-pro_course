from time import sleep
import struct

# for i in range(256):
for i in range(0, -128, -1):
    # print(i, bin(i))
    sleep(0.3)

    # print(f'{i} = {i:08b}')

# для правильного отображения отрицательных чисел
    byte = struct.pack('b', i)[0]
    # byte = struct.pack('b', i)
    print(f'{i} = {byte:08b}')
    # print(byte )
