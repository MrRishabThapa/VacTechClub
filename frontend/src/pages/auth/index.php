<?php
session_start();
if (isset($_SESSION['errors'])) {
  $errors = $_SESSION['errors'];
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vac-Tech Jr | Login</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <div class="wrapper">
    <!-- Left Side with Image Only -->
    <div class="left-side">
      
    </div>

    <!-- Right Side with Form -->
    <div class="right-side">
      <div class="container" id="signIn">
        <div class="tabs">
          <button class="tab-btn active">Login</button>
          <button class="tab-btn" onclick="window.location.href='register.php'">SignUp</button>
        </div>

        <h1 class="form-title">Welcome Back</h1>
        
        <?php
        if (isset($errors['login'])) {
          echo '<div class="error-main">
                    <p>' . $errors['login'] . '</p>
                    </div>';
          unset($errors['login']);
        }
        ?>
        
        <form method="POST" action="user-account.php">
          <div class="input-group">
            <i class="fas fa-envelope"></i>
            <input type="email" name="email" id="email" placeholder="Enter your email" required>
            <?php
            if (isset($errors['email'])) {
              echo ' <div class="error">
                    <p>' . $errors['email'] . '</p>
                </div>';
            }
            ?>
          </div>
          
          <div class="input-group password">
            <i class="fas fa-lock"></i>
            <input type="password" name="password" id="password" placeholder="Enter Password" required>
            <i id="eye" class="fa fa-eye"></i>
            <?php
            if (isset($errors['password'])) {
              echo ' <div class="error">
                    <p>' . $errors['password'] . '</p>
                </div>';
            }
            ?>
          </div>
          
          <p class="recover">
            <a href="#">Recover Password</a>
          </p>
          
          <input type="submit" class="btn" value="Login" name="signin">
        </form>
        
        <div class="signup-link">
          <p>Don't have an account? <a href="register.php">Sign up</a></p>
        </div>
      </div>
    </div>
  </div>
  
  <script src="script.js"></script>
</body>

</html>
<?php
if (isset($_SESSION['errors'])) {
  unset($_SESSION['errors']);
}
?>