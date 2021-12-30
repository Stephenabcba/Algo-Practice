function alphabetPosition(text) {
    positionString = ""
    text = text.toLowerCase()   // convert to lower case for ascii value consistency
    for (var i = 0; i < text.length; i++) {
        var asciiVal = text.charCodeAt(i)  // use the ascii values to confirm that the character is part of the alphabet and to extract value
        if (asciiVal >= 97 && asciiVal <= 122) {
        positionString += asciiVal - 96
        positionString += " "
        }
    }
    return positionString.slice(0,positionString.length-1);  //
}