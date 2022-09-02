function disemvowel(str) {
    var returnStr = ""
    var vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for (var i = 0; i < str.length; i++) {
        if (vowels.indexOf(str[i]) == -1){
            returnStr += str[i]
        }
    }
    return returnStr
}



console.log(disemvowel("THIS IS AWESOME"));
console.log(disemvowel("WhY ArE YoU dOiNG thIs To mE"));

// solutions from codewars:
// use replace functions
//    /   / dictates the pattern
//    [ ] is to match any character in a set
//    g   is all matches, not just the first
//    i   is case insensitive

function disemvowel2(str) {
    return str.replace(/[aeiou]/gi, '')
}

console.log(disemvowel2("THIS IS AWESOME"));
console.log(disemvowel2("WhY ArE YoU dOiNG thIs To mE"));