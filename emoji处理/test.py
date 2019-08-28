import re

"""
@描述           根据传入的content，判断是否是emoji字符。
@return         True是emoji，False不是True是emoji。
正则表达式存在问题，目前未修复，匹配范围过小
"""


def isEmoji(content):
    if not content:
        return False
    if (re.search('[\U00010000-\U0010ffff]', str(content)) != None):
        return True
    elif (re.search('[\uD800-\uDBFF]', str(content)) != None):
        return True
    elif (re.search('[\uDC00-\uDFFF]', str(content)) != None):
        return True
    else:
        return False


path = '../中科院分词/result.txt'
result = 'result.txt'
f = open(result, 'a', encoding='utf-8')
file = open(path, "r", encoding='utf-8', errors="ignore")
while True:
    myarr = file.readline()
    arr = myarr.encode(' utf-8')
    f.write(str(isEmoji(str(arr))) + '\n')
f.close()
