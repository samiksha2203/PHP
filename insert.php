<?php
$m = new MongoClient();
echo "Connection to database successfully";

$db = $m->MYDB259711;
echo "In Database selected successfully";

$col = $db->MyCol;
echo "In Collection selected successfully";

$doc = array(
    "name" => "shreya",
    "age" => 20,
    "dept" => "IT",
    "rollno" => 259711
);

$col->insert($doc);
echo "In Document inserted successfully";
?>
