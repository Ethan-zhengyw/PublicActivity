(function(){
  $(function(){
    $('#inputTime').datetimepicker();
    $('.btn-addTag').each(function(){
      $(this).click(function(){
        /* will be wrong if there are more than one input */
        var input, press;
        input = $('.bootstrap-tagsinput > input');
        input.val(input.val() + $(this).text());
        press = jQuery.Event("keypress");
        press.ctrlKey = false;
        press.which = 13;
        input.trigger(press);
      });
    });
  });
}).call(this);
