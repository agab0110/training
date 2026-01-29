def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

ciphertext = bytes.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c")

printable_range = range(32,127)

for k in range(256):
    key = bytes([k]) * len(ciphertext)
    pt = xor(ciphertext, key)

    if all(c in printable_range for c in pt):
        print(f"Key = {k:02x} --> {pt.decode()}")