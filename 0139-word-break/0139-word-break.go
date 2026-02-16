func wordBreak(s string, wordDict []string) bool {
    dp := make([]bool, len(s) + 1)
    dp[len(s)] = true

    for i := len(s) -1; i >= 0; i-- {
        for _, w := range wordDict {
            end := i + len(w)
            if i + len(w) <= len(s) && s[i:end] == w {
                dp[i] = dp[end]
            }
            if dp[i] {
                break
            }
        }
    }

    return dp[0]
}