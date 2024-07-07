import encryption,decryption
import time
from PublicKey import CreateUser
from PublicKey import GetPublicKeys
import genkey
def NewUser():

    name = input("Enter your Name : ")
    private_key = genkey.priv()
    public_key = str(genkey.mod(genkey.base, private_key, genkey.p))
    with open('PrivateKey.txt', 'w') as fp:
        fp.write(str(private_key))
    CreateUser(name,public_key)


def FindPublickey(SendersName,ReceiversName):
    publickeys=GetPublicKeys()
    keys={}
    flag1=0
    flag2=0
    for row in publickeys:
        if(row[0]==SendersName):
            keys[SendersName]=int(row[1])
            flag1=1
        if(row[0]==ReceiversName):
            keys[ReceiversName]=int(row[1])
            flag2=1
        if(flag1==1 and flag2==1):
            break
    return keys

def communicationKey(code):
    receiversName=input("Enter the receiver's username : ")
    sendersName=input("Enter the sender's username : ")
    keys=FindPublickey(sendersName,receiversName)
    with open('PrivateKey.txt','r') as file:
        privatekey=int(file.read())
    if(code==2):
        Comkey=genkey.mod(int(keys[receiversName]),privatekey,genkey.p)
    elif(code==3):
        Comkey=genkey.mod(int(keys[sendersName]),privatekey,genkey.p)
    else:
        print("Invalid Choice")
    jump=Comkey%100
    offset=(Comkey//100)%100
    if(code==2):
        encryption.imageEncryption(jump,offset)
        print("Message has been encrypted successfully")
        time.sleep(5)
    if(code==3):
        decryption.decrypt(jump,offset)
        time.sleep(1000)

def Menu():
    print("""1.Create User
2.Send Message
3.Receive Message
    """)
    choice=int(input("Select your option : "))
    if(choice==1):
        NewUser()
        print("Public key updated on database and Private key saved on the device")
        time.sleep(5)
    else:
        communicationKey(choice)
Menu()
