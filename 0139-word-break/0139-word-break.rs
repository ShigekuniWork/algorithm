impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let n = s.len();

        let mut dp = vec![false; n + 1];
        dp[n] = true;

        for i in (0..s.len()).rev() {
            for w in &word_dict {
                let end = i + w.len();

                if end <= n && &s[i..end] == w {
                    dp[i] = dp[end];
                }

                if dp[i] {
                    break;
                }
            }
        }

        dp[0]
    }
}