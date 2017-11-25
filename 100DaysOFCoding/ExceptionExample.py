try:
    fh = open("testfile", "r")
    fh.write("i should write something")
except IOError:
    print("error: can't write to the file")
else:
    print("content was written to the file")
    fh.close()
finally:
    print("finally came here")
