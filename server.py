# server.py
import socket
import threading

HOST = '0.0.0.0'  # 全てのインターフェースで待ち受け
PORT = 12345      # 使用するポート番号

def handle_client(conn, addr):
    print(f"{addr} と接続されました")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"{addr} から受信: {data.decode()}")
            
            if data.decode() == "exit":
                break 
            response = "受信しました: " + data.decode()
            conn.sendall(response.encode())
    print(f"{addr} との接続を終了しました")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"サーバー起動中... ポート {PORT} で待機中")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()