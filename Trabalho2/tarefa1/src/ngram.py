import nltk,sys
from collections import Counter

DEBUG=0



def n_gram(text, n, smoothed):

    n=int(n)

    if DEBUG>0:
        print('#\n# NGRAMMIN')
        # print('#\n# TEXT:\n\n',text)

    token = nltk.word_tokenize(text)

    from nltk.util import ngrams
    ngrams = ngrams(token, 1, pad_left=True, pad_right=True, left_pad_symbol='<s>', right_pad_symbol='</s>') if n == 1 \
        else ngrams(token, 2, pad_left=True, pad_right=True, left_pad_symbol='<s>', right_pad_symbol='</s>')

    if DEBUG>0:
        print('#\n#'+str(n)+'-GRAMS:\n')

    counts=dict(Counter(ngrams))


    if DEBUG > 0:
        print('len of counts.value=',len(counts))

    return counts
