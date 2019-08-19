precision = 4
base = 10
q = 3453778329090947803

def encode(x_dec):
    return int(x_dec*(base**precision))%q

def decode(x_fp):
    return (x_fp if x_fp <=q/2 else x_fp-q)/(base**precision)
