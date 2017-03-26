#!/bin/bash
#Arquivo para gerar instancias automaticamente

#Funcao que recebe N e TEMPO_MAXIMO
#Retorna uma lista contendo N atividades entre 0 e TEMPO_MAXIMO
gera_atividade() {
    RANDOM=$$

    for i in `seq 1 $1`
    do
        N1=0
        N2=0
        while [ $N1 -eq $N2 ]
        do
            N1=$(($RANDOM%$2))
            N2=$(($RANDOM%$2))
        done

        max=$N1
        min=$N2

        if [ $N2 -gt $N1 ]
        then
            max=$N2
            min=$N1
        fi
        echo $min $max

    done
}

#Gera atividades

for i in `seq 1 14`
do
    n=$(($i*10))
    m=$(($i*20))
    for j in `seq 1 10`
    do
        arquivo="$(pwd)/arquivos/$n/$j.txt"
        gera_atividade $n $m > $arquivo
        python guloso.py $arquivo -t >> "$(pwd)/resultados/guloso_$n.txt"
        python dinamico.py $arquivo -t >> "$(pwd)/resultados/dinamico_$n.txt"
        python backtracking.py $arquivo -t >> "$(pwd)/resultados/backtracking_$n.txt"
    done
done
