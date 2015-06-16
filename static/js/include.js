$(function() {
	var currentUrl = window.location;

	$('a.profile').click(function(event) {
		// 显示隐藏菜单
		var posL = $(this).offset().left;
		var posT = $(this).offset().top;
		$('.hidden_menu').toggleClass('active').offset({top: posT + 61, left: posL - 48});

	});

	$('.storeUrl').click(function(event) {
		$(this).attr('href', + '#' +currentUrl);
	});

});