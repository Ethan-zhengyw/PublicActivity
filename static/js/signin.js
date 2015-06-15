$(document).ready(function() {

	$('#login_form').submit(function(event) {
		// 隐藏提示出错的红色*
		$(this).find('span').removeClass('active');
		$(this).find('input').each(function(index, domEle) {
			if ($(domEle).val() == "") {
				$(domEle).next().addClass('active');
				event.preventDefault();
			}
		});
	});
});