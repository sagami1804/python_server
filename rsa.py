from Crypto.Util.number import getPrime

charToNumber = {
    ' ': 0,
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    '0': 27,
    '1': 28,
    '2': 29,
    '3': 30,
    '4': 31,
    '5': 32,
    '6': 33, 
    '7': 34, 
    '8': 35,
    '9': 36,
}

numberToChar = {
    0: ' ',
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z',
    27: '0',
    28: '1',
    29: '2',
    30: '3',
    31: '4',
    32: '5',
    33: '6',
    34: '7',
    35: '8',
    36: '9'
}

# 暗号化(共通)
def encRsaCrt(plane, n, e):
    encryptText = pow(plane, e, n)
    return encryptText

# 復号(RSA)
def decRsa(encryptText, n, d):
    decryptText = pow(encryptText, d, n)
    return decryptText

# 復号(RSA-CRT)
def decRsaCrt(encryptText, n, d, p, q):
    # 秘密鍵(RSA-CRTで拡張したもの)
    dp = d % (p - 1)
    dq = d % (q - 1)
    qinv = pow(q, -1, p)

    # 暗号文を分ける
    mp = pow(encryptText, dp, p)
    mq = pow(encryptText, dq, q) 

    # 中国剰余定理を使用してそれぞれ復号した文を元の復号した文に戻す
    decryptText = calcCrt(mp, mq, n, p, q, qinv)
    return decryptText

# 中国剰余定理（CRT）
def calcCrt(mp, mq, n, p, q, qinv):
    t = (qinv * (mp - mq)) % p
    crt = (mq + q * t) % n
    return crt

if __name__ == "__main__":

    # 秘密鍵
    p = getPrime(512)
    q = getPrime(512)

    # 公開鍵
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537

    # 秘密鍵
    d = pow(e, -1, phi)
    
    # 平文（数値）
    m = 1234567890123456
    print("平文：" + str(m))

    # 暗号化
    c = encRsaCrt(m, n, e)
    print("暗号文：" + str(c))

    # 復号(通常のRSA)
    mRsa = decRsa(c, n, d) 
    print("復号した文（通常のRSA）：" + str(m))

    # 復号(CRT)
    mCrt = decRsaCrt(c, n, d, p, q) 
    print("復号した文（CRT）　　　：" + str(m))
