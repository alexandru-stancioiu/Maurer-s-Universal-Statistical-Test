from Crypto.Cipher import ARC4

def main():
    bytes = 1000

    #key = "key"
    #cipher = ARC4.new(key)
    #msg = cipher.encrypt(bytes * '\x00')
    msg = ''
    for i in range (0, bytes):
        msg += str(i)

    sample = open("sample.txt", "w")
    sample.write(msg.encode('hex'))
    sample.close()

if __name__ == "__main__":
    main()