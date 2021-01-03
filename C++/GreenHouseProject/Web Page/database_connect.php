<?php
  $servername = "localhost";
  $username = "<DATA BASE USERNAME>";
  $password = "<DATA BASE PASSWORD>";
  $dbname = "<DATA BASE NAME>";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);
  // Check connection
  if ($conn->connect_error)
  {
    die("Connection failed: " . $conn->connect_error);
  }
  
/*
  $temp = ("'" . $_POST["temp"] . "S'");
  $datetime = ("'" . $_POST["datetime"] . "'");
  $hum = ("'" . $_POST["hum"] . "'");
  $fan_volt = ("'" . $_POST["volt"] . "'");  */

  //$poggers = key($_POST);
  //var_dump($poggers);
  //var_dump($_POST);
  $auth_key = '<AUTH KEY>';
  $key = $_POST['key'];
  $temp = $_POST["temp"];
  $datetime = ("'" . $_POST["DT"] . "'");
  $hum = $_POST["hum"];
  $fan_volt = $_POST["volt"];
  
  $sql = "INSERT INTO AmirPog (Temperature, Humidity, Voltage, DT) VALUES ($temp, $hum, $fan_volt, $datetime);";
  //echo $sql;
  $result = $conn->query($sql);

 // echo "Ugh, Fine I Guess You Are My Little Pogchamp.";
if ($temp > "24") {
  echo "ugh fine, youre my HOT! little pogchamp";
} else {
  echo "ugh fine, youre my COLD! little pochamp";
}
  //echo $error;
?>

