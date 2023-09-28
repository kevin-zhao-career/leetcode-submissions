/** 2667. Create Hello World Function
 *  Author: Kevin Zhao
 *  Time Complexity: O(1)
 *  Space Complexity: O(1)
 */

/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World";
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
