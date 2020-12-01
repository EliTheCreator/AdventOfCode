use std::fs;
use std::thread;

fn task1() {
    let file = fs::read_to_string("input").expect("Unable to read the file");
    let mut memory: Vec<usize> = file
        .split_terminator(",")
        .filter_map(|x| x.parse::<usize>().ok())
        .collect();

    memory[1] = 12;
    memory[2] = 2;
    let computer = thread::spawn(move || {
        let mut i = 0;
        while i < memory.len() {
            let op = memory[i];
            match op {
                1 => {
                    let dest = memory[i + 3];
                    let source1 = memory[i + 1];
                    let source2 = memory[i + 2];
                    memory[dest] = memory[source1] + memory[source2]
                }
                2 => {
                    let dest = memory[i + 3];
                    let source1 = memory[i + 1];
                    let source2 = memory[i + 2];
                    memory[dest] = memory[source1] * memory[source2]
                }
                99 => break,
                _ => {
                    println!("Error: Unknown instruction {}", op);
                    break;
                }
            }
            i += 4;
        }
        println!("Task 1: {}", memory[0]);
    });
    computer.join().unwrap();
}

fn task2() {
    let file = fs::read_to_string("input").expect("Unable to read the file");
    let memory: Vec<usize> = file
        .split_terminator(",")
        .filter_map(|x| x.parse::<usize>().ok())
        .collect();

    let computer = thread::spawn(move || {
        for noun in 0..100 {
            for verb in 0..100 {
                let mut mem = memory.clone();
                mem[1] = noun;
                mem[2] = verb;
                let mut i = 0;
                while i < mem.len() {
                    let op = mem[i];
                    match op {
                        1 => {
                            let dest = mem[i + 3];
                            let source1 = mem[i + 1];
                            let source2 = mem[i + 2];
                            mem[dest] = mem[source1] + mem[source2]
                        }
                        2 => {
                            let dest = mem[i + 3];
                            let source1 = mem[i + 1];
                            let source2 = mem[i + 2];
                            mem[dest] = mem[source1] * mem[source2]
                        }
                        99 => break,
                        _ => {
                            println!("Error: Unknown instruction {}", op);
                            break;
                        }
                    }
                    i += 4;
                }
                if mem[0] == 19690720 {
                    println!("Task 2: {}", 100 * noun + verb);
                    return;
                }
            }
        }
    });
    computer.join().unwrap();
}

fn main() {
    task1();
    task2();
}
