# -*- coding: utf-8 -*-
import js2py
downloadItem= '''
var downloadItem = function(hmpeSeqNo, blbdSeqNo){
	$.ajax({
	    type		: "GET",
	    url			: "/download.do",
	    data		: {
						"hmpeSeqNo"		: hmpeSeqNo
	    			},
	    dataType	: "json",
        success		: function(result) {
	    	if(result.result == "success"){
	    		location.href="/dev/hanaifFileDownload.jsp?seq=" + blbdSeqNo;
	    	}else{
	    		alert("다운로드에 실패하였습니다.");
	    	}
	    },
	    error		: function() {
	    	alert("다운로드에 실패하였습니다.");
	    }
	});
}
'''

if __name__ == '__main__':
    download = js2py.eval_js(downloadItem)
    download(34840, 101122)
