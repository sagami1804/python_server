# client.py
import socket
from rsa import *

SERVER_IP = '10.0.70.204'
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
        
        print(f"n = {n}, e = {e}")
        print("接続しました。メッセージを送信してください")
        
        while True:
            msg = input(f"4桁の数字を-で区切って入力して下さい（終了するには空Enter）: ")
            
            # 空Enterで停止
            if str(msg) == "":
                break

            # 入力した文字列をハイフンで4分割
            msg = msg.split('-')
            enc_msg = ''
            count = 0
            
            # 4桁ずつ暗号化
            for numbers in msg:
                if count == 3:
                    enc_msg = enc_msg + str(encryption(int(numbers),n,e))
                else:
                    enc_msg = enc_msg + str(encryption(int(numbers),n,e)) + '-'
                count = count + 1

            print("暗号:"+str(enc_msg))
            
            # サーバーに送信
            s.sendall(enc_msg.encode())
            
            # サーバーから受信(デバッグ)
            data = s.recv(1024)
            print("サーバーからの返信:", data.decode(),"\n")
        
        
if __name__ == "__main__":
    main()
