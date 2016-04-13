#!/bin/sh
a=1

#cd ../../CRF++-0.58/   
until [ $a -ge 6 ]
do
   echo Fold : $a
   
   #LEARNING OF THE FOLD
   crf_learn ../template ../TrainingFiles/trainFile$a ../Models/model$a
   echo "Fold $a Learning Completed"
   a=`expr $a + 1`
done

#cd -

echo '5 fold learning completed, models generated for each fold'
