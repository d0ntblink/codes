<!DOCTYPE html>
<html>
<script src="https://code.highcharts.com/highcharts.js"></script>
<?php
  $servername = "localhost";
  $username = "airdata";
  $password = "AESl0uis!";
  $dbname = "poggers";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);
  // Check connection
  if ($conn->connect_error)
  {
    die("Connection failed: " . $conn->connect_error);
  }

  $sql = "SELECT * FROM AmirPog ORDER BY DT DESC";
  $result = $conn->query($sql);

  if ($result->num_rows > 0)
   {
     $json_array = array();
    
     echo
     "<div>
         <table border ='1'>
           <tr>
             <th>Temperature</th>
             <th>Humidity</th>
             <th>Voltage</th>
            <th>Datetime</th>
          </tr>";
          

    while($row = $result->fetch_assoc())
    {
        $volt = $row["Voltage"];
        $temp = $row["Temperature"];
        $RH = $row["Humidity"];
        $Date = $row["DT"];

        $json_array[] = array($temp, $RH, $volt, $Date);
        
        echo "<tr>";
        echo "<td>$temp</td>";
        echo "<td>$RH</td>";
        echo "<td>$volt</td>";
        echo "<td>$Date</td>";
        
    }
    echo "</table></div>";

    $javascript_array = json_encode($json_array);

    //echo $javascript_array;
  }
  else
  {
    echo "0 results";
  }
  $conn->close();
?>
</html>
