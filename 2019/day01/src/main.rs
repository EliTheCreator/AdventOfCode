use std::fs;

fn task1() {
    let file = fs::read_to_string("input").expect("Unable to read the file");
    let ascii_numbers = file.split_ascii_whitespace();

    let mut sum: i64 = 0;
    for ascii_number in ascii_numbers {
        sum += ascii_number.parse::<i64>().unwrap() / 3 - 2;
    }
    println!("Task 1: {}", sum);
}

fn task2() {
    let file = fs::read_to_string("input").expect("Unable to read the file");
    let ascii_numbers = file.split_ascii_whitespace();

    let mut sum: i64 = 0;
    for ascii_number in ascii_numbers {
        let mut x = ascii_number.parse::<i64>().unwrap() / 3 - 2;
        while x > 0 {
            sum += x;
            x = x / 3 - 2;
        }
    }
    println!("Task 2: {}", sum);
}

fn main() {
    task1();
    task2();
}
