var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';


function getData(form) {
    // Get the data from the form
    var formData = new FormData(form);
    number = formData.get('number');
    // console.log("number: " + number);alignToTop: true, 
    // scroll to the element with id 'creation_' + the creation number entered in the form
    document.getElementById("creation_" + number).scrollIntoView({ block: 'start', behavior: 'smooth' }); // block: center maybe better?

    // console.log(Object.fromEntries(formData)); //uncomment to log the form data
    return false;
}

// Overwrite the default form submit function
document.getElementById("search").addEventListener("submit", function (event) {
    event.preventDefault();
    getData(event.target);
});


// star submission

// console.log(document.getElementsByTagName("label")[1]); {%  document.getElementsByTagName("label")[0].addEventListener("click", prevent);

// document.querySelectorAll('label').forEach(item => {
//     item.addEventListener('click', event => {
//         // console.log("clicked!");
//         // event.preventDefault();

//         var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
//         var label = event.target;
//         var forAttribute = label.getAttribute('for');
//         var input = document.getElementById(forAttribute);
//         var value = input.value;
//         console.log("label: ", label);
//         console.log("input: ", input);
//         console.log("value: ", value);
//         console.log("csrfToken: ", csrfToken);

        

//     })
// })
