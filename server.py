# server.py
import socket
import threading
from rsa import *

HOST = '0.0.0.0'  # 全てのインターフェースで待ち受け
PORT = 12345      # 使用するポート番号

# 秘密鍵
P = 997
Q = 859

N = P * Q
PHI = (P - 1) * (Q - 1)
E = 65537
D = modinv(E, PHI)

# 秘密鍵(RSA-CRTで拡張したもの)
DP = D % (P - 1)
DQ = D % (Q - 1)
QINV = modinv(Q, P)

def handle_client(conn, addr):
    print(f"{addr} と接続されました")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode()
            print(f"{addr} から受信(暗号): {data}")
            data_list = data.split('-')
            dec_data = ''
            for i in range(4):
                if i == 3:
                    dec_data = dec_data + str(decryption(int(data_list[i])))
                else:
                    dec_data = dec_data + str(decryption(int(data_list[i]))) + '-'
            print(f"{addr} から受信(平文): {dec_data}\n")
            
            if data == "exit":
                break
            response = "受信しました: " + dec_data
            conn.sendall(response.encode())
    print(f"{addr} との接続を終了しました")

def decryption(code):
    text = ""
    text = decRsaCRT(code,N,P,Q,DP,DQ,QINV)
    return text
    
    
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"サーバー起動中... ポート {PORT} で待機中")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
        
        
if __name__ == "__main__":
    main()