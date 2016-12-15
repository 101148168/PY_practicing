CIPHER = {'a':'f', 'b':'e', 'c':'d', 'd':'c', 'e':'b','f':'a'}

# Encode button
def encode(msg):
    print(msg,"encodes to: ",'%s' % '*E*L*'+''.join(
        CIPHER[ch] if ch in CIPHER.keys() else ch for ch in msg ))


def revmapper(to):
    for k, v in CIPHER.items():
        if v == to: return k
        
# Decode button
def decode(msg):
    print(msg, "decodes to: ", '%s' % ''.join(
        revmapper(ch) if ch in CIPHER.values() else ch for ch in msg ))
     

def decide(msg):
    jud = msg[0:5]  # *** or not
    if jud != '*E*L*':
        encode(msg)
    else:
        decode(msg[5:])
        
def main():
    while True:
        msg = input("Input words: ")
        decide(msg)


main()
    


