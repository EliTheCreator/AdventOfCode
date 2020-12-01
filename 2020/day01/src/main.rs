use std::fs;

fn task1() {
    let file = fs::read_to_string("input").expect("Unable to read the file");
    let ep: Vec<u64> = file
        .split_ascii_whitespace()
        .map(|i| i.parse::<u64>().unwrap())
        .collect();

    let l = ep.len();
    for i in 1..l {
        let vi = ep[i];
        for j in i..l {
            let vj = ep[j];
            if vi + vj == 2020 {
                println!("{}", vi * vj);
            }
        }
    }
}

fn task2() {
    let file = fs::read_to_string("input").expect("Unable to read the file");
    let mut ep: Vec<u64> = file
        .split_ascii_whitespace()
        .map(|i| i.parse::<u64>().unwrap())
        .collect();
    ep.sort();

    let l = ep.len();
    for i in 1..l {
        let vi = ep[i];
        for j in i..l {
            let vj = ep[j];
            let vij = vi + vj;
            for k in j..l {
                let vk = ep[k];
                let v = vij + vk;
                if v == 2020 {
                    println!("{}", vi * vj * vk);
                    return;
                } else if v > 2020 {
                    break;
                }
            }
        }
    }
}

fn main() {
    task1();
    task2();
}
