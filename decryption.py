from PIL import Image

def decrypt(gap, offset):
    color = 1

    # opening file and extracting pixels
    img = Image.open('encrypt_img1.png', 'r')
    pixel_arr = list(img.getdata())

    # forming lastbit array
    lastbit = []
    for i in pixel_arr :
        lastbit.append(i[color]%2)

    # extracting string lenght
    binary = []
    for i in range(offset, offset+14*gap, gap) :
        binary.append(str(lastbit[i]))
    lenght = ''
    #print(binary)
    for i in range(2) :
        lenght = lenght + chr(int('0b'+''.join(binary[7*i:7*i+7]), 2))
    str_size = int(lenght)
    
    # converting to binary characters
    binary.clear()
    for i in range(offset + 14*gap, offset+7*gap*str_size + 14*gap, gap) :
        binary.append(str(lastbit[i]))

    # extracting message
    msg = ''
    for i in range(str_size) :
        msg = msg + chr(int('0b'+''.join(binary[7*i:7*i+7]), 2))
    print(msg)