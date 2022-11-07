// create a graph using chart.js given the x and y axis values and the id for the canvas
function createGraph(names, values, canvasId) {
    var config = {
        type: 'bar',
        data: {
            datasets: [{
                data: values,
                backgroundColor: [
                    '#696969', '#808080', '#A9A9A9', '#C0C0C0', '#D3D3D3'
                ],
                label: 'Population'
            }],
            labels: names,
        },
        options: {
            responsive: true
        }
    };

    window.onload = function () {
        var ctx = document.getElementById(canvasId).getContext('2d');
        window.myPie = new Chart(ctx, config);
    };
}
