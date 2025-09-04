impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();
        for c in s.chars() {
            match c {
                // push expected closing bracket
                '(' => stack.push(')'),
                '{' => stack.push('}'),
                '[' => stack.push(']'),

                // check top of stack matches
                ')' | '}' | ']' => {
                    if stack.pop() != Some(c) {
                        return false;
                    }
                }
                _ => return false,
            }
        }
        stack.is_empty()
    }
}