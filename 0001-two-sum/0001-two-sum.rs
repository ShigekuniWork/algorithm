use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut index_cache = HashMap::new();

        for (i, v) in nums.iter().enumerate() {
            let diff = target - v;

            if let Some(&pair_index) = index_cache.get(&diff) {
                return vec![pair_index, i as i32];
            }
            index_cache.insert(v, i as i32);
        }
        // Not found pair of two sum
        vec![]
    }
}