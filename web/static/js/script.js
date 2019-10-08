$(document).ready(function(){ 
	$.datepicker.setDefaults($.datepicker.regional["ru"]);
    $('.datepicker').datepicker();
    $('.carousel').carousel();
    $('.parallax').parallax();
    $('.tooltipped').tooltip();
    $('.materialboxed').materialbox();
	$("button#answer").click(function(){
		let data = {
			child: child_check,
			invalid: invalid_check,
			invalid2: invalid2_check,
			age: Number($("input#age")[0].value),
			personal1: $("#personal option")[1].selected,
			personal2: $("#personal option")[2].selected,
			personal3: $("#personal option")[3].selected,
			personal4: $("#personal option")[4].selected,
			physReady: $("select#selectPhys")[0].text == "Не выбрано" ? null : $("select#selectPhys")[0].value,
			Time: $("select#theTime")[0].text == "Не выбрано" ? null : $("select#theTime")[0].value,

		};
		console.log(data.personal);
		 $.ajax({
			 data: data,
			 url: "/",
			 method: 'POST',
			 dataType: 'json'
			}).always(function(data) {
				$("div#anketa")[0].innerHTML = data.html;
				$("#button_search")[0].innerHTML = '';
				console.log('Tbi JLox');
			});
});
});
