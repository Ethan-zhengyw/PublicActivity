/****************************************/
/****************************************/
/* 	轮播中的左键点击    */
var time = 0;
var left_click_btn = window.setInterval("clock()", 1000);
function clock() {
	++time;
	$('.carousel-control.left').click();
	if (time == 10) {
		window.clearInterval(left_click_btn);
	}
}
/*****************************************/
/*****************************************/
/* 	注册过程忽略用户名   */
function signUp() {
	// chakan zhuce 
	$('.register_submit.active').click();
	console.log($('input[name="register_userName"]').attr('placeholder'));
	if ($('input[name="register_userName"]').attr('placeholder') == '别忘记这里.....')
		console.log('存在空格没填判断正确');
}
/*****************************************/
/*****************************************/
/* 	选择标签   */
function clickTags() {
	$('.tagbtn.btn-addTag.btn.btn-default').eq(0).click();
	var text = $('.tagbtn.btn-addTag.btn.btn-default').eq(0).text();
	if ($('.bootstrap-tagsinput').text().indexOf(text) > 0)
		console.log("tag is put ~");
}
