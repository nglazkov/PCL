from collections import Counter #count repeates words
import re

'''
DEBUG VAR:
     0 : NO PRINTS
     1 : PRINT to debug
'''
DEBUG = -1

def cleaner(line,special_word):
    '''
    Input: text to clean(string) , repalcement word(string)

    Output:
        1: Depending on the code initial code act accordingly:
            ? -> duvidas ; eliminar
            # -> erro ;
            n-é-verbo -> apagar

        2: Delete lines where the special word occurs twice

        3: Replace the special word by the lema in the begg of each line

        4: Remove the lema/anotations at the beggining of each line
    '''

    #split the anottaion  and sentence
    line=line.split('\t')


    #bad annotation marks
    bad_anotations=['?','#','n-é-verbo']


    #slit the anotations
    anotations=line[0]
    if DEBUG>0:
        print('FULL Anotation:',anotations)


    #replace '.' or '?' followed with line break by </s>
    # sentence=line[1:][0].replace('.\n','').replace('?\n','')
    sentence=line[1:][0].replace('\n','')
    if DEBUG>0:
        print('\nCorrected Sentence:',sentence+'\n\n')


    good_sentence = False
    sub_verb=0
    #check for bad annotations
    for bad_anotation in bad_anotations:

        if DEBUG>0:
            print('Bad Anotation: ',bad_anotation)
        good_sentence = True if bad_anotation in anotations else False

        if good_sentence:
            break
        if DEBUG > 0:
            print('GOOD?', good_sentence, '\n')

    if DEBUG>0:
        print('1-PASSED in (wrong or doubt or not_verb) ?', good_sentence, '\n')
    # return sentence if not bad else None


    if not good_sentence:

        if DEBUG>0:
            print('\n\n2-COUNT WORDS:\n\nSPECIAL WORD', special_word, '\n')


        words = sentence.split()
        word_count = Counter(words)


        if DEBUG > 0:
            print('Number of special words:', word_count[special_word])
        good_sentence=True if word_count[special_word] > 1 else False


        if not good_sentence:
            if DEBUG > 0:
                print('\n\n3-REPLACE:\n\nANOTATION', anotations, '\n')

            sub_verb = None
            for bad_anotation in bad_anotations:
                sub_verb = anotations.replace(bad_anotation, '')



    if not good_sentence:
        sentence = sentence.replace(special_word.title(), sub_verb)
        return [True, sentence.replace(special_word, sub_verb)]

    else:
        return [None, line]


#print('Result:',cleaner('cobrir	Cinco das mais importantes cadeias televisivas norte-americano cobrem o acontecimento .\n','cobrem'),'\n')




##

###

####
