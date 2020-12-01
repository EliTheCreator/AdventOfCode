use regex::Regex;
use std::fs;

fn task1() {
    let file = fs::read_to_string("input").expect("Unable to read the file");
    let lines: Vec<&str> = file.split_terminator("\n").collect::<Vec<&str>>();

    let re = Regex::new(r"[A-Z][0-9]+").unwrap();
    for line in lines {
        for pos in re.find_iter(line) {
            println!("{}", pos.as_str());
        }
    }
}

fn main() {
    task1();
}
