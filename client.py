# client.py
import socket
from rsa import *

SERVER_IP = '10.0.3.85'
PORT = 12345
# 秘密鍵
P = 997
Q = 859
N = P * Q
E = 65537

def encryption(text):
    code = ""
    code = encRsaCrt(int(text),N,E)
    return code

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.connect((SERVER_IP, PORT))
        print("接続しました。メッセージを送信してください")
        
        while True:
            msg = input("送信文字列（終了するには空Enter）: ")
            msg = encryption(int(msg))
            print("暗号:"+str(msg))
            if str(msg) == "":
                break
            if str(msg) == "exit":
                break
            s.sendall(str(msg).encode())
            data = s.recv(1024)
            print("サーバーからの返信:", data.decode())
        
        
if __name__ == "__main__":
    main()
