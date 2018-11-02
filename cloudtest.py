# -*- coding: utf-8 -*-
from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

frequencies = {u'分词': 1.4044143689520001, u'并行': 0.6881888228344001, u'数据量': 0.500575331636, u'jieba': 0.47819070011599996, u'python': 0.47819070011599996, u'multiprocessing': 0.47819070011599996, u'Windows': 0.47819070011599996, u'支持': 0.4061623762224, u'自带': 0.3860872963972, u'模块': 0.3583614091748, u'文本': 0.35779402377479996, u'开启': 0.3110397704432, u'效率': 0.2748281896108, u'基于': 0.2650756533652, u'必要': 0.24049372604959998, u'注意': 0.2134106355316, u'环境': 0.2072805633972, u'非常': 0.1961313202536, u'提高': 0.1893673871912, u'为了': 0.18427294719079998, u'时候': 0.17154985333759998,}
wordcloud = WordCloud(font_path="C:\Windows\Fonts\msyhbd.ttc",
                      width=800,
                      height=600,
                      max_words=1000,
                      background_color='white').fit_words(frequencies)

wordcloud.to_file(".\\static\\tmp\\out2.jpg")
