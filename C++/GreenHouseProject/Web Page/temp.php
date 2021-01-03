
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
  $sql = "SELECT * FROM <DATABASE NAME> ORDER BY DT DESC LIMIT 1";
  $result = $conn->query($sql);
  if ($result->num_rows > 0)
   {
     $json_array = array();
    while($row = $result->fetch_assoc())
    {
        $temp = $row["Temperature"];
        echo $temp; 
    }
  }
  else
  {
    echo "0 results";
  }
  $conn->close();
?>
