import time
import struct

f = open(r'\\.\pipe\NPtest', 'r+b', 0)
i = 1

# while True:
    # s = 'Message[{0}]'.format(i)
    # i += 1
        
    # f.write(struct.pack((len(s)) + s).encode('ascii'))   # Write str length and str
    # f.seek(0)                               # EDIT: This is also necessary
    # print('Wrote:', s)

    # n = struct.unpack((f.read(4)).decode())[0]    # Read str length
    # s = f.read(n)                           # Read str
    # f.seek(0)                               # Important!!!
    # print('Read:', s)

    # time.sleep(2)