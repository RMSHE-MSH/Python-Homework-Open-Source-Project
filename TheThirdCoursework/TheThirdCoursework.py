# WordFrequencyCount - TheThirdCoursework;
# Powered by RMSHE / 2022.10.27.Mark0;
# OpenSource:
import jieba
from tabulate import tabulate

# 文件路径;
FilePath = "./2015&2019英语四级真题.txt"
# 需要排除的单词(不分大小写);
Exclude = [
    "a", "the", "are", "and", "or", "not", "is", "was", "has", "from", "rmshe", "we", "me", "who", "you", "that", "than", "for", "in", "on", "this", "one",
    "but", "use", "all", "one", "what", "hear", "its", "his", "when", "here", "end", "were", "way", "cow", "too", "good", "had", "car", "your"]


# 判断目标单词"_word"是否在排除列表"exclude"中;
def isExclude(_word, exclude=()):
    for exc in exclude:
        if exc == _word or exc.capitalize() == _word:
            return True


# 英文词频统计(filePath = 文件路径, lengthThreshold = 单词长度阈值, frequencyThreshold = 单词频率阈值, exclude = 排除的单词列表(不分大小写));
def WordFrequencyCount(filePath: str, lengthThreshold: int = 1, frequencyThreshold: int = 1, exclude=()):
    with open(filePath, encoding='utf-8') as file:
        wordsList = jieba.lcut(file.read())  # 将文件读取到列表;

    count = {}
    for word in wordsList:
        # 首字母转为大写;
        word = word.capitalize()
        # 排除长度小于等于"threshold"的单词,排除中文词语,排除常见单词,排除非字母字符;
        if not (len(word) <= lengthThreshold or '\u4e00' <= word <= '\u9fff' or isExclude(word, exclude) or not word.isalpha()):
            count[word] = count.get(word, 0) + 1  # 统计词频

    # 将字典中的键值对转化为列表后按照词频从大到小排列;
    countList = list(count.items())
    countList.sort(key=lambda x: x[1], reverse=True)

    countList2 = [('KeyWord', 'Frequency')]
    for i in range(len(countList)):
        # 排除词频达不到"frequencyThreshold"的单词;
        if countList[i][1] >= frequencyThreshold:
            countList2.append(countList[i])

    return countList2


print(tabulate(WordFrequencyCount(FilePath, 4, 4, Exclude), headers='firstrow', tablefmt='fancy_grid', showindex=True))
