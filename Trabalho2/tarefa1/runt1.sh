
#generate the .final for any .out file.

# 2 args:
##
##  1: inputfile .out file generated from java CorpusAnnotator.class ;
##  2: special search word to be repalced by anotation in the beg if each line;
#
# Generates a cleaned .final in tarefas2 folder from the .out,

rm ../tarefa1/cobremCobrarCobrir.final
rm ../tarefa1/viramVerVirar.final

python ./src/run_cleaner.py ./cobrem/cobremCobrarCobrir.out ../tarefa1/cobremCobrarCobrir.final cobrem

python ./src/run_cleaner.py ./viram/viramVerVirar.out ../tarefa1/viramVerVirar.final viram
