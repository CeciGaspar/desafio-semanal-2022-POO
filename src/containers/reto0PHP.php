<?php
$num=0;

while ($num < 100){
    $num++;
    if ($num%3==0 and $num%5==0){
        print("FIZZBUZZ");
    } else if ($num%3==0) {
        print("FIZZ");   
    } else if ($num%5==0){    
        print("BUZZ");  
    } else {
        print($num);
    }
}

?>