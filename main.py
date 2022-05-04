import numpy as np
from os import system as bas

# Key = np.array([[17, 17, 5], [21, 26, 21], [2, 2, 1]]) #([[n,p,m],]) for declaring 2-D arrays
moder = int(27)
dicti = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25,
    ' ':26 # The Forbiden character. Muhuhahahahaha!!!!!!.....Shhhhhhhhhhhhh!.....
}

def Key():
    key_str = "ABILITIES"
    return np.array([dicti.get(s.lower(), 26) for s in key_str]).reshape(3,3)


def is_key_valid():
    det_key = int(np.linalg.det(Key()))%moder
    try:
        inv_mod = pow(det_key, -1, moder)
        # print("Det: ",det_key)
        # print("inv_mod: ",pow(det_key, -1, moder))
    except:
        # print("Det: ",det_key)
        # print("inv_mod: ",pow(det_key, -1, moder))
        return False
    return True


def verify_key_inv(key_inv):
    if np.array_equal((Key()@key_inv)%moder,np.identity(3)):
        print("Key Inverse Verified Successfully!")
        return True
    else:
        print("Error: Key inverse failed to get verified :(")
        return False


def vecls_to_str(ls): #coverts column vetor list into string text
    str_txt = ""
    dicti_keyls = list(dicti.keys())
    for v, c in enumerate(ls, 0):
        for it in range(0,3):
            str_txt += dicti_keyls[ls[v][it]]
    return str_txt

def vlu_ls_to_str(ls): #coverts 1d array of ascii values into string text
    str_txt = ""
    dicti_keyls = list(dicti.keys())
    for v in ls:
        str_txt += dicti_keyls[v]
    return str_txt


def adjointer(matrix):
    mtrx = matrix.ravel()  #ravel() converts 2d array to 1d
    A= +((mtrx[4]*mtrx[8])-(mtrx[5]*mtrx[7]))
    B= -((mtrx[3]*mtrx[8])-(mtrx[5]*mtrx[6]))
    C= +((mtrx[3]*mtrx[7])-(mtrx[6]*mtrx[4]))
    D= -((mtrx[1]*mtrx[8])-(mtrx[2]*mtrx[7]))
    E= +((mtrx[0]*mtrx[8])-(mtrx[2]*mtrx[6]))
    F= -((mtrx[0]*mtrx[7])-(mtrx[1]*mtrx[6]))
    G= +((mtrx[1]*mtrx[5])-(mtrx[2]*mtrx[4]))
    H= -((mtrx[0]*mtrx[5])-(mtrx[2]*mtrx[3]))
    I= +((mtrx[0]*mtrx[4])-(mtrx[1]*mtrx[3]))
    cofactor = np.array([[A, B, C], 
                         [D, E, F], 
                         [G, H, I]])
    adjnt = cofactor.T
    return adjnt #convert back to 2d array + transpose



def encipher(plain_txt):

    if not is_key_valid():
        return print("\nYour Key is not compatible. Please change the key!\n")


    '''
        Below given .join() evil looking thing just removes the whitespaces from the input text 
        so that it doesn't contradict with dicti.
    '''
    # compatible_pln_txt = "".join(plain_txt.split())


    while (len(plain_txt))%3 != 0:    #prepairing to easily divide string into 3 equal parts/vectors
        plain_txt += " "


    # ord() and chr() for ascii conversions
    
    ascii_ls = [dicti.get(s.lower(), 26) for s in plain_txt]

    # for g, h in enumerate(ascii_ls, 0): #so that no confusion occurs if input other than dicti
    #     if h not in dicti.keys():
    #         ascii_ls[g] = 26



    col_vecls = []
    i = int(0)
    for j in range(int(len(ascii_ls)/3)):
        col_vecls.append(np.array([ascii_ls[i], ascii_ls[i+1], ascii_ls[i+2]]))
        i+=3

    # print(len(col_vecls), col_vecls)


    ##### Transformation to coloumn vectors done!!!!!!!!!
    #Hill cipher territory starts here
    ciphered_vecls = []
    for z in col_vecls:
        ciphered_vecls.append(z @ Key())  # @ == operator for matrix multiplication


    for x, l in enumerate(ciphered_vecls, 0):
        for y in range(0,3):
            ciphered_vecls[x][y] %= moder #Number of ASCII characters

    # print(col_vecls)
    # print("\n--------------------------------\n")
    # print(ciphered_vecls)

    #Convert ciphered ascii value to characters
    # cipher_txt = ""
    # dicti_keyls = list(dicti.keys())
    # for v, c in enumerate(ciphered_vecls, 0):
    #     for it in range(0,3):
    #         cipher_txt += dicti_keyls[ciphered_vecls[v][it]]
    
    return vecls_to_str(ciphered_vecls)

    # for a, b in enumerate(ascii_ls):
    #     print(type(a),chr(b))
    


def decipher(cipher_txt):
    if not is_key_valid():
        return print("\nYour Key is not compatible. Please change the key!\n")


    #Getting column vectors ready!
    col_vecls = []
    i = int(0)
    for j in range(int(len(cipher_txt)/3)):
        col_vecls.append(np.array([dicti.get(cipher_txt[i]), dicti.get(cipher_txt[i+1]), dicti.get(cipher_txt[i+2])]))
        i+=3
    #Getting Key-1 (inverse) ready!
    det_key = int(np.linalg.det(Key()))%moder
    det_inv_mod = pow(det_key, -1, moder)
    adj_key = adjointer(Key())%moder
    key_inv = (det_inv_mod*adj_key)%moder

    verify_key_inv(key_inv) #Verify if the result is identity matrix. Then good to go!

    # bas("pause")

    #col_vecs and key_inv collide here :)
    plain_vecls = []
    for col_vec in col_vecls:
        plain_vecls.append((col_vec @ key_inv)%moder)


    #convert numbers to letters
    return vecls_to_str(plain_vecls)
    #DELETE
    # plain_txt = ""
    # dicti_keyls = list(dicti.keys())
    # for v, c in enumerate(plain_vecls, 0):
    #     for it in range(0,3):
    #         plain_txt += dicti_keyls[plain_vecls[v][it]]
    
    # return plain_txt




    

if __name__ == "__main__":
    if not is_key_valid():
        print("\nYour Key is not compatible. Please change the key!\n")
        bas("pause")

    while 1:
        print("Key: ", vlu_ls_to_str(Key().ravel()))
        ciphered = encipher(str(input("Enter Plain Text: "))) #,==44 .==46
        print("Ciphered Txt: ",ciphered)
        print("Length: ",len(ciphered))
        # print("-----------------------------------------")
        deciphered = decipher(ciphered)
        print("Deciphered Txt: ",deciphered)
        print("Length: ",len(deciphered))
        print("\n-----------------------------------------\n-----------------------------------------\n")

