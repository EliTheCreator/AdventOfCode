use core::hash::Hash;
use regex::Regex;
use std::collections::HashMap;
use std::fs;
use std::io;
use std::sync::mpsc;
use std::thread;

struct DefaultHashMap<K, V>
where
    K: Eq + Hash + Copy,
    V: Copy,
{
    map: HashMap<K, V>,
    default_val: V,
}

impl<K, V> DefaultHashMap<K, V>
where
    K: Eq + Hash + Copy,
    V: Copy,
{
    fn insert(&mut self, key: K, value: V) -> Option<V> {
        self.map.insert(key, value)
    }

    fn get(&self, key: K) -> V {
        match self.map.get(&key) {
            Some(v) => *v,
            None => self.default_val,
        }
    }
}

fn intcode_emulator(
    mem: &mut DefaultHashMap<i32, i32>,
    input: &mpsc::Receiver<i32>,
    output: &mpsc::Sender<i32>,
) {
    let mut i: i32 = 0;

    loop {
        let instr = mem.get(i);
        let op = instr % 100;

        let par_1 = if instr / 100 % 10 == 1 {
            mem.get(i + 1)
        } else {
            mem.get(mem.get(i + 1))
        };
        let par_2 = if instr / 1000 % 10 == 1 {
            mem.get(i + 2)
        } else {
            mem.get(mem.get(i + 2))
        };
        let par_3 = if instr / 10000 % 10 == 1 {
            i + 3
        } else {
            mem.get(i + 3)
        };

        match op {
            1 | 2 => {
                let result: i32;
                if op == 1 {
                    result = par_1 + par_2;
                } else {
                    result = par_1 * par_2;
                }

                mem.insert(par_3, result);
                i += 4;
            }
            3 => {
                let dest = if instr / 100 % 10 == 1 {
                    i + 1
                } else {
                    mem.get(i + 1)
                };
                let value = input.recv().unwrap();
                mem.insert(dest, value);
                i += 2;
            }
            4 => {
                let source = if instr / 100 % 10 == 1 {
                    i + 1
                } else {
                    mem.get(i + 1)
                };
                let value = mem.get(source);
                output.send(value).unwrap();
                i += 2;
            }
            5 | 6 => {
                let result = par_1 != 0;

                if (op == 5 && result) || (op == 6 && !result) {
                    i = par_2;
                } else {
                    i += 3;
                }
            }
            7 | 8 => {
                let result: i32;
                if (op == 7 && par_1 < par_2) || (op == 8 && par_1 == par_2) {
                    result = 1;
                } else {
                    result = 0;
                }
                mem.insert(par_3, result);

                i += 4;
            }
            99 => break,
            _ => {
                println!("Error: Unknown instruction {}", op);
                break;
            }
        }
    }
}

fn task(task_input: i32) {
    let file = fs::read_to_string("input").expect("Unable to read the file");
    let re = Regex::new(r"-?[0-9]+").unwrap();

    let mut memory = HashMap::<i32, i32>::new();

    for (key, value) in re.find_iter(&file).enumerate() {
        memory.insert(key as i32, value.as_str().parse::<i32>().unwrap());
    }

    let (out_main, in_A) = mpsc::channel::<i32>();
    let (out_A, in_B) = mpsc::channel::<i32>();
    let (out_B, in_C) = mpsc::channel::<i32>();
    let (out_C, in_D) = mpsc::channel::<i32>();
    let (out_D, in_E) = mpsc::channel::<i32>();
    let (out_E, in_main) = mpsc::channel::<i32>();

    out_main.send(task_input);
    let mut amps = Vec::new();
    for (i, o) in vec![
        (in_A, out_A),
        (in_B, out_B),
        (in_C, out_C),
        (in_D, out_D),
        (in_E, out_E),
    ]
    .into_iter()
    {
        let mem = memory.clone();
        let amp = thread::spawn(move || {
            intcode_emulator(
                &mut DefaultHashMap {
                    map: mem,
                    default_val: 0,
                },
                &i,
                &o,
            )
        });
        amps.push(amp);
    }

    for amp in amps.into_iter() {
        match amp.join() {
            Ok(_) => (),
            Err(e) => println!(
                "{}: Failed to join computer to main thread.\n{:?}",
                thread::current().name().unwrap(),
                e
            ),
        }
    }

    for item in in_main.try_iter() {
        println!("{}", item);
    }
}

fn get_input(task: u8) -> i32 {
    println! {"Enter value for task {}:", task};

    loop {
        let mut input = String::new();
        match io::stdin().read_line(&mut input) {
            Ok(_) => {
                let parse_result = input.trim().parse();
                match parse_result {
                    Ok(v) => return v,
                    Err(_) => println!("Unable to parse input, please try again."),
                }
            }
            Err(_) => (),
        }
    }
}

fn main() {
    for t in 1..=2 {
        let task_input = get_input(t);
        println!("Output:");
        task(task_input);
    }
}
