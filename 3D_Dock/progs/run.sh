#!/bin/bash
NEXEC=$1
static=../../inputs/1ACB_rec.parsed
mobile=../../inputs/1ACB_lig.parsed
test_output=../../outputs/test4.output
make
echo "Calculating one execution and comparing"
./ftdock -static $static -mobile $mobile > output
python diff.py $test_output output > diff_result
exit_code=`cat diff_result`
if [ "$exit_code" == "False" ]; then
   echo "No correct results for the optimized program" 
   exit
fi
echo "Correct results for the optimized program" 
echo "Calculating average time for $NEXEC executions"
EXEC=0
totaltime=0
while [  $EXEC -lt $NEXEC ]; do   
    ./ftdock -static $static -mobile $mobile > output
   	timeline=`cat output | grep time:`
	time=`python -c "print '${timeline}'.split()[1]"`
    totaltime=`python -c "print str($totaltime + $time)"` 
    let EXEC=EXEC+1
done
finaltime=$(python -c "print $totaltime/$NEXEC")
echo "Avarage elapsed time for" $NEXEC "executions -> " $finaltime
