from base64 import b64decode

p1 = b64decode("ZmxhZ3t3NDF0XzF0c19hbGxfYjE=")

print(p1)

z = 664813035583918006462745898431981286737635929725

n = (z.bit_length() + 7) // 8
p2 = (z).to_bytes(n, "big")

print(p2)

print("Flag: ", p1 + p2)