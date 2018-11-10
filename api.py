import socket


class API():
    """
    This class is API interface, which is listening everything on port 5554,
    With function worker, which is returning connection information
    """

    def __init__(self):
        """
        Initialize API, opens socket to listen everything on 5554 up to 10 clients.
        Auto called, when created new API-class object.
        """
        self.sock = socket.socket()
        self.sock.bind(('0.0.0.0', 5554))
        self.sock.listen(10)


    def worker(self):
        """
        This function is API worker, which is trying to accept data from socket.
        If nothing to receive - returns False.
        If it received data - returns it.
        """
        conn, addr = self.sock.accept()
        if conn:
            data = conn.recv(2048)
            if not data:
                return False
            return data