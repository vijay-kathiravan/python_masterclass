# jabber = open("C:/Users/vijay/Downloads/sample.txt",'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line,end='')
# jabber.close()
# with open("C:/Users/vijay/Downloads/sample.txt",'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line,end='')
# with open("C:/Users/vijay/Downloads/sample.txt",'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line,end='')
#         line = jabber.readline()
with open("C:/Users/vijay/Downloads/sample.txt",'r') as jabber:
    line = jabber.readlines()
print(line)