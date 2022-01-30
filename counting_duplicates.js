// Count the number of Duplicates
// Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

function duplicateCount(text){
    let freqTable = {}
    for (let chr of text) {
        let chrLower = chr.toLowerCase()
        if (freqTable.hasOwnProperty(chrLower)) {
            freqTable[chrLower]++
        } else {
            freqTable[chrLower] = 1
        }
    }
    let dupeCount = 0
    for (key in freqTable) {
        if (freqTable[key] > 1) dupeCount++
    }
    return dupeCount
}

console.log(duplicateCount(""));
console.log(duplicateCount("abcde"));
console.log(duplicateCount("aabbcde"));
console.log(duplicateCount("aabBcde"));
console.log(duplicateCount("Indivisibility"))
console.log(duplicateCount("Indivisibilities"))