  $(document).ready(function(){
        
            //鼠标悬停事件
            $(".edit, .delete").mouseover(function(){
                $(this).css("cursor", "pointer");
            })

            // 选项改变做相关的状态变化
            function statusChange(self){
                var v = $(self).val();
                var tag = $(self).parent().children(".status-box").first();

                console.log("v: |"+ v + "|");
                console.log("tag: "+ tag);    

                $(tag).removeClass("red green yellow");

                //显示状态颜色
                if(v=="1"){      //  未处理
                    $(tag).addClass("red");
                    console.log("11111111");
                }

                else if(v=="2"){  //  已处理
                    $(tag).addClass("green");
                    console.log("222222222");
                }

                else if(v=="3"){  //  异常
                    $(tag).addClass("yellow");
                    console.log("333333333");
                }
            }

            //单击编辑按钮触发事件
            $(".edit").click(function(){
                var tr = $(this).parent().parent();

                var edit_id = $(tr).attr("item-id");
                var edit_title = $(tr).children("[name='item-title']").first().text();
                var edit_area = $(tr).children("[name='item-area']").first().text();
                var edit_time = $(tr).children("[name='item-time']").first().text();
                var edit_data = $(tr).children("[name='item-data']").first().attr("status");
                var edit_handle = $(tr).children("[name='item-handle']").first().attr("status");
                var edit_content = $(tr).children("[name='item-content']").first().text();
                
                console.log("edit_data: "+ edit_data);
                console.log("edit_handle: "+ edit_handle);

                $("#edit-title").val(edit_title);
                $("#edit-id").val(edit_id);
                $("#edit-area").val(edit_area);
                $("#edit-time").text(edit_time);
                $("#edit-content").val(edit_content);
                $("#edit-data").find("option[value='" + edit_data + "']").attr("selected","selected");
                $("#edit-handle").find("option[value='" + edit_handle + "']").attr("selected","selected");
                
                statusChange("#edit-data");
                statusChange("#edit-handle");
            });

            //设置下拉框的初始转态，改变小方框的背景颜色
            $("#add-item").click(function(){
                $("#add-mode").find(".status-select").each(function(){
                    $(this).find("option[value='1']").attr("selected","selected");
                    statusChange(this);
                })
            });

            $(".status-select").change(function(){
                statusChange(this);
            })

            // 单击删除按钮触发事件
            $(".delete").click(function(){
                var tr = $(this).parent().parent();
                var delete_id = $(tr).attr("item-id");

                var delete_area  = $(tr).children().first().text();
                console.log("delete_area: "+delete_area)

                var delete_title = $(tr).children().first().next().text();
                $("#delete-id").val(delete_id);
                $("#delete-area").text(delete_area);
                $("#delete-title").text(delete_title);

            })

            // 状态显示，html中不要有换行
            $(".status").each(function(){
                var v = $(this).text()
                console.log("v: |" + v + "|")
                if(v=="已处理"){
                    $(this).children("span").addClass("green");
                }
                else if(v=="未处理"){
                    $(this).children("span").addClass("red");
                }
                else if(v=="异常"){
                    $(this).children("span").addClass("yellow");
                }
            }) 


        })

//自动添加每页
  $(function(){
    lst = ["10", "20", "30", "40", "50"];
    for (var i = 0; i < lst.length; i++) {
        var opt = document.createElement("option");
        $(opt).attr("value", lst[i]).text(lst[i]);
        $("#per_page").append(opt);
    }

    var selected_opt = $.cookie("per_page");
    console.log("selected_opt: "+selected_opt)
    if(selected_opt == null) {
        selected_opt = 10;  //给定默认值
    }
    $("#per_page").val(selected_opt); // 设置select选中值

     
    $("#per_page").change(function(){
        var opt = $(this).val(); //获取select选中值
        console.log("opt:" + opt);
        $.cookie("per_page", opt); //写入cookie
        location.reload();
    })
  })