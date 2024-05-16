# Donnee 
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"
encrypted_flag = "-4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_"
n = len(charset)

# On defini la fonction inverse de f
def f_inv(a : int, b : int, n : int, y : int):
    return (y - b) * pow(a, -1, n) % n

def decrypt(message,a,b,n):
    decrypted = ""
    for char in message:
        y = charset.index(char)
        y = f_inv(a,b,n,y)
        decrypted += charset[y]
    return decrypted

# On bruteforce les valeurs de a et b possibles
for a in range(2, n):
    for b in range(1, n):
        res = decrypt(encrypted_flag,pow(a, -1, n),b,n)
        if "404CTF{" in res:
            print(res)