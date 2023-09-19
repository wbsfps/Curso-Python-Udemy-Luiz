const square_root = () => {
    let number = document.getElementById("number").value;
    let result = document.getElementById("result");
    let square_root = parseFloat(Math.sqrt(number).toFixed(2));

    result.textContent = 'The square root of ' + number + ' is ' + square_root;
};