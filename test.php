<?php
$servername = "mysql";
$username = "my_user";
$password = "my_password";
$dbname = "my_database";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully to MySQL";

$conn->close();
?>

