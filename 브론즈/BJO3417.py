# One of the oldest and most common encryption algorithms is Vigenère Cipher. It is quite an old thing — a similar encryption was first described in 1553 by Giovan Battista Bellaso and improved in 1586 by Blaise de Vigenère.

# Vigenère encryption produces a single letter of ciphertext for each letter of plaintext, combining one plaintext letter with one single letter of a key on the corresponding position. If the key is shorter than the plaintext, it is simply repeated as needed, e.g. for a key of length 3 and plaintext of length 7, letters will be combined like this (Ki is the key letter, Pi is the plaintext letter, and Ci is the resulting ciphertext letter).

#  K1 K2 K3 K1 K2 K3 K1
#  P1 P2 P3 P4 P5 P6 P7
# ----------------------
#  C1 C2 C3 C4 C5 C6 C7
# The letter of the key specifies how many positions should be the plaintext letter “shifted forward” in the alphabet. If a key letter is A, the correspoding plaintext letter will be shifted by one character, B means two positions, etc. The alphabet is considered circular, so if the last letter (Z) should be shifted, it becomes A again. Please note that A (key) combined with another A (plaintext) will result in B, which may be a little unusual for the common Vigenère cipher. The Vigenère square at the end of this problem statement gives an overview how letters of a plaintext get combined with letters of a key to produce the ciphertext.

# Your task is to write a program that will encrypt messages using the Vigenère cipher with a given key.
while True:
    x = input()
    if x == '0':
        break
    else:
        y = input()
    if len(x) < len(y):
        while len(x) < len(y):
            x = x+x
    li = []
    for i in range(len(y)):
        t = ord(x[i])+ord(y[i])+1
        t = t-65
        if t > 90:
            t -= 26
        li.append(chr(t))
    print(''.join(li))