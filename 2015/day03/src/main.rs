use std::collections::HashSet;
use std::fs;


fn task1(input: &String) -> usize {
    let mut x = 0;
    let mut y = 0;

    let mut set = HashSet::new();
    set.insert((x, y));

    for c in input.chars() {
        match c {
            '^' => y += 1,
            'v' => y -= 1,
            '<' => x -= 1,
            '>' => x += 1,
            _ => (),
        }

        set.insert((x, y));
    }
    
    set.len()
}


fn task2(input: &String) -> usize {
    let mut santa_x = 0;
    let mut santa_y = 0;
    let mut robot_x = 0;
    let mut robot_y = 0;

    let mut set = HashSet::new();
    set.insert((santa_x, santa_y));

    let (santa_instructions, robot_instructions): (Vec<(usize, char)>, Vec<(usize, char)>) = input
        .char_indices()
        .partition(|(index, _)| index%2 == 0);

    let instruction_groups = [(santa_instructions, &mut santa_x, &mut santa_y), (robot_instructions, &mut robot_x, &mut robot_y)];
    for (instructons, x, y) in instruction_groups {
        for (_, c) in instructons {
            match c {
                '^' => *y += 1,
                'v' => *y -= 1,
                '<' => *x -= 1,
                '>' => *x += 1,
                _ => (),
            }
    
            set.insert((*x, *y));
        }
    }
    
    set.len()
}


fn main() {
    let input = fs::read_to_string("input").expect("Unable to read file");

    let result_task1 = task1(&input);
    let result_task2 = task2(&input);
    println!("{result_task1}");
    println!("{result_task2}");
}
