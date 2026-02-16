func canJump(nums []int) bool {
    max_reach := 0

    for i, n := range nums {
        if i > max_reach {
            return false
        }
        max_reach = max(max_reach, i + n)
        if max_reach >= len(nums)-1 {
            return true
        }
    }

    return true
}