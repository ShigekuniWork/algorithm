use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut cache = HashMap::new();

        for (index, &num) in nums.iter().enumerate() {
            let diff = target - num;
            if let Some(&pair_index) = cache.get(&diff) {
                return vec![pair_index as i32, index as i32];
            }
            cache.insert(num, index);
        }

        vec![]
    }
}