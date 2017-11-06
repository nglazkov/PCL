import re
import io
import sys
import calc_prob as Calc_prob
import mmap

DEBUG=0
def parse_sentence(file_frases, file_param, file_unig, file_big, file_unig_smoo, file_big_smoo):

    f = io.open(file_frases, mode="r+", encoding="utf-8")
    with open(file_param) as f1:
        content = f1.readlines()

    content = [x.strip() for x in content]
    # ['viram', 'ver', 'virar'] ou ['cobrem', 'cobrir', 'cobrar']
    content = content + [content[0].title()] + [content[1].title()] + [content[2].title()]
    # [(0)'viram', (1)'ver', (2)'virar', (3)'Viram', (4)'Ver', (5)'Virar'] ou [(0)'cobrem', (1)'cobrir', (2)'cobrar', (3)'Cobrem', (4)'Cobrir', (5)'Cobrar']

    results=[]

    for line in f:
        print('Linha: ', line)
        if DEBUG>10:
            print(line.rstrip() + ":")
        word_list = line.split()
        line = line.rstrip()
        splitedline = line.split()


        if (len(splitedline) == 1):

            if (splitedline[0] == content[0]): # Ve se é "viram" ou "cobrem"
                # Calc_prob.print_prob("<s> " + content[1] + " </s>", file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                # Calc_prob.print_prob("<s> " + content[2] + " </s>", file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                a=Calc_prob.print_prob("<s> " + content[1] + " </s>", file_unig, file_big,file_unig_smoo, file_big_smoo,line_count_unigrams)
                b=Calc_prob.print_prob("<s> " + content[2] + " </s>", file_unig, file_big,file_unig_smoo, file_big_smoo,line_count_unigrams)
                if max(a, b) == a:
                    results.append([line, [content[1], a], [content[2], b],'Lema mais provável:'+content[1]])
                elif max(a, b) == b:
                    results.append([line, [content[1], a], [content[2], b],'Lema mais provável:'+ content[2]])
                else:
                    results.append([line, [content[1], a], [content[2], b],'Lema mais provável:'+ ' equal prob'])
                break

            elif (splitedline[0] == content[3]): # Ve se é "Viram" ou "Cobrem"
                # Calc_prob.print_prob("<s> " + content[5] + " </s>", file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                # Calc_prob.print_prob("<s> " + content[4] + " </s>", file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                a=Calc_prob.print_prob("<s> " + content[4] + " </s>", file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                b=Calc_prob.print_prob("<s> " + content[5] + " </s>", file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                if max(a, b) == a:
                    results.append([line, [content[4], a], [content[5], b],'Lema mais provável:'+ content[4]])
                elif max(a, b) == b:
                    results.append([line, [content[4], a], [content[5], b],'Lema mais provável:'+ content[5]])
                else:
                    results.append([line, [content[4], a], [content[5], b],'Lema mais provável:'+ ' equal prob'])
                break


        elif ((content[3] in line) or (content[0] in line)): # Ve se "Viram"/"Cobrem" está presente na frase | ou "viram"/"cobrem"

            for i in range(len(splitedline)):
                try:
                    depois = splitedline[i+1]
                except:
                    depois = "</s>"

                if (splitedline[i] == content[3]) and (i == 0): # Ve se no início da frase está "Viram" ou "Cobrem"
                    # Calc_prob.print_prob("<s> " + content[4] + " " + depois, file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    # Calc_prob.print_prob("<s> " + content[5] + " " + depois, file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    a=Calc_prob.print_prob("<s> " + content[4] + " " + depois, file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    b=Calc_prob.print_prob("<s> " + content[5] + " " + depois, file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    if max(a,b)==a:
                        results.append([line,[content[4],a],[content[5],b],'Lema mais provável:'+content[4]])
                    elif max(a,b)==b:
                        results.append([line, [content[4], a], [content[5], b],'Lema mais provável:'+ content[5]])
                    else:
                        results.append([line, [content[4], a], [content[5], b],'Lema mais provável:'+ ' equal prob'])
                    break

                elif (splitedline[i] == content[0]) and (i == 0): # Ve se no início da frase está "viram" ou "cobrem"
                    # Calc_prob.print_prob("<s> " + content[1] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    # Calc_prob.print_prob("<s> " + content[2] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    a=Calc_prob.print_prob("<s> " + content[1] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    b=Calc_prob.print_prob("<s> " + content[2] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    if max(a,b)==a:
                        results.append([line,[content[1],a],[content[2],b],'Lema mais provável:'+content[1]])
                    elif max(a,b)==b:
                        results.append([line, [content[1], a], [content[2], b], 'Lema mais provável:'+content[2]])
                    else:
                        results.append([line, [content[1], a], [content[2], b], 'Lema mais provável:'+' equal prob'])
                    break




                elif (splitedline[i] == content[3]) and (i > 0): # Ve se nesta posição da frase está "Viram" ou "Cobrem"
                    # Calc_prob.print_prob(splitedline[i-1] + " " + content[4] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    # Calc_prob.print_prob(splitedline[i-1] + " " + content[5] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    a=Calc_prob.print_prob(splitedline[i-1] + " " + content[4] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    b=Calc_prob.print_prob(splitedline[i-1] + " " + content[5] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    if max(a,b)==a:
                        results.append([line,[content[4],a],[content[5],b],'Lema mais provável:'+content[4]])
                    elif max(a,b)==b:
                        results.append([line, [content[4], a], [content[5], b],'Lema mais provável:'+ content[5]])
                    else:
                        results.append([line, [content[4], a], [content[5], b], 'Lema mais provável:'+' equal prob'])
                    break


                elif (splitedline[i] == content[0]) and (i > 0): # Ve se nesta posição da frase está "viram" ou "cobrem"
                    # Calc_prob.print_prob(splitedline[i-1] + " " + content[1] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    # Calc_prob.print_prob(splitedline[i-1] + " " + content[2] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    a=Calc_prob.print_prob(splitedline[i-1] + " " + content[1] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    b=Calc_prob.print_prob(splitedline[i-1] + " " + content[2] + " " + depois,file_unig, file_big, file_unig_smoo, file_big_smoo,line_count_unigrams)
                    if max(a,b)==a:
                        results.append([line,[content[1],a],[content[2],b],'Lema mais provável:'+content[1]])
                    elif max(a,b)==b:
                        results.append([line, [content[1], a], [content[2], b], 'Lema mais provável:'+content[2]])
                    else:
                        results.append([line, [content[1], a], [content[2], b],'Lema mais provável:'+ ' equal prob'])
                    break

        else:
            if DEBUG>10:
                print("***** Frase não contém a palavra CHAVE *****")
        if DEBUG>10:
            print("\n-------------------")
            print("-------------------")
            print("-------------------\n")

    f.close()
    with open('./'+content[0]+'Resultados.txt','w') as fout:
        for result in results:
            print('Result:'+str(result))
            print()
            print()

            fout.write('Result:'+str(result))
            fout.write('\n\n')





line_count_unigrams=0
def create_smoothed(file_unig, file_big):
    global line_count_unigrams
    line_count_unigrams = mapcount(file_unig)
    if DEBUG>10:
        print(line_count_unigrams)

    file_unig_smoo = (' ').join(file_unig.split('.')[0:-1])+'_smoothed'+'.'+file_unig.split('.')[-1]

    file_big_smoo = (' ').join(file_big.split('.')[0:-1])+'_smoothed'+'.'+file_big.split('.')[-1]



    with open(file_unig, 'r') as uni_file,              \
            open(file_big, 'r') as bi_file,              \
            open(file_unig_smoo, 'w') as uni_smooth_file, \
            open(file_big_smoo, 'w') as bi_smooth_file:


        for line in uni_file:

            key = line.split()[0]
            # print(key)
            value = int(line.split()[1]) + line_count_unigrams
            # print(value)
            uni_smooth_file.write(str(key) + ' ' + str(value) + '\n')


        for line in bi_file:
            # print (line)
            key = ' '.join(line.split('\t')[0:1])
            # print(key)
            # exit()
            value = int(line.split('\t')[1].split('\n')[0]) + 1
            # print(value)
            bi_smooth_file.write(str(key) + '\t' + str(value) + '\n')

    return file_unig_smoo, file_big_smoo



def mapcount(filename):
    f = open(filename, "r+")
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    return lines


DEBUG=0

if __name__ == "__main__":


    file_unig, file_big, file_param, file_frases = sys.argv[1:]

    file_unig_smoo, file_big_smoo = create_smoothed(file_unig, file_big)

    parse_sentence(file_frases, file_param, file_unig, file_big, file_unig_smoo, file_big_smoo)



    # file_param, file_frases = sys.argv[1:]
    # parse_sentence(file_frases, file_param)


