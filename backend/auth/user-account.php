<?php
session_start();
require_once 'firebase-config.php';

if (isset($_POST['signup'])) {
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $password = $_POST['password'];
    $confirm_password = $_POST['confirm_password'];
    
    $errors = [];
    
    // Validation
    if (empty($name)) {
        $errors['name'] = "Name is required";
    }
    
    if (empty($email)) {
        $errors['email'] = "Email is required";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "Invalid email format";
    }
    
    if (empty($password)) {
        $errors['password'] = "Password is required";
    } elseif (strlen($password) < 6) {
        $errors['password'] = "Password must be at least 6 characters";
    }
    
    if ($password !== $confirm_password) {
        $errors['confirm_password'] = "Passwords do not match";
    }
    
    if (empty($errors)) {
        $result = $firebaseAuth->signUp($email, $password, $name);
        
        if ($result['success']) {
            $_SESSION['user'] = [
                'uid' => $result['uid'],
                'email' => $email,
                'name' => $name
            ];
            
            header("Location: index.php");
            exit();
        } else {
            $errors['user_exist'] = "Error: " . $result['error'];
        }
    }
    
    $_SESSION['errors'] = $errors;
    header("Location: register.php");
    exit();
}

if (isset($_POST['signin'])) {
    $email = trim($_POST['email']);
    $password = $_POST['password'];
    
    $errors = [];
    
    if (empty($email)) {
        $errors['email'] = "Email is required";
    }
    
    if (empty($password)) {
        $errors['password'] = "Password is required";
    }
    
    if (empty($errors)) {
        $result = $firebaseAuth->signIn($email, $password);
        
        if ($result['success']) {
            $_SESSION['user'] = [
                'uid' => $result['uid'],
                'email' => $email,
                'name' => 'User'
            ];
            
            header("Location: home.php");
            exit();
        } else {
            $errors['login'] = "Invalid email or password";
        }
    }
    
    $_SESSION['errors'] = $errors;
    header("Location: index.php");
    exit();
}
?>