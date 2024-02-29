def reverse_sentence_words(sentence):
    # 此处写你的代码
    L=sentence.split()
    print(L)
    L1=L[::-1]
    s='.'.join(L1)
    str=s.replace('.',' ')
    return str
# 获取输入
sentence = input()
# 调用函数并打印结果
print(reverse_sentence_words(sentence))