<?php
$m = new MongoClient();
echo "Connection to database successfully";

$db = $m->MYDB259711;
echo "In Database selected successfully";

$col = $db->MyCol;
echo "In Collection selected successfully";

$col->remove(array("name" => "sami"));

echo "In Document deleted successfully";
?>
