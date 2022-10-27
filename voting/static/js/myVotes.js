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

document.querySelectorAll('label').forEach(item => {
    item.addEventListener('click', event => {
        // console.log("clicked!");
        // event.preventDefault();
        // get value from clicked label
        var label = event.target;
        var input = document.getElementById(label);
        // inputLabel = input.getAttribute("for");
        var x = document.querySelectorAll('[for=label]')[0];
        console.log("x: " + x);
        console.log("label: ", label);
        console.log("input: ", input);

        var clickedValue = item.getAttribute("for");

        // clickedValue.toString();
        //bit hacky but good for POC
        console.log("vote value:", parseInt(clickedValue.slice(-1)) + 1);
    })
})