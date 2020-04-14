#!/usr/bin/python3


main_msg = input("to encrypt press 1 , to decrypt press 2 : ")

def encrypt():

    msg = input("put a message to encrypt : ")

    code = {"a":21,"b":22,"c":23,"d":31,"e":32,"f":33,"g":41,"h":42,"i":43,"j":51,"k":52,"l":53,"m":61,"n":62,"o":63,"p":71,"q":72,"r":73,"s":74,"t":81,"u":82,"v":83,"w":91,"x":92,"y":93,"z":94}
    
    if msg.isalpha():
        print("MESSAGE ENCRYPTED:")
        for m in msg:
            print(code[m],end="")
    else:
            print("ERROR, only characters!! *no spaces*")

    print("\n")


def decrypt():
    msg = input("put a message to decrypt : ")

    code = {'21':'a','22':'b','23':'c','31':'d','32':'e','33':'f','41':'g','42':'h','43':'i','51':'j','52':'k','53':'l','61':'m','62':'n','63':'o','71':'p','72':'q','73':'r','74':'s','81':'t','82':'u','83':'v','91':'w','92':'x','93':'y','94':'z'}
    
    step = 2
    
    f_msg = [msg[i:i+step] for i in range(0,len(msg),step)]

    print("MESSAGE DECRYPTED:")
    for h in f_msg:
        print(code[h],end="")
   
    print("\n")

    

if main_msg == "1":
    encrypt()
elif main_msg == "2":
    decrypt()
else:
    print("error, choose 1 or 2 ")



