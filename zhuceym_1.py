__author__ = 'Administrator'
#写一个具体的程序，完成以下功能：假设老师想注册一个很酷的6位以内英文字母并以.com结尾的域名（如expert.com、fox.com），
# 那么请你设计一个程序，从这个网站（http://www.zgsj.com/domain_reg/
#  这个老师测过可以，但大家也可以找其他的）自动测试所有可能的这样的6位以内英文字母的域名，
# 记录未被其他用户注册的域名（已经被注册的自然是忽略掉了）
import urllib2
import urllib
import re

yw = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
ym = []
res = []

for y1 in yw:
    ym.append(y1)
    for y2 in yw:
        ym.append(y1+y2)
        for y3 in yw:
            ym.append(y1+y2+y3)
            for y4 in yw:
                ym.append(y1+y2+y3+y4)
                for y5 in yw:
                   ym.append(y1+y2+y3+y4+y5)

filename = "zhuceym.txt"
jilu = file(filename,'w')

wz = 'http://www.zgsj.com/domain_reg/domaintrans.asp'
for item in ym:

    values={'name':"%s.com"}
    data = urllib.urlencode(values)#蒋values编码为urllib能理解的格式


    request = urllib2.Request(wz,data)#指定一个域名并发送请求
    response = urllib2.urlopen(request)#服务端响应来自客户端的请求
    the_page = response.read()


    if re.findall( r"value='([a-zA-Z]+\.com)' checked",the_page):#获取字符串中，包含'a-z或A-Z'的所有单词
        jilu.write(str(re.findall(r"value='([a-zA-Z]+\.com)' checked",the_page)))
        jilu.write(' ')
        res.append(re.findall(r"value='([a-zA-Z]+\.com)' checked",the_page))
    else:
        pass

jilu.close()

