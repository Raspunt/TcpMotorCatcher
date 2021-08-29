import socket as sok

host = "0.0.0.0"
port = 5000

with sok.socket(sok.AF_INET, sok.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            

            if data == b"1":
                print("up")
            elif data == b"2":
                print("down")
            elif data == b"3":
                print("left")
            elif data == b"4":
                print("right")

