/*
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).
*/
// Additional observation: the ten minute walk should take you back to where you started, as inferred from the example outputs

function isValidWalk(walk) {
    if (walk.length != 10) {
        return false
    }
    var position = 0.0
    var movement = {
        'n': 1,
        's': -1,
        'w':-0.1,
        'e':0.1,
    }
    for (let i = 0; i < 10; i++) {
        position += movement[walk[i]]
    }
    return (position == 0)
}

console.log(isValidWalk(['n','s','n','s','n','s','n','s','n','s']));
console.log(isValidWalk(['w','e','w','e','w','e','w','e','w','e','w','e']));
console.log(isValidWalk(['n','n','n','s','n','s','n','s','n','s']));


// taken from codewars:
// define a function using the filter function to find the count of each choice (n,s,w,e)
// conditions for the 10 minute walk to be valid:
//    - there must be only 10 actions (walk length = 10)
//    - you must end up where you started
//      - the number of N must match the number of S
//      - the number of E must match the number of W
//      - the above 2 conditions ensure that you end up at (0,0) in the cartesian plane assuming you started at (0,0)
function isValidWalk2(walk) {
    function count(val) {
        return walk.filter(function(a){return a==val;}).length;
    }
    return walk.length==10 && count('n')==count('s') && count('w')==count('e');
}