from reedsolo import RSCodec

class RSEncoder:
    def __init__(self, n=15, k=11):
        self.n = n
        self.k = k
        self.parity = n - k
        self.rs = RSCodec(self.parity)

    def encode(self, data_block):
        data_bytes = bytes(data_block)
        encoded = self.rs.encode(data_bytes)
        return list(encoded)