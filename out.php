
<?php

$m=$_REQUEST['fileurl'];
if($m==NULL)
	echo "<script>alert('please enter file name');
		window.location.href='index.html'; 
		</script>";
else
{
$output=shell_exec('C:\akhila\python C:\Users\vanga\june28\output.py "'.$m.'"');

if($output[1]==1)
{
	echo '<html><body bgcolor="#000000">';
	echo '<center><br><br><h1><font size="+7" color=white>HAPPY SONG</font></h1>';
    echo '<br><img src="img/happy.gif" height="80%" width="40%">';
	echo "</center></body></html>";
}
else
{	echo '<html><body bgcolor="#000000">';
    echo '<center><br><br><h1><font size="+7" color=white>SAD SONG</font></h1>';
    echo '<br><img src="img/sad.gif" height="80%" width="40%">';
	echo "</center></body></html>";
}
}
?>

 
