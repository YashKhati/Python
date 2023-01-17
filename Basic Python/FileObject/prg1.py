# file objects

# f = open('test.txt') # default specified for reading

# f = open('test.txt', 'r')  # open file in read mode

# print(f.mode)

# f.close()

# context manager
# automatically closes file

# with open('test.txt','r') as f:
    # f_contents = f.read()
    # print(f_contents)

    # f_contents = f.readline()
    # print(f_contents)

    # f_contents = f.readlines()
    # print(f_contents)

    # for line in f:
    #   print(line, end='')

    # f_contents = f.read(30)
    # rint(f_contents,end='')

    # f_contents = f.read(50)
    # print(f_contents,end='')



'''

with open('test.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents,end='')
    print('\nf.tell() = ',f.tell())
    #f.seek(0)
    #print("\nf.tell() = ",f.tell())
    f_contents = f.read(size_to_read)
    print(f_contents,end='')
    print('\nf.tell() = ',f.tell())
   # while len(f_contents) > 0 :
    #    print(f_contents,end='*')
    #    f_contents = f.read(size_to_read)

'''


with open('test2.txt', 'w') as f:
    f.write('Ayush')
    f.write('Test')
    f.seek(0)
    f.write('Yash')


with open('test.txt', 'r') as rf:
    with open('test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)

path = 'dog.jpg'
with open(path, 'rb') as rimg:
    with open('dog_copy.jpg', 'wb') as wimg:
        # for line in rimg:
            # wimg.write(line)
        chunk_size =4096
        rimg_chunk = rimg.read(chunk_size)
        while len(rimg_chunk) >0:
            wimg.write(rimg_chunk)
            rimg_chunk = rimg.read(chunk_size)
