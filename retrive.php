<?php
$m = new MongoClient();
echo "Connection to database successfully";

$db = $m->MYDB259711;
echo "In Database selected successfully";

$col = $db->MyCol;
echo "In Collection selected successfully";

$cursor = $col->find();

foreach ($cursor as $doc) {
    echo "<br/>";
    echo $doc["name"] . "<br/>";
    echo $doc["age"] . "<br/>";
    echo $doc["dept"] . "<br/>";
    echo $doc["rollno"] . "<br/>";
}
?>
