use core::hash::Hash;
use regex::Regex;
use std::char;
use std::collections::HashMap;
use std::fs;
use std::io;
use std::sync::mpsc;
use std::thread;

// fn thread_test(v: &mut Vec<u8>) {
//     v[0] = 1;
// }

// fn main() {
//     let mut v: Vec<u8> = vec![4, 5, 6];

//     let t = thread::spawn(move || {
//         thread_test(&mut v);
//         v
//     });
//     let v = t.join().unwrap();

//     println!("{}", v[0]);

//     let mut hmap = HashMap::<u32, String>::new();

//     let x = String::from("hello");
//     hmap.insert(2, x);
//     println!("{}", x);
// }

// struct DefaultHashMap<K, V>
// where
//     K: Eq + Hash,
// {
//     map: HashMap<K, V>,
//     default_val: V,
// }

// impl<K, V> DefaultHashMap<K, V>
// where
//     K: Eq + Hash,
// {
//     fn insert(&mut self, key: K, value: V) -> Option<V> {
//         self.map.insert(key, value)
//     }

//     fn get(&mut self, key: K) -> Option<&V> {
//         match self.map.get(&key) {
//             Some(v) => Some(v),
//             None => Some(&self.default_val),
//         }
//     }
// }

// static mut printer_shutdown_flag: AtomicBool = AtomicBool::new(false);
// static mut computer_shutdown_flag: AtomicBool = AtomicBool::new(false);

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
            None => {
                // self.map.insert(key, self.default_val);
                self.default_val
            }
        }
    }
}

fn intcode(
    mem: &mut DefaultHashMap<i32, i32>,
    input: &mpsc::Receiver<i32>,
    output: &mpsc::Sender<i32>,
    shutdown_flag: &bool,
) {
    let mut i: i32 = 0;

    while !*shutdown_flag {
        let instr = mem.get(i);
        let op = instr % 100;
        let par_1_mode = if instr / 100 % 10 == 1 { true } else { false };
        let par_2_mode = if instr / 1000 % 10 == 1 { true } else { false };
        let par_3_mode = if instr / 10000 % 10 == 1 { true } else { false };

        println!(
            "Pc: {}\tOp: {}\nP1 I: {}\tP2 I: {}\tP3 I: {}",
            i, op, par_1_mode, par_2_mode, par_3_mode
        );

        match op {
            1 | 2 => {
                let source_1 = if par_1_mode {
                    mem.get(i + 1)
                } else {
                    mem.get(mem.get(i + 1))
                };
                let source_2 = if par_2_mode {
                    mem.get(i + 2)
                } else {
                    mem.get(mem.get(i + 2))
                };
                let dest = if par_3_mode { i + 3 } else { mem.get(i + 3) };

                let result: i32;
                if op == 1 {
                    result = source_1 + source_2;
                } else {
                    result = source_1 * source_2;
                }

                println!("Set {} to {}", dest, result);
                mem.insert(dest, result);
                i += 4;
            }
            3 => {
                println!("Requesting input");
                let value = input.recv().unwrap();
                let dest = if par_1_mode { i + 1 } else { mem.get(i + 1) };
                println!("Read {}", value);
                println!("Set {} to {}", dest, value);
                mem.insert(dest, value);
                i += 2;
            }
            4 => {
                let source = if par_1_mode { i + 1 } else { mem.get(i + 1) };
                let value = mem.get(source);
                println!("Sending {} to output", value);
                output.send(value).unwrap();
                i += 2;
            }
            5 | 6 => {
                let par_1 = if par_1_mode {
                    mem.get(i + 1)
                } else {
                    mem.get(mem.get(i + 1))
                };
                let par_2 = if par_2_mode {
                    mem.get(i + 2)
                } else {
                    mem.get(mem.get(i + 2))
                };

                let result = par_1 != 0;

                if (op == 5 && result) || (op == 6 && !result) {
                    i = par_2;
                } else {
                    i += 3;
                }
            }
            7 | 8 => {
                let source_1 = if par_1_mode {
                    mem.get(i + 1)
                } else {
                    mem.get(mem.get(i + 1))
                };
                let source_2 = if par_2_mode {
                    mem.get(i + 2)
                } else {
                    mem.get(mem.get(i + 2))
                };
                let dest = if par_3_mode { i + 3 } else { mem.get(i + 3) };

                let result: i32;
                if (op == 7 && source_1 < source_2) || (op == 8 && source_1 == source_2) {
                    result = 1;
                } else {
                    result = 0;
                }
                mem.insert(dest, result);

                println!("Set {} to {}", dest, result);
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

// fn intcode(
//     mem: &mut DefaultHashMap<i32, i32>,
//     input: &mpsc::Receiver<i32>,
//     output: &mpsc::Sender<i32>,
// ) {
//     let mut i: i32 = 0;

//     loop {
//         let instr = mem.get(i);
//         let op = instr % 100;
//         let par_1_mode = if instr / 100 % 10 == 1 { true } else { false };
//         let par_2_mode = if instr / 1000 % 10 == 1 { true } else { false };
//         let par_3_mode = if instr / 10000 % 10 == 1 { true } else { false };

//         match op {
//             1 | 2 => {
//                 let source_1 = if par_1_mode {
//                     mem.get(i + 1)
//                 } else {
//                     mem.get(mem.get(i + 1))
//                 };
//                 let source_2 = if par_2_mode {
//                     mem.get(i + 2)
//                 } else {
//                     mem.get(mem.get(i + 2))
//                 };
//                 let dest = if par_3_mode { i + 3 } else { mem.get(i + 3) };

//                 let result: i32;
//                 if op == 1 {
//                     result = source_1 + source_2;
//                 } else {
//                     result = source_1 * source_2;
//                 }

//                 mem.insert(dest, result);
//                 i += 4;
//             }
//             3 => {
//                 let value = input.recv().unwrap();
//                 let dest = if par_1_mode { i + 1 } else { mem.get(i + 1) };
//                 mem.insert(dest, value);
//                 i += 2;
//             }
//             4 => {
//                 let source = if par_1_mode { i + 1 } else { mem.get(i + 1) };
//                 let value = mem.get(source);
//                 output.send(value).unwrap();
//                 i += 2;
//             }
//             5 | 6 => {
//                 let par_1 = if par_1_mode {
//                     mem.get(i + 1)
//                 } else {
//                     mem.get(mem.get(i + 1))
//                 };
//                 let par_2 = if par_2_mode {
//                     mem.get(i + 2)
//                 } else {
//                     mem.get(mem.get(i + 2))
//                 };

//                 let result = par_1 != 0;

//                 if (op == 5 && result) || (op == 6 && !result) {
//                     i = par_2;
//                 } else {
//                     i += 3;
//                 }
//             }
//             7 | 8 => {
//                 let source_1 = if par_1_mode {
//                     mem.get(i + 1)
//                 } else {
//                     mem.get(mem.get(i + 1))
//                 };
//                 let source_2 = if par_2_mode {
//                     mem.get(i + 2)
//                 } else {
//                     mem.get(mem.get(i + 2))
//                 };
//                 let dest = if par_3_mode { i + 3 } else { mem.get(i + 3) };

//                 let result: i32;
//                 if (op == 7 && source_1 < source_2) || (op == 8 && source_1 == source_2) {
//                     result = 1;
//                 } else {
//                     result = 0;
//                 }
//                 mem.insert(dest, result);

//                 i += 4;
//             }
//             99 => break,
//             _ => {
//                 println!("Error: Unknown instruction {}", op);
//                 break;
//             }
//         }
//     }
// }

fn printer(output_receiver: &mpsc::Receiver<i32>, shutdown_flag: &bool) {
    while !*shutdown_flag {
        for item in output_receiver.iter() {
            // match item {
            //     Some(v) => {
            //         char::from_u32(v as u32);
            //     }
            //     None => {
            //         break;
            //     }
            // }
            let c = char::from_u32(item as u32).unwrap();
            print!("{}", c);
            // match item {
            //     Some(v) => {
            //         let c = char::from_u32(v as u32).unwrap();
            //         print!("{}", c);
            //     }
            //     None => {
            //         break;
            //     }
            // }
        }
    }
}

fn main() {
    // let mut printer_shutdown_flag: bool = false;
    let mut computer_shutdown_flag: bool = false;
    let file = fs::read_to_string("input").expect("Unable to read the file");
    let re = Regex::new(r"-?[0-9]+").unwrap();

    let mut memory = HashMap::<i32, i32>::new();

    for (key, value) in re.find_iter(&file).enumerate() {
        // println!("Inserting (Key: {}, Value: {})", key, value.as_str());
        memory.insert(key as i32, value.as_str().parse::<i32>().unwrap());
    }

    // let x = re.find_iter(&file)
    //     .enumerate()
    //     .map(|(key, value)| memory.insert(key as i32, value.as_str().parse::<i32>().unwrap()));

    let mut memory = DefaultHashMap {
        map: memory,
        default_val: 0,
    };

    let (input_sender, input_receiver) = mpsc::channel::<i32>();
    let (output_sender, output_receiver) = mpsc::channel::<i32>();

    let computer = thread::spawn(move || {
        intcode(
            &mut memory,
            &input_receiver,
            &output_sender,
            &computer_shutdown_flag,
        );
        memory
    });

    // let printer = thread::spawn(move || {
    //     printer(&output_receiver, &printer_shutdown_flag);
    // });

    loop {
        let mut input = String::new();
        match io::stdin().read_line(&mut input) {
            Ok(_) => {
                if input.trim() == "exit" {
                    break;
                } else {
                    for c in input.trim().chars() {
                        match c.to_digit(10) {
                            Some(v) => match input_sender.send(v as i32) {
                                Ok(_) => {
                                    println!("{}: Sent {}", thread::current().name().unwrap(), v)
                                }
                                Err(e) => println!("{}: {}", thread::current().name().unwrap(), e),
                            },
                            None => println!(
                                "{}: Failed to convert to digit",
                                thread::current().name().unwrap()
                            ),
                        }
                    }
                }
            }
            Err(e) => println!("{}", e),
        }
    }

    computer_shutdown_flag = true;
    // printer_shutdown_flag = true;

    match computer.join() {
        Ok(_) => println!(
            "{}: Successfully joined computer with main thread",
            thread::current().name().unwrap(),
        ),
        Err(e) => println!(
            "{}: Failed to join computer to main thread.\n{:?}",
            thread::current().name().unwrap(),
            e
        ),
    }

    // output_receiver.
    for item in output_receiver.try_iter() {
        println!("{}", item);
        // match char::from_u32(item as u32) {
        //     Some(v) => print!("{}", v),
        //     None => (),
        // }
        // match item {
        //     Some(v) => {
        //         char::from_u32(v as u32);
        //     }
        //     None => {
        //         break;
        //     }
        // }
        // let c = char::from_u32(item as u32).unwrap();
        // print!("{}", c);
    }

    // match printer.join() {
    //     Ok(_) => println!(
    //         "{}: Successfully joined printer with main thread",
    //         thread::current().name().unwrap(),
    //     ),
    //     Err(e) => println!(
    //         "{}: Failed to join printer to main thread.\n{:?}",
    //         thread::current().name().unwrap(),
    //         e
    //     ),
    // }
}
