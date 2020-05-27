#!/usr/bin/env python
# coding: utf-8


from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec


glove_file = datapath('/Users/jacke/Desktop/glove.6B.100d.txt')
tmp_file = get_tmpfile("test_word2vec.txt")
_ = glove2word2vec(glove_file, tmp_file)
model = KeyedVectors.load_word2vec_format(tmp_file)


# Calculate similarity of two words

model.similarity('pasta', 'spaghetti')


# Find similary words

model.similar_by_word('airplane')




