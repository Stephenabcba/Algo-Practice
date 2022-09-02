// Digital root is the recursive sum of all the digits in a number.

function digital_root(n) {
    while (n >= 10) {
        nStr = n.toString()
        n = 0
        for (var i = 0; i < nStr.length; i++) {
            n += parseInt(nStr[i])
        }
    }
    return n
}

console.log(digital_root(493193));
console.log(digital_root(49));
console.log(digital_root(493));
console.log(digital_root(942));
console.log(digital_root(132189));


// codewar solution:
// (n - 1) % 9 + 1
// recursive functions
//   toString()
//   split('')
//   join('+')