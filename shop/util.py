
def normalize(name):
    return name.strip()

def discount(total):
    if total > 150:
        return total * 0.9
    return total

def parse(text):
    return int(text)
