setTimeout(function () {
    messages = document.getElementById('messages');
    if (messages) {
        messages.remove();
    }
}, 5000);
setTimeout(function () {
    errors = document.getElementById('errors');
    if (errors) {
        errors.remove();
    }
}, 5200);