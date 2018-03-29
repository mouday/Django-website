 $('.form_date').datetimepicker({
    language:  'zh-CN',
    weekStart: 1,
    todayBtn:  1,
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    minView: 2,
    forceParse: 0
});


 //前端权限控制
$(function(){

    //权限说明
    //1、admin
    //2、jihua
    //3、shuju
    //4、biaoqian
    //5、wuliao
    //

    var current_user = $("#current_user").text();
    var item_id = $("#edit-id").val();
  // 处理日期框权限  datetimepicker禁用
    var date = $("#edit-date").children("input").val();
    console.log("date:"+date)
    var input = document.createElement("input");
    $(input).addClass("form-control").val(date).attr("readonly", true).attr("name","edit-time");

    if(current_user=="admin"){
        //什么也不做了
    }
    else if(current_user=="jihua"){

        $("#edit-predata").attr("disabled", true);
        $("#edit-data").attr("disabled", true);

        $("#edit-label").attr("disabled", true);
        $("#edit-card").attr("disabled", true);
        $("#edit-chip").attr("disabled", true);
    }
    else{
        //uid 为空就跳转，权限不足，不显示
        if(item_id ==""){
                location.href="/";
        }
        
        if(current_user=="shuju"){

            $("#edit-id").attr("readonly", true);
            $("#edit-area").attr("readonly", true);
            $("#edit-title").attr("readonly", true);

            $("#edit-date").empty().append(input);

            $("#edit-grade").attr("disabled", true);
            $("#edit-label").attr("disabled", true);
            $("#edit-card").attr("disabled", true);
            $("#edit-chip").attr("disabled", true);
        }
        else if(current_user=="biaoqian"){

            $("#edit-id").attr("readonly", true);
            $("#edit-area").attr("readonly", true);
            $("#edit-title").attr("readonly", true);

            $("#edit-date").empty().append(input);

            $("#edit-predata").attr("disabled", true);
            $("#edit-data").attr("disabled", true);
            $("#edit-grade").attr("disabled", true);
            $("#edit-card").attr("disabled", true);
            $("#edit-chip").attr("disabled", true);
        }
        else if(current_user=="wuliao"){

            $("#edit-id").attr("readonly", true);
            $("#edit-area").attr("readonly", true);
            $("#edit-title").attr("readonly", true);
            
            $("#edit-date").empty().append(input);

            $("#edit-predata").attr("disabled", true);
            $("#edit-data").attr("disabled", true);
            $("#edit-grade").attr("disabled", true);
            $("#edit-label").attr("disabled", true);
        }
        else{

            $("#edit-id").attr("readonly", true);
            $("#edit-area").attr("readonly", true);
            $("#edit-title").attr("readonly", true);
            
            $("#edit-date").empty().append(input);

            $("#edit-predata").attr("disabled", true);
            $("#edit-data").attr("disabled", true);
            $("#edit-grade").attr("disabled", true);
            $("#edit-label").attr("disabled", true);
            $("#edit-card").attr("disabled", true);
            $("#edit-chip").attr("disabled", true);
        }
    }
})