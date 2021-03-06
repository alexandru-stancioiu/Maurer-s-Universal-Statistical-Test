#!/usr/bin/env python
#coding: utf8

import array
import itertools

class VMPC(object):
    __slots__ = ['_P', '_N', '_S']

    def __init__(self, level=3):
        self._P = array.array('B', range(256))
        self._S = 0
        self._N = 0

    def KSA(self, cipher_key, cipher_IV=None, KSA_version=1):
        assert(type(cipher_key) is str)
        assert(16 <= len(cipher_key) <= 64)

        if cipher_IV is not None:
            assert(type(cipher_IV) is str)
            assert(16 <= len(cipher_IV) <= 64)

        if KSA_version == 2:
            assert(type(cipher_IV) is str)

        self._S = 0
        self._P = array.array('B', range(256))

        self._KSA(cipher_key)
        if cipher_IV is not None:
            self._KSA(cipher_IV)
        if KSA_version == 2:
            self._KSA(cipher_key)

    def _KSA(self, cipher_key):
        tmp_key = array.array('B', cipher_key)
        tmp_length = len(tmp_key)
        tmp_S = self._S
        tmp_P = self._P

        for m in xrange(768):
            n = m & 255
            tmp_S = tmp_P[(tmp_S + tmp_P[n] + tmp_key[m % tmp_length]) & 255]
            tmp_P[tmp_S], tmp_P[n] = tmp_P[n], tmp_P[tmp_S]

        self._S = tmp_S
        self._P = tmp_P
        self._N = 0

    def crypt(self, data):
        assert(
            type(data) is str
            or type(data) is array.array
            )
        s, n = self._S, self._N
        tmp_P = self._P
        tmp_data = array.array('B', data)
        for i in xrange(len(data)):
            s = tmp_P[(s + tmp_P[n]) & 255]
            tmp_data[i] ^= tmp_P[(tmp_P[tmp_P[s]] + 1) & 255]
            tmp_P[s], tmp_P[n] = tmp_P[n], tmp_P[s]
            n = (n + 1) & 255
        self._S, self._N = s, n
	print tmp_data.tostring().encode('hex')
	sample = open("sample.txt", "w")
    	sample.write(tmp_data.tostring().encode('hex'))
    	sample.close()
	print len('lenght' + tmp_data.tostring().encode('hex'))
        return tmp_data.tostring()
    decrypt = crypt

    def _cipher_stream(self):
        while 1:
            yield ord(self.crypt('\0'))

if __name__ == '__main__':
    test = VMPC()
    test.KSA('test' * 16) 
    test.crypt('\0' * 1024 * 1024)
