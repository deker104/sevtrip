$(document).ready(function(){ 
	$.datepicker.setDefaults($.datepicker.regional["ru"]);
    $('.datepicker').datepicker();
        $('.carousel').carousel();
        $('.parallax').parallax();
         $('.tooltipped').tooltip();

  });

$("button#answer").click(function(){
	// $("div.section.white")[0].innerHTML = "";
	data = {
			child: child_check,
			invalid: invalid_check,
			invalid2: invalid2_check,
			age: Number($("input#age")[0].value),
			personal: $("select#personal").select2('data')[0].text == "Не выбрано" ? null : $("select#personal").select2('data')[0].text,
			physReady: $("select#selectPhys").select2('data')[0].text == "Не выбрано" ? null : $("select#selectPhys").select2('data')[0].text,
			Time: $("select#theTime").select2('data')[0].text == "Не выбрано" ? null : $("select#theTime").select2('data'),

	};
	 $.ajax({
		 data: JSON.stringify(data),
		 url: "/",
		 method: POST,
		 dataType: 'json'
	}).always(function(data) {
		$("div.section.white")[0].innerHTML = data.html;
		console.log('Tbi JLox');
	});
});