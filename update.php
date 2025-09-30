<?php
$m = new MongoClient();
echo "Connection to database successfully";

$db = $m->MYDB259711;
echo "In Database selected successfully";

$col = $db->MyCol;
echo "In Collection selected successfully";

$col->update(
    array("name" => "shreya"),
    array('$set' => array("age" => 19))
);

echo "In Document Updated Successfully";
?>
