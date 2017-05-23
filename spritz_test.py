from spritz import Spritz
import binascii

def test(input, output, result):
    print 'Input: %s, Output: %s - %s' % (input, output, 'PASSED' if output == result else 'FAILED')

spritz = Spritz()

print '// Test basic Spritz output test vectors:'

output_test_vectors = {
    'ABC': '779a8e01f9e9cbc0',
    'spam': 'f0609a1df143cebf',
    'arcfour': '1afa8b5ee337dbc7'
}

for input, result in output_test_vectors.items():
    spritz.initialise_state()
    spritz.absorb(bytearray(input))
    output = binascii.hexlify(spritz.squeeze(8))
    test(input, output, result)

print
print '// Test Spritz hash test vectors:'

hash_test_vectors = {
    'ABC': '028fa2b48b934a18',
    'spam': 'acbba0813f300d3a',
    'arcfour': 'ff8cf268094c87b9'
}

for input, result in hash_test_vectors.items():
    output = binascii.hexlify(spritz.hash(bytearray(input), 32))
    test(input, output[:16], result)

print
print '// Encryption demo:'

key = bytearray('password') # password, test, 
message = bytearray('Hello world! This is a simple Python implementation of Spritz, a redesigned version of the RC4 stream cipher recently published by Rivest and Schuld, which addresses many of the shortcomings that have been identified in RC4. Since Spritz is a sponge-like function, it can also be used to produce cryptographic hashes of an arbitrary length. Unofficial implementation of VMPC (Variably Modified Permutation Composition) stream cipher. There would be possible change in class interface to conform with other crypt libraries like PyCrypto. ')
output = spritz.encrypt(key, message)
sample = open("sample.txt", "w")
#for i in range(100):
sample.write(binascii.hexlify(output)) #output.encode('hex'))
sample.close()
print len('lenght' + binascii.hexlify(output))
print binascii.hexlify(output)
print

print '// Decryption demo:'
print spritz.decrypt(key, output)
