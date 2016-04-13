
#!/bin/sh
a=1
#cd ../../CRF++-0.58/   
until [ $a -ge 6 ]
do
   echo Fold : $a

   #TESTING OF THE FOLD BASED ON CORRESPONDING MODEL
   crf_test -m ../Models/model$a ../TestFiles/testFile$a > ../Results/result$a
   
   a=`expr $a + 1`
done

#cd -
echo 'Predictions for 5 fold completed, 5 result files generated'
echo ""
