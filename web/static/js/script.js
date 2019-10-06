$(document).ready(function(){ 
	$.datepicker.setDefaults($.datepicker.regional["ru"]);
    $('.datepicker').datepicker();
    $('.carousel').carousel();
    $('.parallax').parallax();
    $('.tooltipped').tooltip();
	$("button#answer").click(function(){
	// $("div.section.white")[0].innerHTML = "";
		let data = {
			child: child_check,
			invalid: invalid_check,
			invalid2: invalid2_check,
			age: Number($("input#age")[0].value),
			personal: $("select#personal")[0].text == "Не выбрано" ? null : $("select#personal")[0].value,
			physReady: $("select#selectPhys")[0].text == "Не выбрано" ? null : $("select#selectPhys")[0].value,
			Time: $("select#theTime")[0].text == "Не выбрано" ? null : $("select#theTime")[0].value,

		};
		 $.ajax({
			 data: data,
			 url: "/",
			 method: 'POST',
			 dataType: 'json'
			}).always(function(data) {
				$("div#anketa")[0].innerHTML = data.html;
				console.log('Tbi JLox');
			});
});
});