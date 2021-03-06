#!/bin/bash

SOURCEDIR=/home/codebind/Desktop/code
DESTDIR=/home/codebind/Desktop/code/courses

mkdir courses
#touch headers.txt

case $1 in 
	-s)
		make
		;;
	--setup)
		make
		;;
	-g)
		chmod +x generator
		$SOURCEDIR/generator $2 > master.csv
		;;
	--generate)
		chmod +x generator
                $SOURCEDIR/generator $2 > master.csv
                ;;
	-c)
		if [ $2 == "-all" ]
		then
			for i in $(cut -d',' -f2 master.csv | sort | uniq)
			do
				touch $i.csv
				mv $SOURCEDIR/$i.csv  $DESTDIR
				grep $i "master.csv" | sort | cut -d',' -f1,3 | sed 's/,/ /g' | sort -k1,1 -k2,2rn | sort -uk1,1 | sed 's/ /,/g' >> $DESTDIR/$i.csv
			done
		else
			touch $2.csv
			mv $SOURCEDIR/$2.csv  $DESTDIR
			grep $2 "master.csv" | sort | cut -d',' -f1,3 | sed 's/,/ /g' | sort -k1,1 -k2,2rn | sort -uk1,1 | sed 's/ /,/g' >> $DESTDIR/$2.csv
		fi	
		;;
	--course)
		if [ $2 == "-all" ]
                then
                        for i in $(cut -d',' -f2 master.csv | sort | uniq)
                        do
                                touch $i.csv
                                mv $SOURCEDIR/$i.csv  $DESTDIR
                                grep $i "master.csv" | sort | cut -d',' -f1,3 | sed 's/,/ /g' | sort -k1,1 -k2,2rn | sort -uk1,1 | sed 's/ /,/g' >> $DESTDIR/$i.csv
                        done
                else
                        touch $2.csv
                        mv $SOURCEDIR/$2.csv  $DESTDIR
                        grep $2 "master.csv" | sort | cut -d',' -f1,3 | sed 's/,/ /g' | sort -k1,1 -k2,2rn | sort -uk1,1 | sed 's/ /,/g' >> $DESTDIR/$2.csv
                fi 
		;;
	#-b)
		#if [ $2 == "-all" ]
		#then
			#cut -d',' -f2 master.csv headers.txt | sort | uniq >> headers.txt
			#cut -d',' -f1,2 master.csv | sort | uniq
		#else
		#fi
		#;;
	#--branch)

		#;;
	*)
		echo "not valid option"
		;;
esac

