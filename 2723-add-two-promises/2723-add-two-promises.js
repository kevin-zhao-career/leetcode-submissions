/** 2723. Add Two Promises
 *  Author: Kevin Zhao
 *  Time Complexity: O(1)
 *  Space Complexity: O(1)
 */

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    return Promise.all([promise1, promise2]).then((values) => {
      const sum = values.reduce((accumulator, value) => accumulator + value, 0);
      return sum;
    });  
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
