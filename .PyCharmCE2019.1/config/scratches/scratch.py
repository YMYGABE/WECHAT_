import jieba
import jieba.analyse
excludes = {"宝玉","贾母","凤姐","王夫人","奶奶"}
data = "C:\\Users\\user\\Desktop\\hlm.txt"
def getText():
    txt = open(data,"r",encoding = 'utf-8').read()
    for ch in '!?""(),.:''[]@#$%^&*(_+=':
        txt = txt .replace(ch," ")
        return txt

hlmText = getText()
word = jieba.lcut(hlmText)
counts = {}
for word in word:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
