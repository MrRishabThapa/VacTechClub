const eyeIcon = document.getElementById("eye");
const passwordField = document.getElementById("password");
eyeIcon.addEventListener("click", () => {
  if (passwordField.type === "password" && passwordField.value) {
    passwordField.type = "text";
    eyeIcon.classList.remove("fa-eye");
    eyeIcon.classList.add("fa-eye-slash");
  } else {
    passwordField.type = "password";
    eyeIcon.classList.remove("fa-eye-slash");
    eyeIcon.classList.add("fa-eye");
  }
});

// Password visibility toggle
document.addEventListener('DOMContentLoaded', function() {
    const eyeIcon = document.getElementById('eye');
    if (eyeIcon) {
        eyeIcon.addEventListener('click', function() {
            const passwordInput = document.getElementById('password');
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                this.classList.remove('fa-eye');
                this.classList.add('fa-eye-slash');
            } else {
                passwordInput.type = 'password';
                this.classList.remove('fa-eye-slash');
                this.classList.add('fa-eye');
            }
        });
    }

    // Add animation to input groups on focus
    const inputGroups = document.querySelectorAll('.input-group');
    inputGroups.forEach(group => {
        const input = group.querySelector('input');
        input.addEventListener('focus', function() {
            group.style.transform = 'translateY(-2px)';
        });
        
        input.addEventListener('blur', function() {
            group.style.transform = 'translateY(0)';
        });
    });

    // Button hover effect
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});


