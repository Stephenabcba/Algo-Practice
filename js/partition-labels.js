// leetcode problem #763. Partition Labels
/*
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
*/

/*
solution taken from leetcode
idea:
start with no partition and build as we go through the string from start to end
a letter in the current partition is able to extend the current partition further if the last occurance of this letter exceeds the bounds of the current partition
    - it can "push" the bounds further right (toward the end of the string) so the partition includes all occurances of this letter
implementation:
1. iterate through the string to find the last occurance of each letter
    - store the last occurance index of each letter in a dictionary/object
2. iterate through the string again to build the partitions
    - keep track of the start of the current partition
    2.1 the end of a partition is the higher value between the current end index and the last occurance index of current letter
        - the end partition index >= current index before the next step
    2.2 if the current index is at the end of the partition (end index == current index), we can start a new partition
        - if any letter in the current partition ends further down in the string, (2.1) should have pushed the end partition to that index already
        - the length of the current partition is (end index - start index + 1) to be inclusive of both ends
*/

/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function (s) {
    const letterDict = {}
    for (let i = 0; i < s.length; i++) {
        const letter = s[i]
        letterDict[letter] = i
    }

    const ansArr = []
    let curPartitionStart = 0
    let curPartitionEnd = 0
    for (let i = 0; i < s.length; i++) {
        curPartitionEnd = letterDict[s[i]] > curPartitionEnd ? letterDict[s[i]] : curPartitionEnd
        if (i == curPartitionEnd) {
            ansArr.push(i - curPartitionStart + 1)
            curPartitionStart = i + 1
        }
    }
    return ansArr
};

const s = "ababcbacadefegdehijhklij"
const output = [9, 7, 8]

const s2 = "eccbbbbdec"
const output2 = [10]

console.log(partitionLabels(s2))