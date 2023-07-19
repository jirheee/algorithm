#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}
use std::cell::RefCell;
use std::ops::Deref;
use std::rc::Rc;

struct Solution;
impl Solution {
    pub fn postorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        match root {
            Some(node) => {
                let borrowed = node.borrow();
                vec![
                    Self::postorder_traversal(borrowed.left.clone()),
                    Self::postorder_traversal(borrowed.right.clone()),
                    vec![borrowed.val],
                ]
                .concat()
            }
            None => vec![],
        }
    }
}
