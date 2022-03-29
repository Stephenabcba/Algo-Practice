/*          __                        __         
           /\ \                      /\ \        
 _ __    __\ \ \___      __      ____\ \ \___    
/\`'__\/'__`\ \  _ `\  /'__`\   /',__\\ \  _ `\  
\ \ \//\  __/\ \ \ \ \/\ \L\.\_/\__, `\\ \ \ \ \ 
 \ \_\\ \____\\ \_\ \_\ \__/.\_\/\____/ \ \_\ \_\
  \/_/ \/____/ \/_/\/_/\/__/\/_/\/___/   \/_/\/_/

    Given to a Coding Dojo alumni by Riot Games.
    Rehash an incorrectly hashed string by combining letter count occurrences
    and alphabetizing them.
*/
//                   v
const str1 = "b70a164c32a20c10";
const expected1 = "a184b70c42";

// step 1:
// frequencyMap = {}
// step 2:
// extract [keys? values? something?]
// if it's an array -> sort
// ["b70", "a84", "c42"]

// step 3:
// return a string

// hints:
// parseInt(str)
// isNaN(x)
// myObj.hasOwnProperty("key")

function rehash(str) {
    let idx = 0
    const frequencyMap = {}

    // build frequency map
    while (idx < str.length) {
        // the outer while loop should skip indexes to each letter
        if (isNaN(str[idx])) {
            // save the index of the letter
            const letterIdx = idx
            idx++
            // find the number associated with the letter
            while (!isNaN(str[idx])) {
                idx++
            }
            const curFreq = parseInt(str.slice(letterIdx + 1, idx))
            // add the found frequency to the map
            if (frequencyMap.hasOwnProperty(str[letterIdx])) {
                frequencyMap[str[letterIdx]] += curFreq
            } else {
                frequencyMap[str[letterIdx]] = curFreq
            }
        } else { // this shouldn't happen
            return false
        }
    }
    // convert the map to an array for easier sorting
    const freqArr = []
    for (const letter in frequencyMap) {
        freqArr.push(`${letter}${frequencyMap[letter]}`)
    }
    freqArr.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0))
    return freqArr.join('') // convert the sorted array back to a string
}

rehash(str1);
console.log(rehash(str1) === expected1, "<-- should be \"true\"");