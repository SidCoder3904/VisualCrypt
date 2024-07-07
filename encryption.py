from PIL import Image
import random

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    if(i<64):
      m.append("0"+bin(i)[2:])
    else:
      m.append(bin(i)[2:])
  return m

def encrypt(im,msg,pixel_map,jump,start_height,start_width):
    binary=toBinary(msg)
    i=start_height
    j=start_width
    width,height=im.size
    for k in range(0,len(binary)):
        char=binary[k]
        for x in range(len(char)):
            if(j<width):
                new_bit_r=((pixel_map[j,i][0]>>1)<<1)+int(char[x])
                new_bit_g=((pixel_map[j,i][1]>>1)<<1)+int(char[x])
                new_bit_b=((pixel_map[j,i][2]>>1)<<1)+int(char[x])
                pixel_map[j, i] =(new_bit_r,new_bit_g,new_bit_b)
                j=j+jump
            else:
                j=j-width
                i=i+1
                new_bit_r=((pixel_map[j,i][0]>>1)<<1)+int(char[x])
                new_bit_g=((pixel_map[j,i][1]>>1)<<1)+int(char[x])
                new_bit_b=((pixel_map[j,i][2]>>1)<<1)+int(char[x])
                pixel_map[j, i] =(new_bit_r,new_bit_g,new_bit_b)
                j=j+jump

def imageEncryption(jump,offset):
  imageName=input("Enter the complete image address : ")
  im=Image.open(imageName,'r')
  msg=input("Enter the message : ")
  len_msg=len(msg)
  if (len_msg<10):
    msg = str("0")+str(len_msg)+msg
  elif (len_msg>99) :
     print('Message lenght exceeded.')
  else:
    msg = str(len_msg)+msg
  pixel_map = im.load()
  encrypt(im,msg,pixel_map,jump,0,offset)
  im.save("encrypt_img1.png")
