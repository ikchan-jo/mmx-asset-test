import sys

print ("train.py")
i = int(sys.argv[1])

if 1 == i:
    raise Exception("1 is error")
    sys.exit(1)
elif 2 == i:
    print("2 is ok")
elif 3 == i:
    print("3 is ok")
else:
    raise Exception("{} is error".format(i))
    
sys.exit(0)
