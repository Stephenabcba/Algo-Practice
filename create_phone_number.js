//  Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
//  createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"

function createPhoneNumber(numbers){
    phoneNumberString = "("
    for (let i = 0; i < 3; i++) phoneNumberString += numbers[i]
    phoneNumberString += ") "
    for (let i = 3; i < 6; i++) phoneNumberString += numbers[i]
    phoneNumberString += "-"
    for (let i = 6; i < 10; i++) phoneNumberString += numbers[i]
    return phoneNumberString
}

createPhoneNumber([1,2,3,4,5,6,7,8,9,0])
/*
Alternative solutions:
Solution 1. create the format (xxx) xxx-xxxx
    - make use of replace and replace x one at a time with a for loop
Solution 2. numbers.join('').replace(/(...)(...)(.*)/, '($1) $2-$3');

*/
