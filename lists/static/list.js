jQuery(document).ready(function ($) {
  $('input[name="text"]').on('keypress', function () {
    $('.has-error').hide();
  });
});

