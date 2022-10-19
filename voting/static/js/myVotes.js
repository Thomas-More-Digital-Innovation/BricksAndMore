function getData(form) {
    // Get the data from the form
    var formData = new FormData(form);
    number = formData.get('number');
    // console.log("number: " + number);
    // scroll to the element with id 'creation_' + the creation number entered in the form
    document.getElementById("creation_" + number).scrollIntoView();

    // console.log(Object.fromEntries(formData)); //uncomment to log the form data
    return false;
}

// Overwrite the default form submit function
document.getElementById("search").addEventListener("submit", function (event) {
    event.preventDefault();
    getData(event.target);
});