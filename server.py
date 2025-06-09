# server.py
import socket

HOST = '0.0.0.0'  # 全てのインターフェースで待ち受け
PORT = 12345      # 使用するポート番号

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"サーバー起動中... ポート {PORT} で待機中")
    
    conn, addr = s.accept()
    with conn:
        print(f"{addr} と接続されました")
        while True:
            data = conn.recv(1024)  # データを受信（最大1024バイト）
            if not data:
                break
            print("受信:", data.decode())
            response = "受信しました: " + data.decode()
            conn.sendall(response.encode())
