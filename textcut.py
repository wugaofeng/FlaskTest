# -*- coding: utf-8 -*-
import jieba
import jieba.analyse
import jieba.posseg as pseg

#分词
def extract_tags(content):
    return '/'.join(jieba.cut(content))

#关键词权重集合
def extract_tags_with_weight(content,topK):
    tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
    return tags

#词性分词集合
def extract_tags_with_pseg(content):
    tags = pseg.cut(content)
    return tags

#关键词权重字符串
def extract_tags_with_weight_str(content, topK):
    tags = extract_tags_with_weight(content, topK)
    ret = ''
    for tag in tags:
        ret +=''.join("关键词: %s\t\t 权重: %f  \n" % (tag[0], tag[1]))
        #print(tag[0],tag[1])
    return ret

#词性分词字符串
def extract_tags_with_pseg_str(content):
    tags = extract_tags_with_pseg(content)
    ret = ''
    for word, flag in tags:
        ret +=''.join("%s %s \n" % (word, flag))
    return ret
