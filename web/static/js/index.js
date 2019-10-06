$(document).ready(function(){ 
	$.datepicker.setDefaults($.datepicker.regional["ru"]);
    $('.datepicker').datepicker();
        $('.carousel').carousel();
        $('.parallax').parallax();
         $('.tooltipped').tooltip();

  });
const CL = console.log;
const POST = "POST", GET = "GET";
$("select#address").select2({
	width: 600,
	placeholder: "Адрес",
	ajax: {
		url: "DB/address.php",
		method: POST,
		dataType: "json"
	}
})
$("select#count_of_rooms").select2({width: 40})
$("select[id!=address][id!=count_of_rooms]").select2({width: 300})

$("select#address").on("select2:select", function(){
	data = $("select#address").select2('data')[0];
	if(!data.is_query)
	{
		$("input#count_of_floors")[0].value = data.Floor;
		$("input#Year")[0].value = data.Year;
		$("input#floor")[0].value = $("input#count_of_floors")[0].value == 1 ? 1 : "";
	}
});

const is_full = function()
{
	for(i = 0; i < $("input").length; i++)
	if($("input")[i].value < 0)
	{
		alert("Данные не могут быть отрицательными");
		return false;
	}
	if(!$("select#address").select2('data')[0])
	{
		alert("Не заполнен адрес недвижимости");
		return false;
	}
	if(!$("input#area")[0].value)
	{
		alert("Не заполнена площадь недвижимости");
		return false;
	}		
	if(!$("input#count_of_floors")[0].value)
	{
		alert("Не заполнено количество этажей в недвижимости");
		return false;
	}
	if(!$("input#floor")[0].value)
	{
		alert("Не заполнено этаж");
		return false;
	}
	if(!$("input#Year")[0].value)
	{
		alert("Не заполнен год постройки");
		return false;
	}
	if(Number($("input#count_of_floors")[0].value) < Number($("input#floor")[0].value))
	{
		alert("Этаж не может быть больше количества этажей");
		return false;
	}
	return true;
}
$("button#answer").click(function(){
	// $("div.section.white")[0].innerHTML = "";
	if(is_full())
	{
	data = {
			area: Number($("input#area")[0].value),
			count_of_rooms: Number($("select#count_of_rooms").select2('data')[0].text),
			address: $("select#address").select2('data')[0] ? $("select#address").select2('data')[0].Full_Address : null,
			count_of_floors: Number($("input#count_of_floors")[0].value),
			floor: Number($("input#floor")[0].value),
			lift: lift_check,
			trash: trash_check,
			gase: gase_check,
			area_of_kitchen: Number($("input#area_of_kitchen")[0].value),
			tolchok: $("select#tolchok").select2('data')[0].text == "Нет" ? null : $("select#tolchok").select2('data')[0].text,
			ceiling_height: Number($("input#ceiling_height")[0].value),
			year: Number($("input#Year")[0].value),
			walls: $("select#walls").select2('data')[0].text == "Неизвестно" ? null : $("select#walls").select2('data')[0].text,
			district: $("select#address").select2('data')[0] ? $("select#address").select2('data')[0].District : null,
			lodzhia: $("select#lodzhia").select2('data')[0].text == "Нет" ? null : $("select#lodzhia").select2('data')[0].text,
			ostanovka: ostanovka_check,
			parkovka: parkovka_check
	}
	 $.ajax({
		data: {
			data: JSON.stringify(data, '\n', ' '),
		},
		url: "DB/post.php",
		method: POST,
	});
	k = 1;
	answer = data.area;
	switch(data.district)
	{
		case 1: // Ленинский
			answer *= 37885;
			answer += data.count_of_rooms == 1 ? 140729 : data.count_of_rooms == 3 ? -63968 : data.count_of_rooms == null ? -127936 : 0;
			break; 

		case 2: // Октябрьский
			answer *= 42687;
			answer += data.count_of_rooms == 1 ? 158569 : data.count_of_rooms == 3 ? -72076 : data.count_of_rooms == null ? -144153 : 0;
			break; 

		case 3: // Индустриальный
			answer *= 40713;
			answer += data.count_of_rooms == 1 ? 151236 : data.count_of_rooms == 3 ? -68744 : data.count_of_rooms == null ? -137487 : 0;
			break; 

		case 4: // Устиновский
			answer *= 41544;
			answer += data.count_of_rooms == 1 ? 154324 : data.count_of_rooms == 3 ? -70148 : data.count_of_rooms == null ? -140295 : 0;
			break; 

		case 5: // Первомайский
			answer *=  41617;
			answer += data.count_of_rooms == 1 ? 154795 : data.count_of_rooms == 3 ? -70329 : data.count_of_rooms == null ? -140723 : 0;
			break; 

		default: 
			break;
	}
	if(data.tolchok == "Совмещённый")
		answer += -127936;
	switch(data.wall)
	{
		case "Кирпичный":
			answer += 233728;
			break;

		case "Керамические блоки":
			answer += 13749;
			break;

		case "Хрущёвка(Дерево)":
			answer += -109990;
			break;

		case "Сталинский":
			answer += 206230;
			break;

		case "Монолитный":
			answer += 233728;
			break;

		default:
			answer += 0;
			break;
	}
	if(data.ceiling_height)
		if(data.ceiling_height < 2.5)
			answer += -27497;
		else if(data.ceiling_height >= 2.5 && data.ceiling_height < 2.8)
			answer += 0;
		else if(data.ceiling_height >= 2.8 && data.ceiling_height < 3.4)
			answer += 51174;
		else
			answer += 82494;
	if(data.area_of_kitchen)
		if(data.area_of_kitchen < 6)
			answer += -63968;
		else if(data.area_of_kitchen >= 6 && data.area_of_kitchen < 9)
			answer += 0;
		else if(data.area_of_kitchen >= 9 && data.area_of_kitchen < 12)
			answer += 63968;
		else
			answer += 0;
	if(data.floor == data.count_of_floors)
		answer += -38381;
	else if(data.floor == 1)
		answer += -89556;
	else
		answer += 0;
	if(data.lift)
		k += 0.083;
	if(data.balcon == "Балкон")
		k += 0.083;
	if(data.balcon == "Лоджия")
		k += 0.083;
	if(data.gas)
		k += 0.083;
	if(data.ostanovka)
		k += 0.083;
	if(data.parkovka)
		k += 0.083;
	$("div.section.white")[0].innerHTML = "<h1>" + Math.ceil(answer * k) + "₽</h1>";
};
});