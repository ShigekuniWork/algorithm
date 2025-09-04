// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    #[inline]
    fn attach<'a>(
        tail: &'a mut Box<ListNode>,
        list: &mut Option<Box<ListNode>>,
    ) -> &'a mut Box<ListNode> {
        let next = list.as_mut().unwrap().next.take();
        tail.next = list.take();
        let new_tail = tail.next.as_mut().unwrap();
        *list = next;
        new_tail
    }

    pub fn merge_two_lists(
        mut l1: Option<Box<ListNode>>,
        mut l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode::new(0));
        let mut tail = &mut dummy;

        while l1.is_some() && l2.is_some() {
            if l1.as_ref().unwrap().val <= l2.as_ref().unwrap().val {
                tail = Self::attach(tail, &mut l1);
            } else {
                tail = Self::attach(tail, &mut l2);
            }
        }
        tail.next = l1.or(l2);
        dummy.next
    }
}