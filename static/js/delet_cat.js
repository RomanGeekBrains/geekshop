$(document).ready(function () {
    $(".delete").click(function(){
        let target_href = event.target;
        $(this).parents(".category_record").animate({ opacity: "hide" }, "slow");
        if (target_href) {
            $.ajax({
                url: `/admin/categories/delete/${target_href.id}/`,
                type: "POST",
                // success: function (data) {
                //     console.log('ajax done');                   
                // },
            });
        }
    })
});