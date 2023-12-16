from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

alpha = 2
prime = 29

alicePrivKey = 17
alicePubKey = (alpha ** alicePrivKey) % prime


bobPrivKey = 12
bobPubKey = (alpha ** bobPrivKey) % prime

aliceSharedKey = (bobPubKey ** alicePrivKey) % prime

bobSharedKey = (alicePubKey ** bobPrivKey) % prime

print(aliceSharedKey == bobSharedKey)
