#!/bin/sh
echo ''
echo "#########################################################"
echo "5 cross Evaluation"
echo "#########################################################"
echo ''
a=1

acc=0
until [ $a -ge 6 ]
do
   #FINDING ACCURACY OF THIS FOLD
   ac=$(python '../PythonCodes/crf_accuracy.py' '../Results/result'$a $a)
   #ac=20
   echo -e "\tAccuracy of fold $a : $ac"
   acc=`expr $acc + $ac`

   a=`expr $a + 1`
done
five=5
acc=`expr $acc / $five`
echo ""
echo -e "\tMEAN ACCURACY is $acc %"
echo ""
