//获取系统时间，将时间以指定格式显示到页面。
	function systemTime(){//获取系统时间。
		var dateTime=new Date();
//		var hh=dateTime.getHours();
//		var mm=dateTime.getMinutes();
//		var ss=dateTime.getSeconds();
		var year=dateTime.toLocaleString();
		//分秒时间是一位数字，在数字前补0。
		//将时间显示到ID为time的位置，时间格式形如：19:18:02
		document.getElementById("time").innerHTML=year+" ";
		//每隔1000ms执行方法systemTime()。
		setTimeout("systemTime()",1000);
	}

	function extra(x){	//补位函数。
		if(x < 10){//如果传入数字小于10，数字前补一位0。
			return "0" + x;
		}else{
			return x;
		}
	}