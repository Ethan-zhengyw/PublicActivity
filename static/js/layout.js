(function(){
  $(function(){
    $('.profile').click(function(){
      if ($('.profile-menu').hasClass('hide')) {
        $('.profile-menu').removeClass('hide');
      } else {
        $('.profile-menu').addClass('hide');
      }
    });
    $(document).click(function(e){
      var target, profile;
      target = e.srcElement || e.target;
      profile = $('.profile')[0];
      while (target && target !== document && target !== profile) {
        target = target.parentNode;
      }
      if (target === document) {
        $('.profile-menu').addClass('hide');
      }
    });
    if ($('#home_wrap').length !== 0) {
      $('#header .nav a').removeClass('active');
      $('#header .home').addClass('active');
    } else if ($('#host_wrap').length !== 0) {
      $('#header .nav a').removeClass('active');
      $('#header .host').addClass('active');
    } else {
      $('#header .nav a').removeClass('active');
    }
  });
}).call(this);
