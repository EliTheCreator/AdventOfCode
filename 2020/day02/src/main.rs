use std::fs;

fn main() {
    let file = fs::read_to_string("input").expect("Unable to read file");
    // let file = fs::read("input").expect("Unable to read file");

    let lines: Vec<Vec<&str>> = file.split("\n").map(|s| s.split(" ").collect()).collect();
    // let v: Vec<&str> = file.split("\n").collect();

    let mut count = 0;
    let mut counter = || count += 1;
    for line in lines {
        let letter = line[1].get(0..1).unwrap().as_bytes()[0];
        let num: u8 = line[2].as_bytes().iter().filter(|u| **u == letter).count() as u8;
        let minAndMax: Vec<u8> = line[0]
            .split("-")
            .take(2)
            .map(|i| i.parse::<u8>().unwrap())
            .collect();

        if minAndMax[0] <= num as u8 && num as u8 <= minAndMax[1] {
            counter()
        }
    }

    println!("{}", count);
}
