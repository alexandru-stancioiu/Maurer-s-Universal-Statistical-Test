import math
import sys

def hex2bin(hs):
    """
      Transform a hex string (e.g. 'a2') into a string of bits (e.g.10100010)
    """
    bs = ''
    for c in hs:
        bs = bs + bin(int(c,16))[2:].zfill(4)
    return bs

def backtrack(key, L, table):
    if (len(key) < L):
        backtrack(key + "0", L, table)
        backtrack(key + "1", L, table)
    else:
        table[key] = 0

def main():

    with open(sys.argv[1], 'r') as f:
        sample = f.readline()

    table = {}
    bin_sample = hex2bin(sample)
    n = len(bin_sample)

    # Calculate best values for L and Q based on length_bin_sample

    # [n, L, Q = 2 * 10^L, expectedValue, variance]
    input_size = [
        [387840, 6, 640, 5.2177052, 2.954],
        [904960, 7, 1280, 6.1962507, 3.125],
        [2068480, 8, 2560, 7.1836656, 3.238],
        [4654080, 9, 5120, 8.1764248, 3.311],
        [10342400, 10, 10240, 9.1723243, 3.35],
        [22753280, 11, 20480, 10.170032, 3.384],
        [49643520, 12, 40960, 11.168765, 3.401],
        [107560960, 13, 81920, 12.168070, 3.410],
        [231669760, 14, 163840, 13.167693, 3.416],
        [496435200, 15, 327680, 14.167488, 3.419],
        [1059061760, 16, 655360, 15.167379, 3.421]
    ]

    L = input_size[0][1]
    Q = input_size[0][2]
    expectedValue = input_size[0][3]
    variance = input_size[0][4]
    for i in range(1, len(input_size) - 1):
        if (input_size[i][0] >= n) and (input_size[i + 1][0] < n):
            L = input_size[i][1]
            Q = input_size[i][2]
            expectedValue = input_size[i][3]
            variance = input_size[i][4]
            break
    if n >= input_size[len(input_size) - 1][0]:
        L = input_size[len(input_size) - 1][1]
        Q = input_size[len(input_size) - 1][2]
        expectedValue = input_size[len(input_size) - 1][3]
        variance = input_size[len(input_size) - 1][4]

    initialization_segment = bin_sample[0 : Q * L]
    K = n/L - Q
    test_segment = bin_sample[Q * L : (Q + K) * L]

    backtrack("", L, table)

    for i in range((Q - 1) * L, -1, -L):
        block_id = i/L + 1
        block = str(initialization_segment[i : i + L])
        if table[block] < block_id:
            table[block] = block_id

    sum = 0
    for i in range(0, K * L, L):
        block_id = Q + i/L + 1
        block = str(test_segment[i : i + L])
        diff = block_id - table[block]
        sum += math.log(diff, 2)
        table[block] = block_id

    fn = sum / K

    c = 0.7 - 0.8/L + (4 + 32/L) * math.pow(K, -3/L) / 15
    sigma = c * math.sqrt(variance/K)
    pvalue = math.erfc(math.fabs((fn - expectedValue) / (math.sqrt(2) * sigma)))

    print 'P-value: ' + str(pvalue)
    if (pvalue < 0.1):
        print 'Sequence is non-random'
    else:
        print 'Sequence is random'

if __name__ == "__main__":
    main()
