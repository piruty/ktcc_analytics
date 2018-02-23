#! /usr/bin/env python3
# coding: utf-8

import MeCab
import unicodedata


mt = MeCab.Tagger('-Ochasen')

lyrics = []
for lyric in open('lyrics.txt'):
    tmp_list = []
    lyric = unicodedata.normalize('NFKC', str(lyric))
    node = mt.parseToNode(lyric)
    while node:
        if node.feature.startswith('名詞') or node.feature.startswith('動詞') or node.feature.startswith('形容詞'):
            tmp_list.append(node.surface)
        node = node.next
    lyrics.append(' '.join(tmp_list))

with open('wakati_lyrics.txt', 'w') as f:
    for lyric in lyrics:
        f.write(lyric + '\n')

