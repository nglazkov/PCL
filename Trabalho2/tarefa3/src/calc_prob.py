import mmap




'''
DEBUG > 50 -> check prob uni and bi
DEBUG > 10 -> calc_sentence_prob
'''
DEBUG = 0



def calc_sentence_prob(text, n=0):
    '''
    -Recursive!

    -Returns the probability of an input text

    -Input:
        (text) : str; text to calculate the prob
        (n) : int; iteration control for func
    '''

    if DEBUG > 10:
        print('\n\n############  Recursive Iter nº '+str(n)+'  #############\n')
        # print(' Current text:\n\t:::'+str(text)+':::')
        # print(' Current Smooth var:', smoooth)
        # print(' Current nº lines :', line_count)

    if not n:  # n=0 -> 1st iteration ;
        n = n+1
        return calc_word_prob(text[0], text[1]) * calc_sentence_prob(text[1:], n)

    else:  # normal routine -> not 1st nor last iter
        n = n+1
        return calc_word_prob(text[0], text[1]) * calc_sentence_prob(text[1:], n) if len(text) > 1 else 1




def calc_word_prob(w1, w2):
    '''
    -Returns the probability of word 2 happening after word1 -> P(w2|w1) = countbigrams(w1,w2)/ countbigrams(w1)
    '''

    up = int(count_bi(w1, w2))

    down = int(count_uni(w1))

    return up/down




def count_bi(w1, w2):

    global smoooth

    if DEBUG > 10:
        print('\n######### count_bi begginging         ######')

    if smoooth == 0:
        filename = bigrams_cobrem
        with open(filename, 'r') as file:

            for line in file:
                if line.startswith(w1+' '+w2):

                    if DEBUG > 10:
                        print('count_bi(): s0 - found line with unigram:            ""', line, ' ""#')
                        print('######### count_bi end            ######')
                    return int(line.split('\t')[1].split('\n')[0])

    elif smoooth in [1, 2, 3]:
    # elif smoooth == 1 or smoooth == 2 or smoooth == 3:

        filename = bigrams_smooth_cobrem
        # print(filename)

        with open(filename, 'r') as file:

            for line in file:

                if line.startswith(w1+' '+w2):

                    if DEBUG > 10:
                        print('count_bi: s1,s2,s3 - found in line', line+'#')
                        print('######### count_bi end            ######')
                    # print('\n\n\n')
                    # print(line)
                    # print(line.split('\t')[1])
                    # print(int(line.split('\t')[1].split('\n')[0]))
                    # print('\n\n\n')
                    # exit()
                    return int(line.split('\t')[1].split('\n')[0])

        if DEBUG > 10:
            print('count_bi: s1,s2,s3 - default value for bigram is: 1')
            print('######### count_bi end            ######')
        return 1



def count_uni(w1):
    global smoooth

    if DEBUG > 10:
        print('\n######### count_uni begginging         ######')

    if smoooth == 0:
        filename = unigrams_cobrem
        with open(filename, 'r') as file:
            for line in file:

                if line.startswith(w1+' '):
                    if DEBUG > 10:
                        print('count_uni: s0- found line with unigram:             ""', line, ' ""#')
                        print('######### count_uni end         ######')
                    return int(line.split(' ')[1])


    elif smoooth == 1 or smoooth == 3:

        filename = unigrams_smooth_cobrem

        with open(filename, 'r') as file:

            for line in file:

                if line.startswith(w1+' '):
                    if DEBUG > 10:
                        print('count_uni: s1,s3 - found line with unigram:             ""', line, ' ""#')
                        print('######### count_uni end         ######')
                    return int(line.split(' ')[1]) if smoooth == 1 else int(line.split(' ')[1])+1


        if DEBUG > 10:
            print('count_uni: s1/s3 - line not found, default value:', 1)
            print('######### count_uni end             ######')
        return 1 if smoooth == 1 else 2


    elif smoooth == 2:
        filename = unigrams_smooth_cobrem
        with open(filename, 'r') as file:

            for line in file:

                if line.startswith(w1 + ' '):
                    if DEBUG > 10:
                        print('count_uni: s2 - found line with unigram:             ""', line, ' ""#')
                        print('count_uni: s2 - output value is:', int(line.split(' ')[1])+1)
                        print('######### count_uni end         ######')
                    return int(line.split(' ')[1])+1

        if DEBUG > 10:
            print('count_uni: s2 - line not found, default value:', line_count + 1)
            print('######### count_uni end         ######')
        return line_count + 1

    else:
        if DEBUG > 10:
            print('######## count_uni unexpected ending; value 1 !!!!           ######\n')
        raise
        return 1




def check_missing_unigram(text):
    global smoooth
    if DEBUG > 50:
        print('\n##### check_missing_unigram begginging         ######')

    words = list(text)
    filename = unigrams_cobrem


    with open(unigrams_cobrem, 'r') as file:

        lwords = list(words)

        for line in file:

            for word in words:

                if line.startswith(word+' '):
                    if DEBUG > 50:
                        print('3- check_missing_unigram() Found the unigram "' + word +' "')
                        print(lwords)
                    lwords.remove(word)  # remove word, don't search it again


        if not len(lwords):
            smoooth = 0  # 0 -> case where no missing uni-gram

        elif lwords[0] == words[0] or lwords[0] == words[1]:  # check if its missing the 1st word
            smoooth = 2  # 2 -> case where missing the 1st uni-gram
            if DEBUG > 50:
                print('4- check_missing_unigram(): Didnt find beggining word: "' + lwords[0] + '"', lwords)

        # elif len(lwords) > 1:
        else:
            smoooth = 3  # 3 -> case where missing uni-gram
            if DEBUG > 50:
                print('4- check_missing_unigram(): Didnt find end word: "', lwords[0], '"', lwords)


        if DEBUG > 50:
            print('##### check_missing_unigram end , smooth is='+str(smoooth)+';  line_counts='+str(line_count)+'  ######')




def check_missing_bigram(text):
    global smoooth

    if DEBUG > 50:
        print('\n##### check_missing_bigram beginning         ######')
    # print('      check_missing_bigram: smoothing is :', smoooth)


    if smoooth == 0:

        bigrams = [(text[i], text[i+1]) for i in range(len(text)-1)]


        i = 0

        with open(bigrams_cobrem, 'r') as file:

            for line in file:
                for bigram in bigrams:

                    if line.startswith(bigram[0]+' '+bigram[1]+'\t'):
                        i = i + 1
                        if DEBUG > 50:
                            print('check_missing_bigram: Found the bigram "', str(bigram), '" in line:', line+'#')

        smoooth = 0 if i > 1 else 1  # 1 -> case where missing bi-gram

    else:
        # print('# check_missing_bigram: smooth was already > 0 ; i.e. active ')
        pass

    if DEBUG > 50:
        print('##### check_missing_bigram end , smooth is='+str(smoooth)+';  line_counts='+str(line_count)+'  ######')



def check_prob_style(text):
    check_missing_unigram(text)
    check_missing_bigram(text)
    if DEBUG > 50:
        print('\n##### Checking done, smooth is :', smoooth)
        print('\n\n')


print('\n#####################################################')
print('#####################################################\n')





DEBUG = 0
teext = 'niko cobrir cobrar'


unigrams_cobrem='./ngrams/uningrams_cobrem.txt'
bigrams_cobrem='./ngrams/bingrams_cobrem.txt'
unigrams_smooth_cobrem='./ngrams/uni_smooth_ngrams_cobrem.txt'
bigrams_smooth_cobrem='./ngrams/bi_smooth_ngrams_cobrem.txt'
'''
smoooth=0 -> normal prob calculation
smoooth=1 -> use smoothing to calculate the probs
smoooth=2 -> unigram doesnt exist in the 1st word
smoooth=3 -> unigram doesnt exist sin the last word
'''
smoooth = 0


def mapcount(filename):
    f = open(filename, "r+")
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    return lines
line_count = mapcount(unigrams_cobrem)



def print_prob(text, f1,f2,f3,f4,l):
    global teext
    teext=text
    teext = teext.split(' ')#\n  # split text worb by word
    # print('TEXT IS:', teext)

    global unigrams_cobrem,bigrams_cobrem,unigrams_smooth_cobrem,bigrams_smooth_cobrem
    unigrams_cobrem, bigrams_cobrem, unigrams_smooth_cobrem, bigrams_smooth_cobrem= f1, f2, f3, f4

    global line_count
    line_count=l

    check_prob_style(teext)  # change smooth var accordingly to sentence type
    # print('\n#\n# Calling Recursive func:\n#')
    # print('# probability is : ', calc_sentence_prob(teext),'#\n#')
    return calc_sentence_prob(teext)
    # print('#\n# Main: smooth is: ', smoooth)
    # print('#\n#\n# THE END')
    # print('#')



# TESTS!!
# with open('test.txt', 'r') as file:
#
#     for line in file:
#
#         line = line.split('#')
#         teext = line[0].split(' ')  # split text worb by word
#
#         check_prob_style(teext)  # change smooth var accordingly to sentence type
#
#
#         # if smoooth == 2:
#         # print('\n#\n# Calling Recursive func:')
#
#         if str(calc_sentence_prob(teext))[0:4] != line[1][0:4]:
#
#             print('# Line:\t', line[0])
#             print(calc_sentence_prob(teext), '\t\t\t', line[1])
#             print('# smooth is: ', smoooth)
#             print()
#             print('#####################################################\n\n')
#             print('#####################################################\n\n')
#
#
#     print('\n\n###############       THE END        ################\n\n')
#


#