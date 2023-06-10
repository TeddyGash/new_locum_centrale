var registerAsField = document.getElementById(
  '{{ form.register_as.id_for_label }}',
);
var mdcRegistrationField = document.getElementById('mdc-registration-no-field');
var signupForm = document.getElementById('signup_form');
var signupButton = document.getElementById('signup_button');
var verificationStatus = document.getElementById('verification_status');
var verificationText = document.getElementById('verification_text');

function toggleMdcRegistrationField() {
  if (registerAsField.value === 'doctor' || registerAsField.value === 'pa') {
    mdcRegistrationField.style.display = 'block';
  } else {
    mdcRegistrationField.style.display = 'none';
  }
}

registerAsField.addEventListener('change', toggleMdcRegistrationField);
toggleMdcRegistrationField();

function verifyFormFields() {
  var firstName = $('#id_first_name').val();
  var lastName = $('#id_last_name').val();
  var category = $('#id_register_as').val();
  var mdcNumber = $('#mdc-registration-no-field').val();
  var fullName = firstName + ' ' + lastName;

  if ((category === 'doctor' || category === 'pa') && fullName && mdcNumber) {
    verificationStatus.style.display = 'block';
    verificationText.innerText = 'Verifying...';
    signupButton.disabled = true;

    $.ajax({
      url: "{% url 'users:verify_mdc_details' %}",
      type: 'POST',
      data: {
        full_name: fullName,
        category: category,
        mdc_number: mdcNumber,
        csrfmiddlewaretoken: '{{ csrf_token }}',
      },
      success: function (response) {
        verificationText.innerText = response.message;
        if (response.verified) {
          signupButton.disabled = false;
        } else {
          signupButton.disabled = true;
        }
      },
      error: function (xhr, status, error) {
        verificationText.innerText = 'An error occurred during verification.';
        console.error(error);
        signupButton.disabled = true;
      },
      complete: function () {
        signupForm.submit(); // Submit the form after verification is complete
      },
    });
  } else {
    verificationStatus.style.display = 'none';
    signupButton.disabled = true;
  }
}

$(
  '#id_first_name, #id_last_name, #id_register_as, #mdc-registration-no-field',
).on('input', verifyFormFields);
verifyFormFields();
