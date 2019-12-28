$(document).ready(function () {
    const contactForm = document.getElementById('contact-form');

    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const data = {
            service_id: "gmail",
            template_id: "racquet_shop",
            user_id: emailjs,
            template_params: {
                "name": contactForm.name.value,
                "email": contactForm.email.value,
                "message": contactForm.message.value,
            }
        };

        $.ajax('https://api.emailjs.com/api/v1.0/email/send', {
    type: 'POST',
    data: JSON.stringify(data),
    contentType: 'application/json'
}).done(function() {
    alert('Your mail is sent!');
}).fail(function(error) {
    alert('Oops... ' + JSON.stringify(error));
});
})
})