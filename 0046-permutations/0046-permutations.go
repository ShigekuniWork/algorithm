func permute(nums []int) [][]int {
    n := len(nums)
    if n == 0 {
        return [][]int{}
    }

    totalPermutations := 1
    for i := 1; i <= n; i++ {
        totalPermutations *= i
    }
    
    res := make([][]int, 0, totalPermutations)
    
    backtrack(&res, nums, 0)
    return res
}

func backtrack(res *[][]int, nums []int, idx int) {
    if idx == len(nums) {
        row := make([]int, len(nums))
        copy(row, nums)

        *res = append(*res, row) 
        return
    }
    
    for i := idx; i < len(nums); i++ {
        nums[idx], nums[i] = nums[i], nums[idx]
        backtrack(res, nums, idx+1)
        nums[idx], nums[i] = nums[i], nums[idx]
    }
}