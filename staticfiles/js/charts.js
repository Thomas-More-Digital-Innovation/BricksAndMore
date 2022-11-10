function testfunc(queryset) {
    console.log(queryset);
}


// create a graph using chart.js given the x and y axis values and the id for the canvas
function createGraph(creationNames, values, label, canvasId) {
    console.log("creating graph");
    console.log(creationNames);
    console.log(values);
    console.log(label);
    console.log(canvasId);
    console.log("end of creating graph");
    var config = {
        type: 'bar',
        data: {
            datasets: [{
                data: values,
                backgroundColor: [
                    '#696969', '#808080', '#A9A9A9', '#C0C0C0', '#D3D3D3'
                ],
                label: label
            }],
            labels: creationNames,
        },
        options: {
            responsive: true
        }
    };

    var ctx = document.getElementById(canvasId).getContext('2d');
    window.myPie = new Chart(ctx, config);

    // window.onload = function () {
    // var ctx = document.getElementById(canvasId).getContext('2d');
    // window.myPie = new Chart(ctx, config);
    // };
}

