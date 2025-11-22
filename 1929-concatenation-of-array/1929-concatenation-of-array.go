func getConcatenation(nums []int) []int {
    numsLength := len(nums)

    arr := make([]int, numsLength * 2)
	for i := range(nums) {
        cur := nums[i]
		arr[i] = cur
		arr[i + numsLength] = cur
	}

	return  arr
}