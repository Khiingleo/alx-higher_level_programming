$(function() {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
        var myHello = data.hello;
        $('#hello').text(myHello);
    });
});