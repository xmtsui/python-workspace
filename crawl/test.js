//股指和国债产品代码
var P_IF = "IF";
var P_TF = "TF";

var product = "";

//获得URL参数
var isDebug=false;

 var xmlDoc=null;
var data = null; //document.getElementById("marketDatas");
//bit 表示小数点几位
  //得到最小值
 var MIN=function(arr,bit){
      var maxValue=0;
	  arr.sort(function compare(a,b){return a-b});
	 if(arr.length>0){
          maxValue=arr[0]*1;
	      maxValue=maxValue.toFixed(bit);
	 }
     return maxValue;
  }
  //得到最大值
  var MAX=function(arr,bit){
      var maxValue=0;
	  arr.sort(function compare(a,b){return b-a});
	 if(arr.length>0){
           maxValue=arr[0]*1;
	   maxValue=maxValue.toFixed(bit);
	 }
     return maxValue;
  }
//求和
  var SUM=function(arr,bit){
      var sum=0;
	  for(var i=0;i<arr.length;i++){
           sum+=arr[i]*1;
	  }
	  sum=sum.toFixed(bit);
	  return sum;
  }
//解析xml文件
//@update_date  :2010-02-09 18:51
//WCM每天生成文档的格式为:2010/01/01 月和日的时间必须是二位来得到文件的地址

/* *********************wu.changsheng@trs.com.cn修改开始******************* */
//@update_date:2010-04-22 19:45
var xmlFiletoPath="";
var count=0;
var XML_FILE_DATE="";
var ccpmObj={
    XML_NAME:"index.xml",
	SPLIT:"/",
	ONEDAY:24*60*60*1000,
	getLocalDate:function(_Parameter){
	  var __Parameter=_Parameter;
     if(__Parameter <10){
      __Parameter="0"+_Parameter;
	}
	 return __Parameter;
	},
    //参数类型为:日期
	getXMLPath:function(dt){
	   var _month=this.getLocalDate(dt.getMonth()+1);
	   var _date=this.getLocalDate(dt.getDate());
	   var __year=dt.getYear();
	   __year=(__year<1900)?(1900+__year):__year;
	   XML_FILE_DATE=__year+""+_month+""+_date;
	   if(isDebug){
	     alert("交易日历:"+XML_FILE_DATE);
	   }
	   var XML_FILE=__year+""+_month+this.SPLIT+_date+this.SPLIT+this.XML_NAME;
	   return XML_FILE;
	},
     //参数类型为:日期
	getPresenceDataToPath:function(dt){
        var XML_FILE=this.getXMLPath(dt);
		 if(isDebug){
		    alert("getPresenceDataToPath()加载的XML文件为:"+XML_FILE);
		  }
        var _loadXml=loadXml(XML_FILE);
        if(isDebug){
		   alert(typeof(_loadXml));
		}
		if(typeof(_loadXml) == "boolean"){
			   count++;
			   if(count>15){XML_FILE_DATE="";return false;}
               this.getPresenceDataToPath(new Date(dt-this.ONEDAY));
		 }else{
		    xmlFiletoPath= XML_FILE;
			return true;
		 }
	}
}
/**
  *通过jquery解析成交持仓排名的数据201008-20@wcs
  */
//对象扩充:Array
//一个数组去除重复
Array.prototype.delRepeat=function(){
	    var newArray=[];
	    var provisionalTable = {};
	    for (var i = 0, item; (item= this[i]) != null; i++) {
	        if (!provisionalTable[item]) {
	            newArray.push(item);
	            provisionalTable[item] = true;
	        }
	    }
	    return newArray;
}

function ajaxCCPMXML(XML_FILE){
   if(XML_FILE == null)return false;
   var __date=XML_FILE.split("/");
   var dateStr=__date[0]+""+__date[1];
   var showHtml="";
   var top='<table width="95%" border="1" align="center" cellpadding="0" cellspacing="0" bgcolor="E8E8E8" bordercolor="#FFFFFF" bordercolorlight="#000000" bordercolordark="#FFFFFF">'
   +'<tr align="center" valign="middle" bgcolor="#F9F9F9"> '
   +'<td align="left" class="table_first" width="50%" colspan="6" style="color: #2366A4">'
   +'&nbsp;&nbsp;合约:';
   var end='</table>';
   $.ajax({
			dataType:"xml",
			url: XML_FILE,
			success: function(xml){
			   //存放所有合约信息
               var __instrumentIds=new Array();
			   $(xml).find("data").each(function(){
					var instrumentId = $.trim($(this).find("instrumentId").text());
					//得到产品合约
					var instrumentProduct = $.trim($(this).find("productid").text()) || P_IF;

					//和选择的合约相同
					if (instrumentProduct === product){
						 __instrumentIds.push(instrumentId);		
					}
					
			   });
                __instrumentIds=__instrumentIds.delRepeat();
				
               //通过合约来查询相关的数据
			   for(var idsNumber=0;idsNumber<__instrumentIds.length;idsNumber++){
                 //构建显示页面
				     var dataHtml=top;
					 dataHtml+=__instrumentIds[idsNumber];
					 dataHtml+='</td> <td align="right" class="table_first" width="50%" colspan="6" style="color: #2366A4">交易日期:';
		             //dataHtml+=XML_FILE_DATE;
                              dataHtml+=dateStr;
		             dataHtml+='&nbsp;&nbsp;</td>'+'</tr>';
                     dataHtml+= '<tr align="center" valign="middle" bgcolor="#FFFFFF">'+
					  '<td align="center" class="table_first" colspan="4" style="color: #2366A4">成交量排名</td>'+
					  '<td align="center" class="table_first" colspan="4" style="color: #2366A4">持买单量排名</td>'+
					  '<td align="center" class="table_first" colspan="4" style="color: #2366A4">持卖单量排名</td>'+
                '</tr>'+
                '<tr align="center" valign="middle" bgcolor="F9F9F9">'+
					  '<td class="table_first" style="color: #2366A4">名次</td>'+
					  '<td class="table_first"  style="color: #2366A4">会员简称</td>'+
					  '<td class="table_first"  style="color: #2366A4">成交量</td>'+
					  '<td class="table_first"  style="color: #2366A4">比上交易日增减</td>'+
					  '<td class="table_first"  style="color: #2366A4">名次</td>'+
					  '<td class="table_first"  style="color: #2366A4">&nbsp;&nbsp;会员简称&nbsp;&nbsp;</td>'+
					  '<td class="table_first"  style="color: #2366A4">持买单量</td>'+
					  '<td class="table_first"  style="color: #2366A4">比上交易日增减</td>'+
					  '<td class="table_first"  style="color: #2366A4">名次</td>'+
					  '<td class="table_first"  style="color: #2366A4">会员简称</td>'+
					  '<td class="table_first"  style="color: #2366A4">持卖单量</td>'+
					  '<td class="table_first"  style="color: #2366A4">比上交易日增减</td>'+
                '</tr>';
				 var r=0;
				 var cjlpm={"par":[]};
				 var cmlpm={"par":[]};
				 var cmlpm1={"par":[]};
                 $(xml).find("data").each(function(){
					var instrumentNumber = $.trim($(this).find("instrumentId").text());
					//得到产品合约
					var instrumentProduct = $.trim($(this).find("productid").text()) || P_IF;

					 if(instrumentNumber == __instrumentIds[idsNumber] && instrumentProduct === product){
						 var _attrValue=$.trim($(this).attr("Value"));
                          var dataObj={
							   dataTypeId:$.trim($(this).find("dataTypeId").text()),
							   rank:$.trim($(this).find("rank").text()),
							   shortname:$.trim($(this).find("shortname").text()),
							   volume:$.trim($(this).find("volume").text()),
							   varVolume:$.trim($(this).find("varVolume").text()),
								partyid:$.trim($(this).find("partyid").text()),
								attrValue:_attrValue,
                                instrumentId:instrumentNumber
						   };
						  switch(parseInt(_attrValue)){
							  case 0:
								  cjlpm.par.push(dataObj);
							      break
                              case 1:
								  cmlpm.par.push(dataObj);
							      break
							  case 2:	
								  cmlpm1.par.push(dataObj);
							      break
						  }
					 }
			     });
				 //显示数据
				 var volumeArr=new Array();//成交量
		         var volumeAdd=new Array();//成交量增减
	             var strikeNumber=new Array();//持买单量
		         var strikeNumberAdd=new Array();//持买单量增减
	             var positionNumber=new Array();//持卖单量
		         var positionNumberAdd=new Array();//持卖单量增减
				 for(var cjlpmLength=0;cjlpmLength<cjlpm.par.length;cjlpmLength++){
				     //alert(cjlpm.par[cjlpmLength].attrValue);
                     //显示行
					  if(r%2==0){
				            dataHtml+='<tr valign="middle" bgcolor="#FFFFFF">'
			             }else{
				            dataHtml+='<tr valign="middle" bgcolor="F9F9F9">'
			              }
						 r+=1;
					    dataHtml=dataHtml+'<td  class="tb_content_right" style="word-break:break-all" align="right">'
						+cjlpm.par[cjlpmLength].rank+'</td>'+
					    '<td align="center" class="tb_content_right" style="word-break:break-all">'
						+cjlpm.par[cjlpmLength].partyid
						+'-'+cjlpm.par[cjlpmLength].shortname+'</td>'+
					    '<td  class="tb_content_right" style="word-break:break-all" align="right">'
						+cjlpm.par[cjlpmLength].volume+'</td>'
						+
					    '<td  class="tb_content_right" style="word-break:break-all" align="right">'
						+cjlpm.par[cjlpmLength].varVolume+'</td>'
						+
					    '<td  class="tb_content_right" style="word-break:break-all" align="right">'
						+cmlpm.par[cjlpmLength].rank+'</td>'+
					 '<td align="center" class="tb_content_right" style="word-break:break-all">'
						+cmlpm.par[cjlpmLength].partyid+'-'+cmlpm.par[cjlpmLength].shortname+'</td>'+
					 '<td  class="tb_content_right" style="word-break:break-all" align="right">'
						+cmlpm.par[cjlpmLength].volume+'</td>'+
					 '<td  class="tb_content_right" style="word-break:break-all" align="right">'
						+cmlpm.par[cjlpmLength].varVolume+'</td>'+
					 
					'<td  class="tb_content_right" style="word-break:break-all" align="right">'
					+cmlpm1.par[cjlpmLength].rank+'</td>'+
					'<td align="center" class="tb_content_right" style="word-break:break-all">'
					+cmlpm1.par[cjlpmLength].partyid+'-'+cmlpm1.par[cjlpmLength].shortname+'</td>'+
					'<td  class="tb_content_right" style="word-break:break-all" align="right">'
					+cmlpm1.par[cjlpmLength].volume+'</td>'+
					'<td  class="tb_content_right" style="word-break:break-all" align="right">'
					+cmlpm1.par[cjlpmLength].varVolume+'</td>'+
                 '</tr>';
                  volumeArr.push(cjlpm.par[cjlpmLength].volume);
		          volumeAdd.push(cjlpm.par[cjlpmLength].varVolume);
		          strikeNumber.push(cmlpm.par[cjlpmLength].volume);
		          strikeNumberAdd.push(cmlpm.par[cjlpmLength].varVolume);
		          positionNumber.push(cmlpm1.par[cjlpmLength].volume);
		          positionNumberAdd.push(cmlpm1.par[cjlpmLength].varVolume);
				}
				 if(isDebug){
				     alert("共保存数据个数:"+cjlpm.data.length);
			     }
				 //在这里做合计显示@date:2010-05-25 16:07
		var countNum='<tr align="center" valign="middle" bgcolor="F9F9F9">'+
					  '<td class="tb_content_right" style="color: #2366A4">合计</td>'+
					  '<td class="tb_content_right"  style="word-break:break-all">&nbsp</td>'+
					  '<td class="tb_content_right"   align="right" style="word-break:break-all">'+SUM(volumeArr,0)+'</td>'+
					  '<td class="tb_content_right"  align="right" style="word-break:break-all">'+SUM(volumeAdd,0)+'</td>'+
					  '<td class="tb_content_right"  style="color: style="word-break:break-all">&nbsp</td>'+
					  '<td class="tb_content_right"  style="color: style="word-break:break-all">&nbsp</td>'+
					  '<td class="tb_content_right"   align="right" style="word-break:break-all">'+SUM(strikeNumber,0)+'</td>'+
					  '<td class="tb_content_right"  align="right" style="word-break:break-all">'+SUM(strikeNumberAdd,0)+'</td>'+
					  '<td class="tb_content_right"  style="word-break:break-all">&nbsp</td>'+
					  '<td class="tb_content_right"  style="word-break:break-all">&nbsp</td>'+
					  '<td class="tb_content_right"   align="right" style="word-break:break-all">'+SUM(positionNumber,0)+'</td>'+
					  '<td class="tb_content_right"  align="right" style="word-break:break-all">'+SUM(positionNumberAdd,0)+'</td>'+
                '</tr>';
		         dataHtml+=countNum;
                 dataHtml+=end;
				 showHtml+=dataHtml;
			   }
				document.getElementById("textArea").innerHTML=showHtml;
 
			},

			complete:function(xhr, status){
				//$("#loading").remove();
			},
			error:function(xhr, status, errMsg){
				document.getElementById("textArea").innerHTML="当前交易日没有数据";
			}
     });
}
function parseXml(XML_FILE){
//页面第一次加载时XML_FILE为空,首先加载当天的数据
	if(XML_FILE==null){
          var dt=new Date();
		  if(!ccpmObj.getPresenceDataToPath(dt)){
		     var tA=document.getElementById("textArea");
             tA.innerHTML="当前交易日没有数据！";
			 return false;
		  }
		 XML_FILE=xmlFiletoPath;
	}
	 
    //增加ajax解析XML
     ajaxCCPMXML(XML_FILE);
	  if(isDebug){
		  alert("加载的XML文件为:"+XML_FILE);
		}

	
}

function getMax(value1,value2){
	return value1 > value2?value1:value2;
}

//去掉字符串的空格
String.prototype.trim = function(){
	return this.replace(/(^\s*)|(\s*$)/g, "");
}

//加载xml文件
function loadXml(XML_FILE , dataContainer){
	// 加载xml文档

	if(window.ActiveXObject)
	{
		xmlDoc = new ActiveXObject('Microsoft.XMLDOM');
		xmlDoc.async = false;
		xmlDoc.load(XML_FILE);
		var flag = xmlDoc.getElementsByTagName("data").length;
	    if(flag==0){
	       return false;
	     }
	}else if (document.implementation && document.implementation.createDocument)
	{
		xmlDoc = document.implementation.createDocument('', '', null);
		xmlDoc.async = false;
		xmlDoc.load(XML_FILE);
		flagff = xmlDoc.getElementsByTagName("data").length;
		
		if(isDebug){
	       alert("得到解析XML元素长度:"+flagff);
	   }
	   if(flagff==0)return false;
	}
   return xmlDoc;
}

function ondate()
{
	var datestr=document.getElementById("actualDate").value;

	//得到产品号
	product = $.trim($("#product").val());
	if (product === "") {
		alert("产品号不能为空， 请选择产品");
		return;
	}

	if(datestr!=null&&datestr!='') {
		var Searchday = new Date();
		var today= new Date();
		var year=datestr.substring(0,4);
		var mon=datestr.substring(5,7);
		var day=datestr.substring(8,10);
		Searchday.setYear(year);
		Searchday.setMonth(mon);
		Searchday.setDate(day);
		var week=new Date(year,mon-1,day).getDay()
		var search=year+""+mon+""+day;
		var search1=year+"-"+mon+"-"+day;

		var year1=today.getFullYear();
		var mon1=today.getMonth();
		mon1=mon1+1;
		var day1=today.getDate();
		var tod='';
		var tod1='';
		if(day1<10){
			tod=year1+""+(mon1 < 10 ? ("0" + mon1) : mon1)+""+"0"+day1;
			tod1=year1+"-"+(mon1 < 10 ? ("0" + mon1) : mon1)+"-"+"0"+day1;
		}else{
			tod=year1+""+(mon1 < 10 ? ("0" + mon1) : mon1)+""+day1;
			tod1=year1+"-"+(mon1 < 10 ? ("0" + mon1) : mon1)+"-"+day1;
		}

		if(search>tod) {
			alert("日期不能大于"+tod1+",请重新输入正确日期");
		} else {
			//if(week==6 || week==0) {
			//	alert(search1+"不是交易日,请重新输入正确日期");
			//} else {
				document.getElementById("Day").value=search;
				var path=search.substr(0,6)+"/"+search.substr(6,2)+"/index.xml";
				parseXml(path);
			//}
		}

	} else {
		alert("日期不正确，请重新输入正确日期")
	}
}
