/*!
    * Start Bootstrap - SB Admin v6.0.1 (https://startbootstrap.com/templates/sb-admin)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */


    (function($) {
    "use strict";

    // Add active state to sidbar nav links
    // var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
    //     $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {
    //         if (this.href === path) {
    //             $(this).addClass("active");
    //         }
    //     });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function(e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
    });
})(jQuery);



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



function csrfSafeMethod(method){
    return ['GET','OPTIONS','HEAD','TRACE'].includes(method);
}

$.ajaxSetup({
    beforeSend: function (xhr,settings){
        if(!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken",csrftoken)
        }
        

    }
})



$(document).ready(function() {
    toastr.options = {
        'closeButton': true,
        'debug': false,
        'newestOnTop': false,
        'progressBar': true,
        'positionClass': 'toast-bottom-right',
        'preventDuplicates': false,
        'showDuration': '1000',
        'hideDuration': '1000',
        'timeOut': '5000',
        'extendedTimeOut': '1000',
        'showEasing': 'swing',
        'hideEasing': 'linear',
        'showMethod': 'fadeIn',
        'hideMethod': 'fadeOut',
    }
});



// var start_date = document.getElementById('id_start_date')
// flatpickr(start_date,{})

window.onload = datepickerload();
function datepickerload(){
    const myDateInput = document.querySelectorAll(".dateinput");
myDateInput.forEach(element => {
  flatpickr(element, {

})

}); 

}

