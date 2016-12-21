# coding=utf-8
import fileinput
#文件内容liudehua替换AAAA,并且备份一个新的文件后缀为_bak
for line in fileinput.input("contact.txt", backup='_bak', inplace=1):
    line = line.replace("liudehua", "AAAA")
    print line,


'''
#修改某行
with open("contact.txt"."r+") as f:
    old = f.read()
    f.seek(5)
    f.write("new line\n" + old)
line before
   '''