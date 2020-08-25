/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {

    // init a new linked list
    let head = new ListNode()
    let node = head

    // carry will always be 0 or 1
    let carryOver = 0

    // while l1 or l2 exist:
    while (l1 || l2) {
        // get l1 and l2 values

        // if l1 is present, grab that val, otherwise 0
        let l1Value = l1 ? l1.val : 0
        // if l2 is present, grab that val, otherwise 0
        let l2Value = l2 ? l2.val : 0

        // add up the two values and the carry over if there is one
        let sum = l1Value + l2Value + carryOver

        // reset to 0 after a sum of two nodes 
        carryOver = 0
        let newVal = sum

        // if the sum is greater than 9, then carry over = 1

        if (sum > 9) {
            // strip off the 10ths place
            newVal = sum % 10
            // update carryOver to 1 (carryover will max be 1)
            carryOver = 1
        }

        // next node, pass in the new value
        node.next = newListNode(newVal)
        // update linked list 
        node = node.next

        // traverse l1 
        if (l1) {
            l1 = l1.next
        }
        // traverse l2
        if (l2) {
            l2 = l2.next
        }
    }

    // if there is at least 1 value in carryOver
    if (carryOver) {
        // add one more node at the end, which is val of the carry Over
        node.next = new ListNode(carryOver)

    }

    // return head, point to where the num actually starts

    return head.next
};