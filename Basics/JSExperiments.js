function f1() {
    fruit = "orange";
    return fruit;
}

function f2() {
    fruit = "pear";
    return fruit;
}

fruit = "Apple"
console.log(fruit);
console.log(f1())
console.log(f2())
console.log(fruit);

// ---------------

console.log("hello" == "Hello")

// ----------------

console.log("---- Move zeros -------")

function moveZeros(arr) {
    let zeroIndix = 0;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] != 0) {
            [arr[i], arr[zeroIndix]] = [arr[zeroIndix], arr[i]];
            zeroIndix++;
        }
    }

    return arr;
}

console.log(moveZeros([0, 1, 0, 3, 12]))
console.log(moveZeros([0, 1]))
console.log(moveZeros([0, 0]))
console.log(moveZeros([0]))
console.log(moveZeros([]))
console.log(moveZeros([1, 0]))