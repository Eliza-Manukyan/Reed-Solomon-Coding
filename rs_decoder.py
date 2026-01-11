from reedsolo import RSCodec, ReedSolomonError

class RSDecoder:
    def __init__(self, n=15, k=11):
        self.parity = n - k
        self.rs = RSCodec(self.parity)

    def decode(self, received_block):
        try:
            decoded, _, _ = self.rs.decode(bytes(received_block))
            return list(decoded), True
        except ReedSolomonError:
            return None, False