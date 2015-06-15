(function(){
  $(function(){
    var myTagNum, i$, to$, i, hotTagNum, pagingHandler, getActs, sHomepageUpdate;
    $('#myTab a').click(function(e){
      e.preventDefault();
      $(this).tab('show');
    });
    $('.carousel').carousel();
    $(window).scroll(function(){
      var scrollt;
      scrollt = document.documentElement.scrollTop + document.body.scrollTop;
      if (scrollt > 200) {
        $('.back_to_top').fadeIn();
      } else {
        $('.back_to_top').stop().fadeOut();
      }
    });
    $('.back_to_top').click(function(){
      $('html,body').animate({
        scrollTop: '0px'
      }, 200);
    });
    myTagNum = $('.active .my_tag .tag').length;
    if (myTagNum <= 5) {
      $('.my_tag .slide_toggle').hide();
    } else {
      for (i$ = 5, to$ = myTagNum - 1; i$ <= to$; ++i$) {
        i = i$;
        $($('#future .my_tag .tag')[i]).addClass('slide_tag');
      }
      for (i$ = 5, to$ = myTagNum - 1; i$ <= to$; ++i$) {
        i = i$;
        $($('#past .my_tag .tag')[i]).addClass('slide_tag');
      }
      for (i$ = 5, to$ = myTagNum - 1; i$ <= to$; ++i$) {
        i = i$;
        $($('#all .my_tag .tag')[i]).addClass('slide_tag');
      }
    }
    hotTagNum = $('.active .hot_tag .tag').length;
    if (hotTagNum <= 5) {
      $('.hot_tag .slide_toggle').hide();
    } else {
      for (i$ = 5, to$ = hotTagNum - 1; i$ <= to$; ++i$) {
        i = i$;
        $($('#future .hot_tag .tag')[i]).addClass('slide_tag');
      }
      for (i$ = 5, to$ = hotTagNum - 1; i$ <= to$; ++i$) {
        i = i$;
        $($('#past .hot_tag .tag')[i]).addClass('slide_tag');
      }
      for (i$ = 5, to$ = hotTagNum - 1; i$ <= to$; ++i$) {
        i = i$;
        $($('#all .hot_tag .tag')[i]).addClass('slide_tag');
      }
    }
    $('.my_tag .slide_toggle').click(function(){
      $('.active .my_tag .slide_tag').slideToggle('fast');
      if ($(this).text() === '展开') {
        $(this).text('收起');
      } else {
        $(this).text('展开');
      }
    });
    $('.hot_tag .slide_toggle').click(function(){
      $('.active .hot_tag .slide_tag').slideToggle('fast');
      if ($(this).text() === '展开') {
        $(this).text('收起');
      } else {
        $(this).text('展开');
      }
    });
    $('.sort_area .sort').click(function(){
      $('.sort_area .sort').removeClass('active');
      $(this).addClass('active');
      getActs();
    });
    $('.tag_item').click(function(e){
      var target, i$, ref$, len$, x, tagName, tagSelected;
      target = $(e.target);
      if ($(this).hasClass('chosen')) {
        $(this).removeClass('chosen');
        for (i$ = 0, len$ = (ref$ = $('.tag_selected')).length; i$ < len$; ++i$) {
          x = ref$[i$];
          if ($(x).data('id') === target.data('id')) {
            $(x).remove();
          }
        }
      } else {
        $(this).addClass('chosen');
        tagName = $('<span class="name"></span>').text($(this).text());
        tagSelected = $('<div class="tag_selected" data-id="' + target.data('id') + '"></div>');
        tagSelected.append(tagName);
        tagSelected.append("<img class='tag_close' src='images/close.png'>");
        $('.tag_chosen').append(tagSelected);
      }
      getActs();
    });
    $(".tag_chosen").on('click', '.tag_close', function(){
      var target, i$, ref$, len$, x;
      target = $(this.parentNode);
      for (i$ = 0, len$ = (ref$ = $('.tag_item')).length; i$ < len$; ++i$) {
        x = ref$[i$];
        if ($(x).data('id') === target.data('id')) {
          $(x).removeClass('chosen');
        }
      }
      this.parentNode.remove();
      getActs();
    });
    $('.timing').click(function(){
      $('.tag_item').removeClass('chosen');
      $('.tag_selected').remove();
      $('.sort_area .sort').removeClass('active');
      $('.time').addClass('active');
      getActs();
    });
    pagingHandler = function(){
      var i$, ref$, len$, x, timeBucket, timeId, currentPage;
      for (i$ = 0, len$ = (ref$ = $('.timing')).length; i$ < len$; ++i$) {
        x = ref$[i$];
        if ($(x).hasClass('active')) {
          timeBucket = $(x).data('id');
          break;
        }
      }
      timeId = '#' + timeBucket;
      $('.previous,.next').removeClass('disabled');
      for (i$ = 0, len$ = (ref$ = $(timeId + ' .paging')).length; i$ < len$; ++i$) {
        x = ref$[i$];
        if ($(x).parent().hasClass('active')) {
          currentPage = $(x).data('id');
        }
      }
      if (currentPage === 1) {
        $(timeId + ' .pagination .previous').addClass('disabled');
      }
      if (currentPage === $(timeId + ' .paging').length) {
        $(timeId + ' .pagination .next').addClass('disabled');
      }
    };
    pagingHandler();
    $(".pagination").on('click', '.paging', function(e){
      var i$, ref$, len$, x, timeBucket, timeId, target;
      for (i$ = 0, len$ = (ref$ = $('.timing')).length; i$ < len$; ++i$) {
        x = ref$[i$];
        if ($(x).hasClass('active')) {
          timeBucket = $(x).data('id');
          break;
        }
      }
      timeId = '#' + timeBucket;
      e.preventDefault();
      target = $(e.target.parentNode);
      if (target.hasClass('active')) {
        return;
      }
      $(timeId + ' .pagination li').removeClass('active');
      target.addClass('active');
      pagingHandler();
      getActs(true);
    });
    $(".pagination").on('click', '.previous,.next', function(e){
      var i$, ref$, len$, x, timeBucket, timeId, target;
      for (i$ = 0, len$ = (ref$ = $('.timing')).length; i$ < len$; ++i$) {
        x = ref$[i$];
        if ($(x).hasClass('active')) {
          timeBucket = $(x).data('id');
          break;
        }
      }
      timeId = '#' + timeBucket;
      e.preventDefault();
      target = $(e.target);
      if (target.parent().hasClass('disabled')) {
        return;
      }
      for (i$ = 0, len$ = (ref$ = $(timeId + ' .paging')).length; i$ < len$; ++i$) {
        x = ref$[i$];
        if ($(x).parent().hasClass('active')) {
          if (target.data('id') === 0) {
            $(x).parent().prev().addClass('active');
            $(x).parent().removeClass('active');
            break;
          } else if (target.data('id') === -1) {
            $(x).parent().next().addClass('active');
            $(x).parent().removeClass('active');
            break;
          }
        }
      }
      pagingHandler();
      getActs(true);
    });
    getActs = function(pageIsChanged){
      var i$, ref$, len$, x, timeBucket, timeId, pageNum, tags, orderBy;
      for (i$ = 0, len$ = (ref$ = $('.timing')).length; i$ < len$; ++i$) {
        x = ref$[i$];
        if ($(x).hasClass('active')) {
          timeBucket = $(x).data('id');
          break;
        }
      }
      timeId = '#' + timeBucket;
      if (pageIsChanged !== true) {
        pageNum = 1;
      } else {
        for (i$ = 0, len$ = (ref$ = $(timeId + ' .paging')).length; i$ < len$; ++i$) {
          x = ref$[i$];
          if ($(x).parent().hasClass('active')) {
            pageNum = $(x).data('id');
          }
        }
      }
      tags = [];
      for (i$ = 0, len$ = (ref$ = $(timeId + ' .tag_selected')).length; i$ < len$; ++i$) {
        x = ref$[i$];
        tags.push($(x).data('id'));
      }
      for (i$ = 0, len$ = (ref$ = $(timeId + ' .sort')).length; i$ < len$; ++i$) {
        x = ref$[i$];
        if ($(x).hasClass('active')) {
          orderBy = $(x).data('id');
          break;
        }
      }
      $('.activities-template').stop();
      sHomepageUpdate(timeBucket, tags, orderBy, pageNum);
    };
    sHomepageUpdate = function(timeBucket, tags, orderBy, pageNum){
      var option;
      option = {
        timeBucket: timeBucket,
        tags: tags,
        orderBy: orderBy,
        pageNum: pageNum
      };
      $.get('/s-homepage-update', option, function(data){
        var timeId, pageNext, i$, to$, i, pageLi, pageA;
        $('.activities-template').html(data.activitiesTemplate);
        $('.activities-template').hide();
        $('.activities-template').fadeIn();
        timeId = '#' + timeBucket;
        $(timeId + ' .paging').parent().remove();
        pageNext = $(timeId + ' .next');
        $(timeId + ' .next').remove();
        for (i$ = 1, to$ = data.numOfPages; i$ <= to$; ++i$) {
          i = i$;
          if (i === pageNum) {
            pageLi = $('<li class="active">');
          } else {
            pageLi = $('<li>');
          }
          pageA = $('<a class="paging" href="#" data-id="' + i + '">' + i + '</div>');
          pageLi.append(pageA);
          $(timeId + ' .pagination').append(pageLi);
        }
        $(timeId + ' .pagination').append(pageNext);
        pagingHandler();
      });
    };
  });
}).call(this);
