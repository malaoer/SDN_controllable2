


def convert( strIP):
    ip_list = strIP.split('.')
    lst = []
    for i in ip_list:
        two = bin(int(i, 10)).lstrip("0b")
        lst.append(two.zfill(8))
    return " ".join(lst)

ip1 = convert('192.168.64.0')
ip2 = convert('192.168.69.0')
print(ip1)
print(ip2)
