use std::fs;


fn task1(input: &String) -> u32 {
    input.lines()
        .map(|line| {
            line.split("x")
                .map(|c| c.parse::<u32>()
                .unwrap())
        })
        .map(|mut line| {
            let l = line.next().unwrap();
            let w = line.next().unwrap();
            let h = line.next().unwrap();

            let sides = [l*w, w*h, h*l];
            let min_size = sides.into_iter()
                                     .reduce(|acc, e| acc.min(e))
                                     .unwrap();
            let box_area: u32 = sides.map(|side| side*2)
                                     .into_iter()
                                     .sum();

            box_area + min_size
        })
        .sum()
}


fn task2(input: &String) -> u64 {
    input.lines()
        .map(|line| {
            line.split("x")
                .map(|c| c.parse::<u64>()
                .unwrap())
        })
        .map(|mut line| {
            let sides = [
                line.next().unwrap(),
                line.next().unwrap(),
                line.next().unwrap(),
            ];

            let max_size = sides.into_iter()
                                     .reduce(|acc, e| acc.max(e))
                                     .unwrap();
            let ribbon = sides.map(|side| side*2)
                                   .into_iter()
                                   .sum::<u64>()
                              - 2*max_size;
            let bow = sides.into_iter()
                           .reduce(|acc, e| acc*e)
                           .unwrap();

            ribbon + bow
        })
        .sum()
}


fn main() {
    let input = fs::read_to_string("input").expect("Unable to read file");

    let result_task1 = task1(&input);
    let result_task2 = task2(&input);
    println!("{result_task1}");
    println!("{result_task2}");
}
