#!/bin/bash

courses=$(wc -l < /home/codebind/Desktop/code1/headers.txt)  

#echo $courses

INPUTFILE=home/codebind/Desktop/code1/master.csv

#while read line; do for i in 'awk -F"," '{print $1}' $INPUTFILE', j in 'awk -F"," '{print $2}' $INPUTFILE' ; done < $INPUTFILE

#while read line; do for i in 'awk -F"," '{print $1}' $INPUTFILE', j in 'awk -F"," '{print $2}' $INPUTFILE', k in 'awk -F"," '{print $3} $INPUTFILE' ; done < $INPUTFILE

#for i in 'awk -F"," '{print $1}' $INPUTFILE', j in 'awk -F"," '{print $2}' $INPUTFILE', k in 'awk -F"," '{print $3}' $INPUTFILE' ;do ;done

#sed 's/,/ /g' master.csv | awk -F, '{print $1","}' master.csv |

#echo $line#sed 's/,/ /g' master.csv | awk -F, '{ print $1"," ; if ( $line == $2) print $3 ; else print ","}' master.csv


#while read line ; do awk -F, '{ print $1"," ; if ( $2 == $line ) print $3 ; else print ",";}' master.csv ; done < headers.txt 

#sed 's/,/ /g' master.csv | awk -F, 'BEGIN{print $1",";{while read line ; do echo $line ; done < headers.txt}}' master.csv

#for line in  $(cat headers.txt)
#do
 # sed 's/,/ /g' master.csv | awk '{ print $1"," ; if ( $2 == $line ) print "," ; else print $3;}'  
#done

#sed 's/,/ /g' master.csv | awk '{ print $1"," ; for line in $(cat /home/codebind/Desktop/code1/headers.txt) ( $2 == line ) ? print $3 : print ","}'

#sed 's/,/ /g' master.csv | awk '{ print $1"," ; for line in $(cat /home/codebind/Desktop/code1/headers.txt) ( $2 == line ) ? print $3 : print ","}'

#awk '{print;getline;  file++;while((getline <sprintf("headers.txt",file))>0) print $1",";( $2 == getline ) ? print $3 : print ",";close(sprintf("headers.txt", file));}' master.csv > output.txt

index=0 
while read line 
do 
	arr[$index]=$line 
	((index++)) 
done < headers.txt 
echo ${arr[*]}

len=${#arr[@]}

echo $len

#sed 's/,/\t/g' master.csv | awk '{print $1",";for(i in arr){ if ($2!=arr[i]) print ","; else print $3;} i++}' 

echo "$(cut -d',' -f1 master.csv)"
for i in $(cut -d',' -f2 master.csv)
do
	for (( j=0 ; j<$len ; j++ ))
	do
		if [ $i == arr[j] ] 
		then
			echo "$(cut -d',' -f3 master.csv)"
		else
			echo ","
		fi
	done
done


