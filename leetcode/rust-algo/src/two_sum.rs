use std::collections::HashMap;

struct Solution1;

impl Solution1 {
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

struct Solution2;

impl Solution2 {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::with_capacity(nums.len() / 2);

        for (i, num) in nums.iter().enumerate() {
            if let Some(&j) = seen.get(&(target - num)) {
                return vec![j as i32, i as i32];
            }
            seen.insert(num, i);
        }
        unreachable!()
    }
}
