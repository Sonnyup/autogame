import hashlib

def get_file_md5():
    f = open('config.ini','rb')
    m = hashlib.md5()
    while True:
        #如果不用二进制打开文件，则需要先编码
        #data = f.read(1024).encode('utf-8')
        data = f.read(1024)  #将文件分块读取
        if not data:
            break
        m.update(data)
    return m.hexdigest()
