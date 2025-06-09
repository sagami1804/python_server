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

# 暗号化(RSA)
def encRsaCrt(plane, n, e):
    encryptText = (plane ** e) % n
    return encryptText

# 復号(RSA-CRT)
def decRsaCRT(encryptText, n, p, q, dp, dq, qinv):
    mp = (encryptText ** dp) % p
    mq = (encryptText ** dq) % q
    decryptText = calcCrt(mp, mq, q, qinv) % n
    return decryptText

# 中国剰余定理（CRT）
def calcCrt(mp, mq, q, qinv):
    crt = mq + (mp - mq) * qinv * q
    return crt

# 拡張ユークリッドの互除法
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# モジュラ逆数
def modinv(q, p):
    g, x, y = xgcd(q, p)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % p

if __name__ == "__main__":

    # 秘密鍵
    p = getPrime(8)
    q = getPrime(8)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = modinv(e, phi)

    # 秘密鍵(RSA-CRTで拡張したもの)
    dp = d % (p - 1)
    dq = d % (q - 1)
    qinv = modinv(q, p)
    
    # 平文（4桁の数値）
    m = 9999
    print("平文：" + str(m))

    # 暗号化
    c = encRsaCrt(m, n, e)

    print("暗号文：" + str(c))

    # 復号
    m = decRsaCRT(c, n, p, q, dp, dq, qinv) 

    print("復号した文：" + str(m))