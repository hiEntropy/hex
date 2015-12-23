import sys
'''

'''
def convert(value):
    if len(value)==1:
        return '%'+hex(ord(value[0]))[2:]
    else:
        return '%'+hex(ord(value[0]))[2:]+convert(value[1:])

def getArgs(value):
    if len(value)==1:
        return value[0]
    else:
        return value[0]+getArgs(value[1:])

def main():
    if len(sys.argv[1:])>0:
        input_string=getArgs(sys.argv[1:])
        print(convert(input_string))

main()
