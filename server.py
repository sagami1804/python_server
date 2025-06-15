# server.py
import socket
import threading
import time
from rsa import *

HOST = '0.0.0.0'  # 全てのインターフェースで待ち受け
PORT = 12345      # 使用するポート番号

# pとqの素数を生成
P = getPrime(512)
Q = getPrime(512)

N = P * Q
PHI = (P - 1) * (Q - 1)
E = 65537
D = pow(E, -1, PHI)

# 秘密鍵(RSA-CRTで拡張したもの)
DP = D % (P - 1)
DQ = D % (Q - 1)

# クライアントとの通信
def handle_client(conn, addr):
    print(f"{addr} と接続されました")
    
    # 公開鍵を送信
    public_key = f"{N},{E}"
    conn.sendall(public_key.encode())
    
    with conn:
        while True:
            # データ受信
            data = conn.recv(1024)
            
            # データが空なら終了
            if not data:
                break
            data = data.decode()
            print(f"\n{addr} から受信(暗号): {data}\n")
            dec_data = str(decryption(int(data)))
            print(f"{addr} から受信(平文): {dec_data}\n")

            # 復号結果をクライアントに送信
            dec_data_add_hyphen = f"{dec_data[:4]}-{dec_data[4:8]}-{dec_data[8:12]}-{dec_data[12:]}"
            response = "受信しました: " + dec_data_add_hyphen
            conn.sendall(response.encode())
            
    print(f"{addr} との接続を終了しました")

# 復号
def decryption(code):
    text = decRsaCrt(code, N, D, P, Q)
    return text
    
    
def main():
    # サーバー起動
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"サーバー起動中... ポート {PORT} で待機中")

        # クライアントと通信
        while True:
            conn, addr = s.accept()
            
            # 非同期で1対多通信
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
        
        
if __name__ == "__main__":
    main()
