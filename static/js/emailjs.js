$(document).ready(function () {
    const contactForm = document.getElementById('contact-form');
    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const data = {
            service_id: "gmail",
            template_id: "racquet_shop",
            user_id: emailjs,
            template_params: {
                "from_name": contactForm.name.value,
                "from_email": contactForm.email.value,
                "shop_request": contactForm.message.value
            }
        };

        $.ajax('https://api.emailjs.com/api/v1.0/email/send', {
    type: 'POST',
    data: JSON.stringify(data),
    contentType: 'application/json'
}).done(function() {
    contact_success();
    console.log('Your email has been sent');
}).fail(function(error) {
    contact_error();
    console.log('Oops... ' + JSON.stringify(error));
});
});
    function contact_success(){
        var success = {
        message: 'Thanks! Your email has been sent',
        title: 'Email sent',
        size: 'md',
    };

eModal.alert(success);
    }

    function contact_error(){
        var error = {
        message: 'Sorry, there was a problem. Please try again',
        title: 'Email not sent',
        size: 'md',
    };

eModal.alert(error);
    }

});
