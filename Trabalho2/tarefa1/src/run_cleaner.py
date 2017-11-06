import sys

from cleaner import cleaner

DEBUG=0

def run_cleaner(ifilename,ofilename,special_word):

    print('#\n#')
    print('#\n# Input File (.out) to clean:', ifilename)

    cleaned_fname=ofilename

    print('#\n# Output File (.out) to clean:', cleaned_fname)
    print('#\n# Word to replace, etc. :', special_word)

    print('# Opening File...#\n#\n#')


    with open(ifilename, 'r') as infile, \
         open(cleaned_fname, 'w') as outfile:

        sentenceCounter=0

        for line in infile:

            if DEBUG>0:
                    print('#\n# Sentence nº',sentenceCounter,':')

            # try:
            cleaned = cleaner(line,special_word)
            # print(len(cleaned))
            # print(cleaned)
            # print()

            # verification if all sentences at least have THE word

            if cleaned[0] == None:

                if DEBUG>0:
                    print('#\n    ', cleaned[1])


            elif cleaned[0]:

                if DEBUG>0:
                    print('#\n# Cleaned')

                outfile.write(cleaned[1])
                outfile.write('\n')


            # except:
            #
            #     print('#\n# UNKOWN ERROR')
            #     print('#\n# Nº',sentenceCounter)
            #     print('#\n# Sentence:\n\n',cleaned[1])

            if DEBUG>0:
                print('#\n#\n#')
            sentenceCounter+=1


if __name__ == "__main__":

        ifilename,ofilename,special_word=sys.argv[1:]

        run_cleaner(ifilename,ofilename,special_word)




        #
