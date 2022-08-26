# 正则：用来匹配字符串的一门表达式语言
# 测试的方法：https://tool.oschina.net/regex/
# 1.支持普通字符
# 2.元字符：就一个符号来匹配一堆内容
#           \d能够匹配一个数字(0-9)
#           \w能够匹配数字，字母，下划线(0-9,a-z，A-Z，_)
#           \W除了数字，字母，下划线以外的内容
#           \D除了数字以外的内容
#           [abc]匹配a,b,c[^abc]除了a, b,c
#           .除了换行符以外的其他所有内容都可以被匹配
# 3.量词：控制，前面元字符出现的频次
#           +，前面的元字符出现1次或多次,贪婪匹配的,尽可能多的拿到数据
#           *，前面的元字符出现0次或多次，贪婪匹配的.尽可能多的拿到数据
#           ?，前面的元字符出现0次或1次
#           $：匹配行尾，匹配以$之前的字符结束的字符串
#           ^：匹配行首，匹配以^后面的字符开头的字符串
# 4：惰性匹配(重点).*?
#             玩儿吃鸡游戏，晚上一起上游戏,干嘛呢?打游戏啊
#                   玩儿.*?游戏：1
#                           1.玩儿吃鸡游戏
#                           2.玩儿吃鸡游戏，晚上一起上游戏
#                           3.玩儿吃鸡游戏，晚上一起上游戏，干嘛呢?打游戏
#             .*?惰性匹配,匹配到距离xxx最近的内容
#              <div class=“img”><div>小团团</div><div>露脸了</div></div>
#                   <div>.*?</div> :<div>小团团</div>
#                                   <div>露脸了</div>
import re
# findall search finditer
# re.S 匹配所有行
# result=re.findall(r"\d+","今天我花了很多钱，买了100辆梅赛德斯，花费5000w")
# print(result)
# ['100', '500']findall 拿到的是列表

# result=re.search(r"\d+","今天我花了很多钱，买了100辆梅赛德斯，花费5000w")
# print(result)  search拿到第一个结果就返回
# <re.Match object; span=(11, 14), match='100'>
# print(result.group())
# 100

# result=re.finditer(r"\d+","今天我花了很多钱，买了100辆梅赛德斯，花费5000w")
# print(result) #<callable_iterator object at 0x00000148D6AE5A80>
#把所有的结果放在一个迭代器内
# for item in result:
#     print(item.group())
# <re.Match object; span=(11, 14), match='100'> 100
# <re.Match object; span=(22, 25), match='500'> 500

#预加载
# obj=re.compile(r"\d+")
# result=obj.findall("今天我花了很多钱，买了100辆梅赛德斯，花费500w")
# print(result)#['100', '500']


s='''
<div class='acv'>
    <div><a href="baidu.com">我是百度</a></div>
    <div><a href="qq.com">我是腾讯</a></div>
    <div><a href="163.com">我是网易</a></div>
</div>
'''

# obj=re.compile(r'<div><a href=".*?">.*?</a></div>')
# result=obj.finditer(s)
# for item in result:
#     print(item.group())
        # <div><a href="baidu.com">我是百度</a></div>
        # <div><a href="qq.com">我是腾讯</a></div>
        # <div><a href="163.com">我是网易</a></div>

# obj=re.compile(r'<div><a href="(?P<url>.*?)">(?P<txt>.*?)</a></div>')
# result=obj.finditer(s)
# for item in result:
#     url=item.group('url')
#     txt=item.group('txt')
#     print(txt,url)
# 我是百度 baidu.com
# 我是腾讯 qq.com
# 我是网易 163.com

#     print(item.groupdict())
# {'url': 'baidu.com', 'txt': '我是百度'}
# {'url': 'qq.com', 'txt': '我是腾讯'}
# {'url': '163.com', 'txt': '我是网易'}

