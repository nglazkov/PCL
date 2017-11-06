import sys
import mmap
from ngram import n_gram
from collections import defaultdict

DEBUG=0



def testoutfile(ifilename,ofilename):

    #nlines=mapcount(ifilename)
    print('\n\n\nInput File (.out) to clean:', ifilename)
    #print('# With',nlines,'nº of lines')

    line_count = mapcount(ifilename)

    print('\n\nOutput Files, ngrams:\n#')

    unigram_fname='../tarefa1/ngrams/uni'+ofilename+'.txt'
    bnigram_fname='../tarefa1/ngrams/bi'+ofilename+'.txt'
    unigram_smooth_fname='../tarefa1/ngrams/uni_smooth_'+ofilename+'.txt'
    bnigram_smooth_fname='../tarefa1/ngrams/bi_smooth_'+ofilename+'.txt'

    print('Unigram file: ', unigram_fname)
    print('Bigram file: ', bnigram_fname)
    print('Unigram Smooth file: ', unigram_smooth_fname)
    print('Bigram Smooth file: ', bnigram_smooth_fname)
    print('\n')

    with open(ifilename, 'r') as ifile,                  \
    open(unigram_fname, 'w') as uni_file,                 \
    open(bnigram_fname, 'w') as bi_file,                   \
    open(unigram_smooth_fname, 'w') as uni_smooth_file,     \
    open(bnigram_smooth_fname, 'w') as bi_smooth_file:

        dict_ngrams, dict_bigrams=dict(), dict()
        dict_ngrams_smoothed,dict_bigrams_smoothed=dict(), dict()

        for line in ifile:

            # get ngrams for this sentence
            ngrams = n_gram(line, 1, False)
            # group with the previous
            dict_ngrams = dsum(dict_ngrams, ngrams)

            # get ngrams for this sentence
            ngrams = n_gram(line, 2, False)
            # group with the previous
            dict_bigrams = dsum(dict_bigrams, ngrams)

            # get smoothed ngrams for this sentence
            ngrams = n_gram(line, 1, True)
            # group with the previous
            dict_ngrams_smoothed = dsum(dict_ngrams_smoothed, ngrams)

            # get smoothed ngrams for this sentence
            ngrams = n_gram(line, 2, True)
            # group with the previous
            dict_bigrams_smoothed = dsum(dict_bigrams_smoothed, ngrams)

            # print('#\n#\n#')


        # #  sad bcs nltk doesnt add the beg and end taggs to counts :(
        # dict_ngrams['<s>'] = line_count
        # dict_ngrams['</s>'] = line_count


        #NORMAL

        for key, value in dict_ngrams.items():
            if DEBUG > 0:
                print(str(key[0])+' '+str(value))
            uni_file.write(str(key[0])+' '+str(value)+'\n')
        uni_file.write('<s>' + ' ' + str(line_count) + '\n')         #hammered bcs python wont add stange/long keys (e.g. </s>)
        uni_file.write('</s>' + ' ' + str(line_count) + '\n')        #hammered bcs python wont add stange/long keys (e.g. </s>)
        print('UNIGRAMS done')

        for key, value in dict_bigrams.items():
            if DEBUG>0:
                print(str(key[0])+' '+str(key[1])+'\t'+str(value))
            bi_file.write(str(key[0])+' '+str(key[1])+'\t'+str(value)+'\n')
        print('BIGRAMS done')


        #SMOOTHED

        for key, value in dict_ngrams_smoothed.items():
            if DEBUG>0:
                print(str(key[0])+' '+str(value))
            uni_smooth_file.write(str(key[0])+' '+str(value+len(dict_ngrams)+2)+'\n')
        uni_smooth_file.write('<s>' + ' ' + str(line_count+len(dict_ngrams)+2) + '\n')         #hammered bcs python wont add stange/long keys (e.g. </s>)
        uni_smooth_file.write('</s>' + ' ' + str(line_count+len(dict_ngrams)+2) + '\n')        #hammered bcs python wont add stange/long keys (e.g. </s>)
        print('UNIGRAMS SMOOTHED done')


        for key, value in dict_bigrams_smoothed.items():
            if DEBUG>0:
                print(str(key[0])+' '+str(key[1])+'\t'+str(value))
            bi_smooth_file.write(str(key[0])+' '+str(key[1])+'\t'+str(value+1)+'\n')
        print('BIGRAMS SMOOTHED done')

        print('\n\nNGRAMS END \n#\n\n')





def dsum(*dicts):
    '''
    From stackoverflow, joins and sums values of dicts
    '''

    ret = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    return dict(ret)


def mapcount(filename):
    f = open(filename, "r+")
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    return lines


if __name__ == "__main__":

    ifilename, ofilename=sys.argv[1:]

    testoutfile(ifilename, ofilename)









#
