import jieba

result = jieba.tokenize(u'虽然隔得很远，但还是都属于亚热带季风气候，应该差别不大。')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0], tk[1], tk[2]))
