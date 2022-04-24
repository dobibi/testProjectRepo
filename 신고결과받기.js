// 출처 : 프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/92334

var list_A = ["muzi", "frodo", "apeach", "neo"];
var report_A = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"];
var A = 2;

var list_B = ["con", "ryan"];
var report_B = ["ryan con", "ryan con", "ryan con", "ryan con"];
var B = 3;

var result = [];

result = solution(list_A, report_A, A);

//console.log("----------result----------------", result);

function solution(id_list, report, k) {

    var kChk = false;
    kChack(k);

    var idListCnt = [];
    var listCnt = 0;
    var reportAttackList = [];

    for (var i = 0; i < id_list.length; i++) {

        var listId = id_list[i].toString();
        //console.log("======================id_list[i]=======================", id_list[i]);
        var idListAttackList = [];
        var reportIdSet;
        var reportId_A;
        var reportId_B;

         for (var j = 0; j < report.length; j++) {
             reportIdSet = report[j].split(',').toString();
             reportId_A = reportIdSet.substr(0, id_list[i].length)
             reportId_B = reportIdSet.substr(id_list[i].length + 1, reportIdSet.length);
             listChk = reportId_A.indexOf(id_list[i]);

             if (listChk != -1) {
                 listCnt += 1;
                 idListAttackList.push(reportId_B);
                //console.log("-------------listChk 누적 체크---------------", listCnt);
             }
         }
         idListCnt.push(listCnt);
         reportAttackList.push(idListAttackList);
         listCnt = 0;

    }

    var string_A = "";
    var string_B = "";
    var string_C = "";
    var string_D = "";
    var chkCnt = 0;
    for (var i = 0; i < reportAttackList.length; i++) { 
     
        if (chkCnt == 0) {
            string_A = reportAttackList[i].toString();
            chkCnt += 1;
        } else if (chkCnt == 1) { 
            string_B = reportAttackList[i].toString();
            chkCnt += 1;
        }  else if (chkCnt == 2) { 
            string_C = reportAttackList[i].toString();
            chkCnt += 1;
        } else if (chkCnt == 3) { 
            string_D = reportAttackList[i].toString();
            chkCnt += 1;
        }
    }

    var resultArr = [];
    var stringNm = "";
    var cnt = 0;
    for (var i = 0; i<reportAttackList.length; i++) { 
        stringNm = reportAttackList[i].toString();

        if (stringNm == string_A) {
            let aa = stringNm.indexOf(string_B);
            let bb = stringNm.indexOf(string_C);
            let cc = stringNm.indexOf(string_D);

            if (aa != -1) { 
                cnt += 1;
            }
            if (bb != -1) { 
                cnt += 1;
            }
            if (cc != -1) { 
                cnt += 1;
            }
            resultArr.push(cnt);
            cnt = 0;

        } else if (stringNm == string_B) { 
            let dd = stringNm.indexOf(string_C);
            let ee = stringNm.indexOf(string_D);

             if (dd != -1) { 
                cnt += 1;
            }
            if (ee != -1) { 
                cnt += 1;
            }
            resultArr.push(cnt);
            cnt = 0;

        }  else if (stringNm == string_C) { 
            let ff = stringNm.indexOf(string_D);

            if (ff != -1) { 
                cnt += 1;
            }
            resultArr.push(cnt);
            cnt = 0;

        } else if (stringNm == string_D) { 
            cnt = 0;
            resultArr.push(cnt);
            cnt = 0;
        }
    }

    return resultArr;
}

// k값 체크
function kChack(k) {
    kChk = false;

    if (k => 1 && k <= 200) {
        kChk = true;
    }

    return kChk;
}