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
    code = encRsaCrt(text,N,E)
    return code

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.connect((SERVER_IP, PORT))
        print("接続しました。メッセージを送信してください")
        
        while True:
            msg = input(f"4桁の数字を-で区切って入力して下さい（終了するには空Enter）: ")
            msg = msg.split('-')
            enc_msg = ''
            count = 0
            for numbers in msg:
                if count == 3:
                    enc_msg = enc_msg + str(encryption(int(numbers)))
                else:
                    enc_msg = enc_msg + str(encryption(int(numbers))) + '-'
                count = count + 1

            print("暗号:"+str(enc_msg))
            if str(msg) == "":
                break
            if str(msg) == "exit":
                break
            s.sendall(enc_msg.encode())
            data = s.recv(1024)
            print("サーバーからの返信:", data.decode())
        
        
if __name__ == "__main__":
    main()
