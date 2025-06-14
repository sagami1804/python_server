# client.py
import socket
from rsa import *

SERVER_IP = '172.23.25.106'
PORT = 12345

# 暗号化
def encryption(text,n,e):
    code = encRsaCrt(text,n,e)
    return code

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        # サーバーに接続
        s.connect((SERVER_IP, PORT))
        
        # 公開鍵を受信
        key_data = s.recv(1024)
        keys = key_data.decode().split(",")
        n = int(keys[0])
        e = int(keys[1])
        
        print(f"n = {n}, e = {e}\n")
        print("接続しました。メッセージを送信してください")
        
        while True:
            msg = input(f"4桁の数字を-で区切って入力して下さい（終了するには空Enter）: ")
            
            # 空Enterで停止
            if str(msg) == "":
                break

            enc_msg = str(encryption(int(msg.replace('-', '')),n,e))
            print("\n暗号:"+enc_msg+"\n")
            
            # サーバーに送信
            s.sendall(enc_msg.encode())
            
            # サーバーから受信(デバッグ)
            data = s.recv(1024)
            print("\nサーバーからの返信:", data.decode(),"\n")
        
        
if __name__ == "__main__":
    main()
