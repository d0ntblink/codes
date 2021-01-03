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

  $sql = "SELECT * FROM <DATABASENAME> ORDER BY DT ASC";
  $result = $conn->query($sql);

  if ($result->num_rows > 0)
  {
    $monitor_array = array();

    while($row = $result->fetch_assoc())
    {
      $temp = $row["Temperature"];
      $hum = $row["Humidity"];
      $volt = $row["Voltage"];
      $dt = $row["DT"];

      $date = date_create($dt);
      $date_formatted = date_format($date, "U");

      $tempfloat = floatval($temp);
      $humfloat = floatval($hum);
      $voltfloat = floatval($volt);
      $date_epoch = floatval($date_formatted) * 1000;
           
      //$json_array[] = array($temp, $hum, $volt, $date_epoch);
      $temp_array[] = array($date_epoch, $tempfloat);
      $hum_array[] = array($date_epoch, $humfloat);
      $volt_array[] = array($date_epoch, $voltfloat);
      
    }

    $json_array[] = array($temp_array, $hum_array, $volt_array);
    
    //converts PHP array into a format javascript can interpret
    $javascriptarray = json_encode($json_array);

    echo($javascriptarray);
  }
  else
  {
    echo "0 results";
  }
  $conn->close();
?>


