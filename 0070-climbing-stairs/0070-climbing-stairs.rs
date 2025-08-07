impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n <= 3 {
            return n;
        }

        let mut prev = 1;
        let mut curr = 2;

        for _ in 3..=n {
            let next = prev + curr;
            prev = curr;
            curr = next;
        }
        curr
    }
}