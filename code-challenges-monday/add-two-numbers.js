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

    let head = new ListNode()
    let node = head

    let carryOver = 0

    while (l1 || l2) {


        let l1Value = l1 ? l1.val : 0
        let l2Value = l2 ? l2.val : 0

        let sum = l1Value + l2Value + carryOver

        // reset to 0 after a sum
        carryOver = 0
        let newVal = sum

        if (sum > 9) {
            // strip off the 10ths place
            newVal = sum % 10
            // update carryOver to 1
            carryOver = 1
        }

        node.next = newListNode(newVal)
        // update linked list 
        node = node.next

        if (l1) {
            l1 = l1.next
        }
        if (l2) {
            l2 = l2.next
        }
    }

    if (carryOver) {

        node.next = new ListNode(carryOver)

    }

    return head.next
};