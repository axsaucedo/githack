var account_view = {
    init : function() {
        $(".badge").hover(function() {
            $(this).find(".badgeDesc").show()
        }, function() {
            $(this).find(".badgeDesc").hide()
        })
    }
}


$(function() {
    account_view.init();
    alert("sup");
});