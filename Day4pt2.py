import hashlib

### Practice with hashlib and creating hashes
# input = ["Hello World"]
# i = hashlib.new('md5')
# i.update(b"abcdef609043")
# print(i.hexdigest())
# h = hashlib.new('md5')
# h.update(b"ckczppom")
# print(h.hexdigest())

for i in range(0,10000000):
    h = hashlib.new('md5')                      #creating a variable storing a new function of hashing via md5 algo
    # input = 'abcdef'                          #testing input
    input = 'ckczppom'
    counter = str(i)                            #Extra, but created a variable for visual understanding of counting via i
    # input = "".join((input,counter))          #Need to concatenate input and counter; this way worked but was extremely slow
    h.update(bytes(input+counter, 'ascii'))     #before hashing, string needs to be encoded; got the same same as using ascii codec?
    # h.update((input + counter).encode())      #this also worked, but need to read more into how to properly use built in
    key = h.hexdigest()                         #returning the md5 hash in hex (digest  is like the result)
    if key[:6]  == '000000':
        break
print("The lowest key that produces a MD5 hash that\n"
      "begins with '000000' is :", input+counter)
