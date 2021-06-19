<html>
    <head>
        <meta charset="utf-8" />
        <title>Raspberry Pi Gpio</title>
    </head>
 
    <body style="background-color: white;">
    <!-- On/Off button's picture -->
	<?php
	$val_array = array(0,0);
	//this php script generate the first page in function of the file
	for ( $i= 0; $i<2; $i++) {
		//set the pin's mode to output and read them
		system("gpio mode ".$i." out");
		exec ("gpio read ".$i, $val_array[$i], $return );
	}
	//for loop to read the value
	$i =0;
	for ($i = 0; $i < 2; $i++) {
		//if off
		if ($val_array[$i][0] == 0 ) {
			echo ("<img id='button_".$i."' src='con/red_".$i.".png' onclick='change_pin (".$i.");'/>");
		}
		//if on
		if ($val_array[$i][0] == 1 ) {
			echo ("<img id='button_".$i."' src='con/green_".$i.".png' onclick='change_pin (".$i.");'/>");
		}	 
	}
	?>
	 
	<!-- javascript -->
	<script src="script.js"></script>
    </body>
</html>