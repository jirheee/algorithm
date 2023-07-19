use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let reverse_index_map = nums
            .iter()
            .enumerate()
            .map(|(i, n)| (*n, i))
            .collect::<HashMap<_, _>>();

        for (i1, num) in nums.iter().enumerate() {
            if let Some(i2) = reverse_index_map.get(&(target - num)) {
                if i1 != *i2 {
                    return vec![i1 as i32, *i2 as i32];
                }
            }
        }

        unreachable!("unreachable by assumption")
    }
}
