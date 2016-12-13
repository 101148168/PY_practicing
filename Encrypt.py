CIPHER = {'a':'f', 'b':'e', 'c':'d', 'd':'c', 'e':'b','f':'a', 'i':'z', 'o':'l'}

# Encode button
def encode(msg):
    print(msg,"encodes to: ",'%s' % ''.join(
        CIPHER[ch] if ch in CIPHER.keys() else ch for ch in msg ))

# Decode button
def decode(msg):
    print(msg, "decodes to: ", '%s' % ''.join(
        CIPHER[ch] if ch in CIPHER.values() else ch for ch in msg ))

def decide(choose, msg):
    if choose in ['e', 'E']:
        encode(msg)
    elif choose in [ 'd', 'D']:
        decode(msg)
    else :
        print('Enter invalid please try again')
        
def main():
    while True:
        msg = input("Input words: ")
        choose =input("Encode please enter 'E', Decode please enter 'D': ")
        decide(choose, msg)

main()
    


