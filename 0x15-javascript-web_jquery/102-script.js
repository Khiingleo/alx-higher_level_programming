$(function() {
    $('#btn_translate').click(function() {
        var input = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/hello/' + input, function(data) {
            $('#hello').text(data.hello);
        });
    });
});