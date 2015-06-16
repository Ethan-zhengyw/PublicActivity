$(document).ready(function() {
	// 获取点击注册前的页面地址，藏在hash中
	var url = window.location.hash.split('#')[1];

	$('#login_form').submit(function(event) {
		event.preventDefault();
		var flag = true;
		// 隐藏提示出错的红色*
		$(this).find('span').removeClass('active');
		$(this).find('input').each(function(index, domEle) {
			if ($(domEle).val() == "") {
				$(domEle).next().addClass('active');
				flag = false;
			}
		});
		if (flag) {
			var csrftoken = getCookie('csrftoken');
			$.ajax({
				type: 'post',
				url: 'service/signin',
				data: {'email': $('#email').val(), 'password': $('#password').val(), 'csrfmiddlewaretoken': csrftoken},
				success: function(data) {
					var obj = eval("("+data+")");
					if (parseInt(obj['status']) === 1) {
						location.href = url;
					} else {
						$('#email').val('').attr('placeholder', 'Login Error');
					}
				}
			});
		}
	});
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

