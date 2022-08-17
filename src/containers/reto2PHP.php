<?php

function fibonacci_iter($n)
{
    $a = 1;
    $b = 1;
    
    if ($n == 1) {echo ('0');} 
    elseif ($n == 2) {echo ('0'); echo ('1');}
   else {
    echo ('0'); echo ($a); echo ($b);
   	for ($n = 47; $n > 0; $n--) {
    $total = $a + $b;
    $b = $a;
    $a = $total;
    echo ($total);;
}
		}
    }
   
fibonacci_iter(50)

?>