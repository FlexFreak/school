import hashlib

def ver(str):
    str = str.encode('utf-8')
    enc = hashlib.md5(str).hexdigest()
    print(enc)

ver('aödsfkajsödflkjasödflkjaösdlkfjöasldkfjasöldfkjö')