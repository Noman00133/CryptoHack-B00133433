string = "label"
flag = ''

for label1 in string:
    flag += chr(ord(label1) ^ 13)

print('crypto{{{}}}'.format(flag))