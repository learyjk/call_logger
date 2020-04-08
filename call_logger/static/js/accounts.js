const form = document.getElementById('form');
const first_name = document.getElementById('first_name');
const last_name = document.getElementById('last_name');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

// Show input error message
function showError(input, message) {
    input.className = 'form-control is-invalid';
    const small = input.parentElement.querySelector('small');
    small.className = 'invalid-feedback';
    small.innerText = message;
}

// Show success outline
function showSuccess(input, message) {
    input.className = 'form-control is-valid';
    const small = input.parentElement.querySelector('small');
    small.className = 'valid-feedback';
    small.innerText = message;
}


function checkRequired(inputArray) {
  let valid = true;
  for (const input of inputArray) {
    if (input.value.trim() === '') {
      valid = false;
      showError(input, `${getFieldName(input)} is required`);
    }
    else {
        showSuccess(input, 'Looks Good!');
    }
  }
  return valid;
}

// Check email is valid
function checkEmail(input) {
  const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if (re.test(input.value.trim())) {
    showSuccess(input, 'Looks Good!');
    return true;
  } else {
    showError(input, 'Email is not valid');
    return false;
  }
}

// Check input length
function checkLength(input, min, max) {
  if (input.value.length < min) {
    showError(
      input,
      `${getFieldName(input)} must be at least ${min} characters`
    );
    return false;
  } else if (input.value.length > max) {
    showError(
      input,
      `${getFieldName(input)} must be less than ${max} characters`
    );
    return false;
  } else {
    showSuccess(input, 'Looks Good!');
    return true;
  }
}

// Check passwords match
function checkPasswordsMatch(input1, input2) {
  if (input1.value !== input2.value) {
    showError(input2, 'Passwords do not match');
    return false;
  }
  return true;
}

// Get fieldname
function getFieldName(input) {
  return input.id.charAt(0).toUpperCase() + input.id.slice(1);
}

// Event listeners
form.addEventListener('submit', function(e) {
  if (!checkLength(username, 3, 15)) {
      e.preventDefault();
  }
  if (!checkLength(password, 6, 25)) {
      e.preventDefault();
  }
  if (!checkEmail(email)) {
      e.preventDefault();
  }
  if (!checkPasswordsMatch(password, password2)) {
      e.preventDefault();
  }
  if (!checkRequired([first_name, last_name, username, email, password, password2])) {
      e.preventDefault();
  }
});
