#!/usr/bin/env python
# -*- coding: utf-8 -*-

word1en = "6in"
word1ar = "طين"
count1 = 7

word2en = "tin"
word2ar = "تين"
count2 = 7

md_file = open("""{0}-{1}.md""".format(word1en, word2en), 'w')

md_file.write("""---
title: {0} - {1}
layout: problem

words:
""".format(word1ar, word2ar))

def md_words_writer(wordxen, wordxar, countx):
    md_file.write("""  - spelling: "{0}"
    pronounciations:
""".format(wordxar))
    i = 1
    while i <= countx:
        md_file.write("""      - file: "{0}/{0}-{1}.mp3"
""".format(wordxen, i))
        i = i + 1
md_words_writer(word1en, word1ar, count1)
md_words_writer(word2en, word2ar, count2)

md_file.write("""---""")

md_file.close()
