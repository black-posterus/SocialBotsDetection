# coding=utf-8            设定编码形式
import  re                #包含正则表达式
import codecs
dict = {}
z = re.compile(u'[\u4e00-\u9fa5]+')#将所有的中文字符全部都包含里面
with open('../中科院分词/result.txt', 'rb') as f:#自己的文件可以根据自己的具体需要更改路径
    mylist=f.readlines()
    for row in mylist:
        row= row.strip().decode('utf-8')
        row.strip(' ')#这里可以更改为其他的条件，比如说逗号或者其他的，根据自己语料库的需要设置即可
        i = z.findall(row)            #Z1统计单字，Z4表示统计四字高频
        for j in i:  
            if (j in dict):
                dict[j] += 1
            else:
                dict[j] = 1
dict = sorted(dict.items(), key=lambda d: d[1],reverse=True)       #安装value排序
with open('result.txt', 'w',encoding='utf-8') as f:
    for a, b in dict:                                                  #a是中文，b是词出现的次数
        if b > 0:
             #print(a,b)
            f.write(a + "," + str(b) + "\n")
