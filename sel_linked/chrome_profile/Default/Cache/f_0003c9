/*
Copyright (c) 2005 JSON.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The Software shall be used for Good, not Evil.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

/*
    The global object JSON contains two methods.

    JSON.stringify(value) takes a JavaScript value and produces a JSON text.
    The value must not be cyclical.

    JSON.parse(text) takes a JSON text and produces a JavaScript value. It will
    throw a 'JSONError' exception if there is an error.
*/
var JSON = {
    copyright: '(c)2005 JSON.org',
    license: 'http://www.crockford.com/JSON/license.html',
/*
    Stringify a JavaScript value, producing a JSON text.
*/
    stringify: function (v) {
        var a = [];

/*
    Emit a string.
*/
        function e(s) {
            a[a.length] = s;
        }

/*
    Convert a value.
*/
        function g(x) {
            var c, i, l, v;

            switch (typeof x) {
            case 'object':
                if (x) {
                    if (x instanceof Array) {
                        e('[');
                        l = a.length;
                        for (i = 0; i < x.length; i += 1) {
                            v = x[i];
                            if (typeof v != 'undefined' &&
                                    typeof v != 'function') {
                                if (l < a.length) {
                                    e(',');
                                }
                                g(v);
                            }
                        }
                        e(']');
                        return;
                    } else if (typeof x.valueOf == 'function') {
                        e('{');
                        l = a.length;
                        for (i in x) {
                            v = x[i];
                            if (typeof v != 'undefined' &&
                                    typeof v != 'function' &&
                                    (!v || typeof v != 'object' ||
                                        typeof v.valueOf == 'function')) {
                                if (l < a.length) {
                                    e(',');
                                }
                                g(i);
                                e(':');
                                g(v);
                            }
                        }
                        return e('}');
                    }
                }
                e('null');
                return;
            case 'number':
                e(isFinite(x) ? +x : 'null');
                return;
            case 'string':
                l = x.length;
                e('"');
                for (i = 0; i < l; i += 1) {
                    c = x.charAt(i);
                    if (c >= ' ') {
                        if (c == '\\' || c == '"') {
                            e('\\');
                        }
                        e(c);
                    } else {
                        switch (c) {
                        case '\b':
                            e('\\b');
                            break;
                        case '\f':
                            e('\\f');
                            break;
                        case '\n':
                            e('\\n');
                            break;
                        case '\r':
                            e('\\r');
                            break;
                        case '\t':
                            e('\\t');
                            break;
                        default:
                            c = c.charCodeAt();
                            e('\\u00' + Math.floor(c / 16).toString(16) +
                                (c % 16).toString(16));
                        }
                    }
                }
                e('"');
                return;
            case 'boolean':
                e(String(x));
                return;
            default:
                e('null');
                return;
            }
        }
        g(v);
        return a.join('');
    },
/*
    Parse a JSON text, producing a JavaScript value.
*/
    parse: function (text) {
        return (/^(\s+|[,:{}\[\]]|"(\\["\\\/bfnrtu]|[^\x00-\x1f"\\]+)*"|-?\d+(\.\d*)?([eE][+-]?\d+)?|true|false|null)+$/.test(text)) &&
            eval('(' + text + ')');
    }
};
// http://www.webreference.com/js/column8/functions.html
function setCookie(name,value,path,expires,domain,secure){
	document.cookie=name+'='+escape(value)+((expires)?';expires='+expires.toGMTString():'')+
		((path)?';path='+path:';path=/')+((domain)?';domain='+domain:'')+((secure)?'; secure':'');
}
function getCookie(name){
	var dc=document.cookie;
	var prefix=name+'=';
	var begin=dc.indexOf('; '+prefix);
	if (begin==-1) {
		begin=dc.indexOf(prefix);
		if(begin!=0) return null;
	} else
		begin+=2;
	var end=document.cookie.indexOf(';',begin);
	if (end==-1) end=dc.length;
	return unescape(dc.substring(begin+prefix.length,end));
}
function dateTime() {
	var t=this;
	t.lang_src = 'en';
	t.lang_clt = 'en';
	t.mmm = { 'en':['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'] };
	t.mmm2i = {};
	t.re_yyyy = /^(\d\d)(\d\d)$/;
	t.re_iso8601 = /^(\d\d\d\d)\-(\d\d)\-(\d\d)[\sT](\d\d):(\d\d):(\d\d)Z$/;
	t.re_disp1   = /^(\w\w\w)\s(\d+),\s(\d\d\d\d)\sat\s(\d+):(\d+)\s*([ap])m?$/;//Jan 19, '11 at 10:26p
	t.re_disp2   = /^([A-Za-z]{3})\s(\d+),\s'(\d{2})\sat\s(\d+):(\d+)\s*([ap])m?$/;
	t.init_mmm2i = function() {
		for (var lang in t.mmm ) {
			t.mmm2i[lang] = [];
			for (var i=0,l=t.mmm[lang].length;i<l;i++) {
				t.mmm2i[lang][ t.mmm[lang][i].toLowerCase() ] = i;
			}
		}
	}
	t.init = function() {
		t.init_mmm2i();
	}
	t.local_text_for_any = function(any,yy,ap) {
		var myDt = t.date_for_any(any);
		var str = t.local_text_for_dt( myDt,yy,ap );
		return str;
	}
	t.local_text_for_dt = function(myDt,yy,ap) {
		if ( ! myDt ) return '';
		var str = t.mmm[t.lang_clt][ myDt.getMonth() ]+' '+myDt.getDate()+', ';
		if ( yy ) {
			var matches = t.re_yyyy.exec( myDt.getFullYear() );
			str += "'" + matches[2];
		}
		else str += myDt.getFullYear();
		var hr24 = myDt.getHours();
		var hr12
			= hr24==0 ? 12
			: hr24>12 ? hr24 - 12
			: hr24;
		var mm = myDt.getMinutes();
		if ( mm < 10 ) mm = '0'+mm;
		str += ' at '+hr12 +':'+ mm;
		if (ap) str += hr24 > 11 ? 'p' : 'a';
		else    str += hr24 > 11 ? ' pm' : ' am';
		return str;
	};
	t.date_for_any = function(any) {
		if ( !any ) return '';
		var dtinfo = {};
		var mtype = 0;
		var matches = t.re_disp1.exec( any );
		if ( matches != null && matches.length==7 ) mtype = 1;
		else matches = t.re_disp2.exec( any );
		if ( mtype==0 && matches != null && matches.length==7 ) mtype = 2;
		else if ( mtype==0 ) matches = t.re_iso8601.exec( any );
		if ( mtype==0 && matches != null && matches.length==7 ) mtype = 3;
		if ( mtype==0 ) return;
		myDt = new Date();
		if ( mtype == 1 || mtype == 2 ) {
			var yyyy = matches[3];
			if (yyyy < 100) {
				if ( yyyy < 40 ) yyyy = '20'+yyyy;
				else yyyy = '19'+yyyy;
			}
			var hr24 = matches[4];
			if ( matches[6]=='p' && hr24!=12 ) hr24 = parseInt(hr24) + 12;
			if ( matches[6]=='a' && hr24==12 ) hr24 = 0;
			myDt.setUTCFullYear( yyyy );
			myDt.setUTCMonth( t.mmm2i[t.lang_src][ matches[1].toLowerCase() ] );
			myDt.setUTCDate( matches[2] );
			myDt.setUTCHours( hr24 );
			myDt.setUTCMinutes( matches[5] );
			myDt.setUTCSeconds( 0 );
		} else if ( mtype == 3 ) {
			myDt.setUTCFullYear( matches[1] );
			myDt.setUTCMonth( matches[2]-1 );
			myDt.setUTCDate( matches[3] );
			myDt.setUTCHours( matches[4] );
			myDt.setUTCMinutes( matches[5] );
			myDt.setUTCSeconds( matches[6] );
		}
		return myDt;
	}
}
function delCookie(name,path,domain){
	if (getCookie(name)) {
		document.cookie=name+'='+
		((path)?';path='+path:'') +
		((domain)?';domain='+domain:'') +
		';expires=Thu, 01-Jan-07 00:00:01 GMT';
	}
}
function pgFwd(pg,c2pg) {
	// var tPgFwd    = new pgFwd(,); tPgFwd.init();
	var d=document,t=this;
	t.pg   = pg;
	t.c2pg = c2pg;
	t.init = function() {
		var uri = window.location.href;
		var cap = uri.match(/(http:\/\/.+\/\d{4}\/\d{2}\/[^/]+\/\d\d[^/]{26})\/(\d{8}[^/]{26})#(\d{8}[^/]{26})/);
		if (!cap) return;
		var base = cap[1];
		var mcid = cap[2];
		if (!mcid) return;
		if (t.c2pg[mcid][1] && t.c2pg[mcid][1] != t.pg) {
			var pguri = base;
			if (t.c2pg[mcid][1] != 1 ) {
				pguri = pguri + '/nested/page/'+ t.c2pg[mcid][1];
			}
			pguri = pguri + '/' + mcid + '#' + mcid;
			window.location = pguri;
		}
	}
}
function mSort(ul,msgs,msgs_meta) {
	// SO QA1134976
	var d=document,t=this;
	t.ul  = ul;
	t.ids = [];
	t.map = {};
	t.cache_loaded = 0;
	t.check_cache = function() {
		//if (t.cache_loaded == 1) return;
		var ul   = d.getElementById(t.ul);
		var lis  = ul.getElementsByTagName("LI");
		var map  = t.map;
		//var ids  = t.ids;
		var ids  = [];
		for(var i=0, l=lis.length; i < l; i++) {
			//var title = lis[i].title;
			var cap   = lis[i].id.match(/(.+)_li/);
			var cid   = cap[1];
			var info  = $('#'+cid).attr('title');
			var parts = info.split(',');
			//if (! map[ title ]) {
				map[cid] = {
					cron  : parts[1],
					nest  : parts[2],
					html  : lis[i].innerHTML,
					title : lis[i].title,
					info  : info
				};
				ids[i] = cid; //title;
			//}
		}
		t.map = map;
		t.ids = ids;
		t.cache_loaded = 1;
	};
	t.sort_responses = function(type) {
		t.check_cache();
		if (type != 'newest' && type != 'oldest' && type != 'rnested') {
			type = 'nested';
		}
		var ids = t.ids;
		if (type == 'nested') { ids = ids.sort(
			function(a,b) { return t.map[a]['nest'] - t.map[b]['nest'] } )
		} else if (type == 'rnested') { ids = ids.sort(
			function(a,b) { return t.map[b]['nest'] - t.map[a]['nest'] } )
		} else if (type == 'newest') { ids = ids.sort(
			function(a,b) { return t.map[b]['cron'] - t.map[a]['cron'] } )
		} else if ( type == 'oldest') { ids = ids.sort(
			function(a,b) { return t.map[a]['cron'] - t.map[b]['cron'] } )
		}
		var ul  = document.getElementById(t.ul);
		var lis = lis = ul.getElementsByTagName("LI");
		for(var i = 0, l = ids.length; i < l; i++) {
			lis[i].innerHTML = t.map[ ids[i] ]['html'];
			lis[i].title     = t.map[ ids[i] ]['title'];
			lis[i].id        = ids[i] + '_li';
		}
		if (type == 'nested' || type == 'rnested') {
			//$('div.indent').each(function(idx,itm) {$('#'+itm.id).css('margin-left', itm.title * 15 + 'px')});
			//$('.indent1').each( function(idx,itm) {$('#'+itm.id).css('padding-left', itm.title * 26 + 'px')} );
			$('.indent1').each( function(idx,itm) {
				var dep = $('#'+itm.id).attr('class').match(/\bindentd(\d+)\b/)[1];
				$('#'+itm.id).css('padding-left', ( dep * 26 ) + 'px')
			} );
			$('div.indent2').each( function(idx,itm) {
				var dep = $('#'+itm.id).attr('class').match(/\bindentd(\d+)\b/)[1];
				$('#'+itm.id).css('padding-left', (( dep * 26 ) + 30) + 'px')
			} );
		} else {
			//$('div.indent').css('margin-left',0);
			$('.indent1').css('padding-left',0);
			$('div.indent2').css('padding-left',30);
		}
		$('a.sortTab').removeClass('youarehere');
		$('#sort_'+type).addClass('youarehere');
	};
};
function sToggler() {
	var t=this;
	t.toggle = function(cont_id,ctl_id,show_text,hide_text) {
		if ($('#'+cont_id).css('display')=='none') {
			$('#'+ctl_id).html(hide_text);
			$('#'+cont_id).show();
		} else {
			$('#'+ctl_id).html(show_text);
			$('#'+cont_id).hide();
		}
	}
	t.toggle2 = function(cont_sel,ctl_sel,show_text,hide_text,cont2_sel) {
		if ($(cont_sel).css('display')=='none') {
			$(ctl_sel).html(hide_text);
			$(cont_sel).show();
			if (cont2_sel) { $(cont2_sel).hide(); }
		} else {
			$(ctl_sel).html(show_text);
			$(cont_sel).hide();
			if (cont2_sel) { $(cont2_sel).show(); }
		}
	}
}
function gUsDisplay(usrs_more_id,usrs_more_av_html,usrs_more_av_info) {
	var t=this;
	t.flag_loaded = 0;
	t.usrs_more_id = usrs_more_id;
	t.usrs_more_av_html = usrs_more_av_html;
	t.usrs_more_av_info = usrs_more_av_info;
	t.lazy_init = function() {
		if ( t.flag_loaded > 0 ) { return; };
		for(var i=0,l=t.usrs_more_av_info.length; i<l; i++) {
			var u_info = t.usrs_more_av_info[i];
			var uri = 'http://www.gravatar.com/avatar/' + u_info['md5'] + '?s=40&d=identicon&r=R';
			var id  = 'g_u_av_img_' + u_info['idx'];
			$('#'+id).attr('src',uri);
		}
		//$('#'+t.usrs_more_id).html( t.usrs_more_av_html );
		t.flag_loaded = 1;
	}
}
function qToggler() {
	var t=this;
	t.hide_text = '- Hide quoted text -';
	t.show_text = '- Show quoted text -';
	t.toggle = function(obj) {
		var qcid_ctl = obj.id;
		var qcid = qcid_ctl.split('__')[0];
		if ($('#'+qcid).css('display')=='none') {
			$('#'+qcid_ctl).html(t.hide_text);
			$('#'+qcid).show();
		} else {
			$('#'+qcid_ctl).html(t.show_text);
			$('#'+qcid).hide();
		}
	}
	t.init = function(pg_type) {
		if (pg_type == 't') {
			$('.qc_cnt').hide();
			$('.qc_ctl').html(t.show_text);
		} else $('.qc_ctl').html(t.hide_text);
		$('.qc_ctl').bind('click',function() {
			iQToggler.toggle(this);return false;
		});
	}
}
function rToggler() {
	// var iRToggler = new rToggler;iRToggler.init();
	var t=this;
	t.toggle_thin = function(obj) {
		var mcid = obj.id.split('_')[0];
		$('#'+mcid+'_thinhead').css('display','none');
		$('#'+mcid+'_fullhead').css('display','');
		$('#'+mcid+'_content').css('display','');
	}
	t.toggle_full = function(obj) {
		var mcid = obj.id.split('_')[0];
		$('#'+mcid+'_fullhead').css('display','none');
		$('#'+mcid+'_content').css('display','none');
		$('#'+mcid+'_thinhead').css('display','');
	}
	t.init = function() {
		if (getCookie('rbody')=='h') {
			$('.rbody').css('display','none');
			$('.tr_head_thin').css('display','');
			$('#ctl_rbody_showhide').html('collapsed')
		};
		$('.rc_ctl_full').bind('click',function() {
			iRToggler.toggle_full(this);return false;
		});
		$('.rc_ctl_thin').bind('click',function() {
			iRToggler.toggle_thin(this);return false;
		});
	}
}
function user_prefs(pg_type) {
	var t=this;
	t.pg_type = pg_type;
	t.tog_sb_u_list = function() {
		if ($('#user_list_content').css('display') == 'none') {
			$('#user_list_content').css('display','');
			$('#ctl_ulist_showhide').html('on');
			$('#sb_user_style').css('display','');
			setCookie('ulist','s')
		} else {
			$('#user_list_content').css('display','none');
			$('#ctl_ulist_showhide').html('off');
			$('#sb_user_style').css('display','none');
			setCookie('ulist','h')
		};
	};
	t.tog_sb_u_style = function(show) {
		if (show != 'a' && show != 'n') {
			if ($('#user_list_avatars').css('display')=='none') show = 'a';
			else show = 'n';
		}
		if (show == 'a') {
			$('#user_list_names').css('display','none');
			$('#user_list_avatars').css('display','');
			$('#ctl_ulist_style').html('avatars');
			setCookie('ustyle','a')
		} else {
			$('#user_list_avatars').css('display','none');
			$('#user_list_names').css('display','');
			$('#ctl_ulist_style').html('names');
			setCookie('ustyle','n')
		};
	}
	t.init = function() {
		if (t.pg_type == 'g' && getCookie('ulist')=='h')  t.tog_sb_u_list();
		if (getCookie('ustyle')=='n') t.tog_sb_u_style('n');
	}
}
function gbOSch() {
	document.write('<span class="inactive">|</span>  <a href="#" class="topbar_nav" onclick="window.external.AddSearchProvider(\'http://grokbase.com/opensearch.xml\');return false" title="Add Grokbase OpenSearch to browser">Add</a>');
}
function listUtils() {
	var d=document,t=this;
	t.toggle = function(key) {
		if (!key) { return; };
		var id_list = '#'+key+'_list';
		var id_icon = '#'+key+'_ico';
		if ( $( id_list ).css('display')=='none') {
			$(id_list).show();
			$(id_icon).html('&#9660;');
			$(id_icon).html('<span style="font-size:13px;margin-left:0px;">&#9660;</span>');
		} else {
			$(id_list).hide();
			$(id_icon).html('&#9654;');
			$(id_icon).html('<span style="font-size:10px;margin-left:3px">&#9654;</span>');
			t.hideMore(key);
		}
	}
	t.initMore = function(key) {
		if ( $('#'+ key +'_list li').length > 5 ) {
			$('#'+key+'_more').show();	
		}
	}
	t.hideMore = function(key) {
		var hide_them = 0;
		$('#'+ key + '_list li').each(function(index) {
			if ( index > 4 ) {
				if (!$(this).hasClass('moreLi')) {
					$(this).addClass('moreLi');
				}
				hide_them = hide_them+1;
   			}
		});
		if (hide_them>0) {
			var id_more = '#'+key+'_more';
			if($(id_more).css('display')=='none') {
				$(id_more).show();
			}
		}
	}
	t.showMore = function(key) {
		$('#'+ key + '_list li').each(function(index) {
			if ($(this).hasClass('moreLi')) {
				$(this).removeClass('moreLi');
			}
		});
		$('#'+key+'_more').hide();
	}
}
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
(function() {
  var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
  po.src = 'https://apis.google.com/js/plusone.js';
  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
})();

function gMap() {
	var t=this;
	t.mapOptions={mapTypeId:google.maps.MapTypeId.ROADMAP};
	t.mapFoci = {
		world:{latlon:[18.0,0.0],zoom:2},us:{latlon:[37.0625,-95.677068],zoom:4},
		na:{latlon:[52.268157,-102.832031],zoom:3},sa:{latlon:[-25.00,-63.63],zoom:3},
		eu:{latlon:[49.61071,15.029297],zoom:4},as:{latlon:[45,95],zoom:3},
		af:{latlon:[0,20],zoom:3},au:{latlon:[-25.641526,134.296875],zoom:4},
	};
	t.initMapFoci = function() {
		for (key in t.mapFoci) {
			var ll = t.mapFoci[key]['latlon'];
			t.mapFoci[key]['gll'] = new google.maps.LatLng( ll[0], ll[1] );
		}
	};
	t.focus = function( location ) {
		if ( t.mapFoci[location] ) {
			var loc = t.mapFoci[location];
			t.map.setCenter( loc['gll'] );
			t.map.setZoom( loc['zoom'] );
			if ( location != 'world' ) {
				$('.loc_continent').hide();
				if ( location == 'us' ) {
					$('.loc_continent_na').show();
					$('.loc_country').hide();
					$('.loc_country_' + location ).show();
				} else {
					$('.loc_continent_' + location ).show();
					$('.loc_country').show();
				}
			} else {
				$('.loc_continent').show();
				$('.loc_country').show();
			}
			$('a.nav1').removeClass('youarehere');
			$('#nav1_' + location).addClass('youarehere');
		}
	}
	t.map = '';
	t.init = function( markers ) {
		t.initMapFoci();
		t.mapOptions['center'] = t.mapFoci['world']['gll'];
		t.mapOptions['zoom'] = t.mapFoci['world']['zoom'];
		t.map = new google.maps.Map(document.getElementById("map_canvas"), t.mapOptions);
		t.addMarkers( markers );
	}
	t.addGoogMarker = function( map, markerLatLng, markerTitleString, markerContentString ) {
		var googMarkerLatlng = new google.maps.LatLng( markerLatLng[0], markerLatLng[1] );
		var infowindow    = new google.maps.InfoWindow({
			content: markerContentString
		});
		var marker = new google.maps.Marker({
			position: googMarkerLatlng,
			map: map,
			title:markerTitleString
		});
		google.maps.event.addListener(marker, 'click', function() {
			infowindow.open(map,marker);
		});
	};
	t.addMarkers = function( markers ) {
		for (i=0,l=markers.length;i<l;i++) {
			var info = markers[i];
			t.addGoogMarker( t.map, info['latlon'], info['title'], info['content'] );
		}
	}
};