
$(function () {
    const token = localStorage.getItem("token")
    $.ajax({
        type: 'GET',
        dataType: 'json',
        beforeSend: function (xhr){ 
            xhr.setRequestHeader('Authorization', "Basic " + token); 
        },
        url: '/api/lunar_phase',
        success: function (data) {
            const response = data.response;
            const id = response.id;
            const moon_id = "#" + id;

            $('h1').text(response.name);
            $(moon_id).css({ 'opacity': 1 });
        }
    });
})