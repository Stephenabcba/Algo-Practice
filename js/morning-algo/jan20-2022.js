/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    let counter = 0
    for (var i = 0; i < str.length; i++) {
        if (str[i] === '(') {
            counter++
        } else if (str[i] === ')') {
            counter--
        }
        if (counter < 0) {
            return false
        }
    }
    return counter == 0
}

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const two_str3 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const two_expected3 = true;

const two_str4 = "D(i{a}l[ t]o)n{e";
const two_expected4 = false;

const two_str5 = "A(1)s[O (n]0{t) 0}k";
const two_expected5 = false;

// PSEUDO CODE
// create a function that takes in a string
// create an empty array
// iterate through the string
    // if we encounter an opening symbol '(' '[' or '{', we append the symbol to the array at the end
    // if we encounter a closing symbol ')' ']' or '}', we check if the symbol saved at the array matches with what we have
        // if it matches, we remove the opening symbol from the array
        // if it does not match, we return false
// if the array is not empty at the end, return false
// otherwise, return true



/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    var symbolArray = []
    var openSymbols = {
        '(':')',
        '[':']',
        '{':'}'
    }
    var closeSymbols = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    // var closeSymbols = ")]}"
    for (var i = 0; i < str.length; i++) {
        // console.log(i);
        if (openSymbols.hasOwnProperty(str[i])) {
            // console.log('opening');
            symbolArray.push(str[i])
        } else if (closeSymbols.hasOwnProperty(str[i])) {
        // } else if (closeSymbols.includes(str[i])) { if closeSymbols is saves as a string
            // console.log('closing');
            if (symbolArray.length == 0) {
                return false
            }
            // var temp = symbolArray.pop()
            // console.log(temp);
            // console.log(openSymbols[temp]);
            // if (str[i] != openSymbols[temp]) {
            //     return false
            // }

            if (str[i] != openSymbols[symbolArray.pop()]) {
                return false
            }
        }
    }
    // if (symbolArray.length == 0) {
    //     return true
    // }
    // return false
    return (symbolArray.length == 0)
}
console.log("str3");
console.log(bracesValid(two_str3));
console.log("str4");
console.log(bracesValid(two_str4));
console.log("str5");
console.log(bracesValid(two_str5));

// console.log(bracesValid("]]]}}}}))))))"));


/*****************************************************************************/