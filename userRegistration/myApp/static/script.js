function validateForm() {
    var name = document.getElementById('name').value;
    var dob = document.getElementById('dob').value;
    var category = document.getElementById('category').value;
    var email = document.getElementById('email').value;
    var mobile = document.getElementById('mobile').value;
    var password = document.getElementById('password').value;
    var college = document.getElementById('college').value;
    var branch = document.getElementById('branch').value;
    var year = document.getElementById('year').value;
  
    // Basic validation for empty fields
    if (name === '' || dob === '' || category === '' || email === '' || mobile === '' || password === '' || college === '' || branch === '' || year === '') {
      alert('Please fill out all fields');
      return false;
    }
  
    // More validation can be added here (e.g., email format, mobile number format, etc.)
  
    return true;
  }
  