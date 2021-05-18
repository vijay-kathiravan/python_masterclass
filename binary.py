# with open("binary",'bw') as bin_file:
#     for i in range(17):
#         bin_file.write(bytes(i))
# with open("binary",'br') as binfile:
#     for b in binfile:
#         print(b)
a = 65534
b = 65535
c = 65536
x = 2998302
with open("binary2",'bw') as bin_files:
    bin_files.write(a.to_bytes(2,'big'))
    bin_files.write(b.to_bytes(2,'big'))
    bin_files.write(x.to_bytes(4,'big'))
    bin_files.write(x.to_bytes(4,'little'))
with open("binary2",'br') as biniles:
    e = int.from_bytes(biniles.read(2),'big')
    print(e)
    f = int.from_bytes(biniles.read(2),'big')
    print(f)
    g = int.from_bytes(biniles.read(4),'big')
    print(g)
    h = int.from_bytes(biniles.read(4),'big')
    print(h)
    i = int.from_bytes(biniles.read(4),'big')
    print(i)