$(document).ready(function () {
    const contactForm = document.getElementById('contact-form');
    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();
        console.log('its working');
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
    eModal.alert('Your email has been sent');
}).fail(function(error) {
    eModal.alert('Oops... ' + JSON.stringify(error));
});
})
})
