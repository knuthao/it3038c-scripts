$Machines = 'knuthao-win'
#foreach ($Machine in $Machines) {
 #   $RCounters = Get-Counter -ListSet * -ComputerName $Machine
  #  "There are {0} counters on {1}" -f $RCounters.count, {$Machine}
#}

foreach ($machine in $Machines) {
    $pt = (Get-Counter -Counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 10).CounterSamples.CookedValue
    $sample = 1
    foreach ($p in $pt) {
        "Sample {2}: CPU is at {0}% on {1}" -f [int]$p, $machine, $sample | out-File -Append C:\logs\output.txt
        $sample++
    }    
}