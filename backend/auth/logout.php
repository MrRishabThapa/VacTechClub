<?php
session_start();

// Optional: Revoke Firebase token
if (isset($_SESSION['user']['idToken'])) {
    // You can call Firebase API to revoke the token if needed
}

session_destroy();
header("Location: index.php");
exit();
?>