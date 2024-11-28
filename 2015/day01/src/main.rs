use std::fs;


fn task1(input: &String) -> i32 {
    input.chars()
        .map(|c| {
            match c {
                '(' => 1,
                ')' => -1,
                _ => 0,
            }
        })
        .sum()
}


fn task2(input: &String) -> Option<usize> {
    let mut sum = 0;
    for (index, c) in input.chars().enumerate() {
        match c {
            '(' => sum += 1,
            ')' => sum -= 1,
            _ => (),
        }

        if sum < 0 {
            return Some(index+1);
        }
    }

    return None;
}


fn main() {
    let input = fs::read_to_string("input").expect("Unable to read file");

    let result_task1 = task1(&input);
    let result_task2 = task2(&input).unwrap();
    println!("{result_task1}");
    println!("{result_task2}");
}
