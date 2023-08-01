/** 
 * @param {number} target
 * @return {number}
 */
Array.prototype.upperBound = function(target) {
    let leftIndex = 0, rightIndex = this.length;
    while (leftIndex < rightIndex) {
        const middleIndex = (leftIndex + rightIndex) >> 1;
        if(this[middleIndex] <= target) {
            leftIndex = middleIndex + 1;
        }
        else {
            rightIndex = middleIndex;
        }
    }
    return (leftIndex > 0 && this[leftIndex - 1] == target) ? leftIndex - 1 : -1;
};
