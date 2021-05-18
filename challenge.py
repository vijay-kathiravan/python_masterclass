# Write a programme to append the times table to our jabber wockey programme
# in sample.txt. we want the tables from 2 to 12 ( Similar to the output from
# the for loops part 2 lecture in section 6).

# The first column of the numbers should be right justified
with open("C:/Users/vijay/Downloads/sample.txt",'w') as jabber:
    for i in range(2,13):
        for j in range(1,14):
            print("{} times {} is {}".format((str(j).rjust(4)),i,i*j),file=jabber)
        print("*"*40,file=jabber)
