# Kick The Can Crew Lyric Analytics

----

## What is This?

Kick the can crew(ktcc)の歌詞を取得し、分かち書きすることで解析するための情報を生成するためのものです。

## Script file Description

### get_lyrics.py

歌詞掲載サイトからktccの歌詞を取得する。
取得された歌詞は「lyrics.txt」というテキストファイルに1行1曲で書き込まれる。

### make_wakati_data.py

lyrics.txtに保存された歌詞情報を分かち書きして保存し直す。
分かち書きされた歌詞は「wakati_lyrics.txt」というテキストファイルに1行1曲で書き込まれる。

## Next todo

gensim(word2vec)を使ったスクリプトを追加する
Word Cloudもやってみたい

## Reference

[「OK word2vec ! "マジ卍"の意味を教えて」 Twitterデータからword2vec実践してみた](http://www.randpy.tokyo/entry/python_word2vec)

## Licence

MIT

## Author

[piruty](https://piruty.com)
