x="100100101010100110100010"
xw="code"
y="000001110000111010100000010100111000111000100010"
yw="Bbraille"    
z="000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
zw="Tthe quick brown fox jumps over the lazy dog"

# class Matrix():

a = [['000001', True]]

def append_dict(n, w):
    count = 0
    for i in range(0,len(n),6): 
        x = [w[count], n[i:i+6]]
        flag_rep = False
        if i > 0:
            for j in a:
                if j[1] == n[i:i+6]:
                    flag_rep = True
        if flag_rep == False:
                a.append(x)
           
        count = count+1

append_dict(x, xw)
append_dict(y, yw)
append_dict(z, zw)
for i in a:
    print(i)

def translate(s):
    result: 
    
    print(result)

