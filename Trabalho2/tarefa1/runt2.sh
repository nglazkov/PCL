
#generate the .final for any .out file.

# 2 args:
##
##  1: inputfile .out file generated from java CorpusAnnotator.class ;
##  2: special search word to be repalced by anotation in the beg if each line;
#
# Generates a cleaned .final in tarefas2 folder from the .out,


rm ngrams/*

python ./src/run_ngram.py cobremCobrarCobrir.final ngrams_cobrem 


python ./src/run_ngram.py viramVerVirar.final ngrams_viram
