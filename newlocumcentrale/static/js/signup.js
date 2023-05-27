// signup.js

var registerAsField = document.getElementById(
  '{{ form.register_as.id_for_label }}',
);
var mdcRegistrationField = document.getElementById('mdc-registration-no-field');

mdcRegistrationField.style.display = 'none';

registerAsField.addEventListener('change', function () {
  var selectedOption = registerAsField.value;
  if (selectedOption === 'doctor' || selectedOption === 'pa') {
    mdcRegistrationField.style.display = 'block';
  } else {
    mdcRegistrationField.style.display = 'none';
  }
});

// Trigger the change event initially to set the initial visibility correctly
registerAsField.dispatchEvent(new Event('change'));

// $(document).ready(function() {
//     var registerAsField = $('#id_register_as');
//     var mdcRegistrationNoField = $('#id_mdc_registration_no');

//     function toggleMdcRegistrationNoField() {
//       var selectedValue = registerAsField.val();
//       if (selectedValue === 'doctor' || selectedValue === 'pa') {
//         mdcRegistrationNoField.parent().show();
//       } else {
//         mdcRegistrationNoField.parent().hide();
//       }
//     }

//     toggleMdcRegistrationNoField();
//     registerAsField.change(toggleMdcRegistrationNoField);
//   });

//   $("register-as-field").change(function() {
//     if ($(this).val() == "doctor" || $(this).val() == "pa") {
//       $('#mdc-registration-no-field').show();
//       $('#mdc-registration-no-field').attr('required', '');
//       $('#mdc-registration-no-field').attr('data-error', 'This field is required.');
//     } else {
//       $('#mdc-registration-no-field').hide();
//       $('#mdc-registration-no-field').removeAttr('required');
//       $('#mdc-registration-no-field').removeAttr('data-error');
//     }
//   });
//   $("#register-as-field").trigger("change");
