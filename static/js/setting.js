(function(){
  $('#avatar-form').submit(function(evt){
    evt.preventDefault();
    $.ajax({
      type: 'POST',
      url: '/s-user-save',
      processData: false,
      contentType: false,
      data: new FormData(this),
      success: function(msg){
        if (msg === 'ok') {
          location.href = '/setting';
        } else {
          alert(msg);
        }
      }
    });
  });
  $(function(){
    $('#inputTime').datetimepicker();
    $('.btn-addTag').each(function(){
      $(this).click(function(){
        /* will be wrong if there are more than one input */
        var input, press;
        input = $('.bootstrap-tagsinput > input');
        input.val(input.val() +', '+ $(this).text());
        press = jQuery.Event("keypress");
        press.ctrlKey = false;
        press.which = 13;
        input.trigger(press);
      });
    });
  });
}).call(this);
