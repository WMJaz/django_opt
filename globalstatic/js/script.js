function AjaxRequests(data){
    var formData;
    if (data instanceof FormData) 
        formData = data;
    else {
        formData = new FormData();
        for (var key in data) {
            if (data.hasOwnProperty(key))
                formData.append(key, data[key]);
        }
    }
    return formData;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    var openmodalscount = 0;
    $(document).on('shown.bs.modal', '.modal', function () {
        openmodalscount++;
    });
    $(document).on('hidden.bs.modal', '.modal', function () {
        openmodalscount--;
        if (openmodalscount > 0) {
            $('body').addClass('modal-open');
        }
    });
});