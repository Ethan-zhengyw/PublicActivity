(function(){
  $(function(){
    $('.del').click(function(e){
      var target, id, tr;
      target = $(e.target);
      id = target.data('id');
      tr = $('.item-id-' + id);
      $.get('/s-activity-delete?id=' + id, function(results){
        if (results.success === 1) {
          if (tr.length > 0) {
            tr.remove();
          }
        }
      });
    });
    $('#myTab a').click(function(e){
      e.preventDefault();
      $(this).tab('show');
    });
  });
}).call(this);
