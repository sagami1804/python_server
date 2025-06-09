# client.py
import socket
import rsa

SERVER_IP = '10.0.3.85'
PORT = 12345

def encryption(text):
    code = ""
    return code

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        print("接続しました。メッセージを送信してください")
        
        while True:
            msg = input("送信文字列（終了するには空Enter）: ")
            msg = encryption(msg)
            print("暗号:"+msg)
            if msg == "":
                break
            if msg == "exit":
                break
            s.sendall(msg.encode())
            data = s.recv(1024)
            print("サーバーからの返信:", data.decode())
        
        
if __name__ == "__main__":
    main()
