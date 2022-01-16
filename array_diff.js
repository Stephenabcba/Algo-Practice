// Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

// It should remove all values from list a, which are present in list b keeping their order.

function arrayDiff(a,b) {
    var returnArray = []
    for (var i = 0; i < a.length; i++) {
        var inListB = false
        for (var j = 0; j < b.length; j++) {
            if (a[i] == b[j]) {
                inListB = true
                break
            }
        }
        if (!inListB) {
            returnArray.push(a[i]) 
        }
    }
    return returnArray
}

console.log(arrayDiff([], [4,5]));
console.log(arrayDiff([3,4], [3]));
console.log(arrayDiff([1,8,2], []));
console.log(arrayDiff([1,2,3], [1,2]));

// from codeWars:
// can also use array.filter()
// filter() takes in either
//  - a function 
//  - or a statement using '=>'
// to check if a value is in b:
//  - use includes() : returns true or false
//  - use indexOf()  : returns index, -1 if not in array
function arrayDiff2(a,b) {
    return a.filter(v => !b.includes(v))
}

console.log(arrayDiff2([], [4,5]));
console.log(arrayDiff2([3,4], [3]));
console.log(arrayDiff2([1,8,2], []));
console.log(arrayDiff2([1,2,3], [1,2]));