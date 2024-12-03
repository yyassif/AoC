import re

def read_memory(filename):
    """
    Reads corrupted memory from a text file.
    
    Args:
        filename (str): Path to the text file containing corrupted memory
        
    Returns:
        str: The corrupted memory string
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
    """
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")

def parse_multiplications(memory, handle_conditions=False):
    """
    Parse corrupted memory using regex to find valid multiplication instructions
    and control statements.
    
    Args:
        memory (str): The corrupted memory string
        handle_conditions (bool): Whether to handle do() and don't() conditions
    
    Returns:
        int: Sum of all valid multiplication results
    """
    # Pattern for valid multiplication: mul followed by two 1-3 digit numbers
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    if not handle_conditions:
        # Part 1: Simply find all valid multiplications using findall
        multiplications = re.findall(mul_pattern, memory)
        return sum(int(x) * int(y) for x, y in multiplications)
    
    # Part 2: Need finditer for positions of all patterns
    total_sum = 0
    enabled = True
    
    # Patterns for control statements
    do_pattern = r"do\(\)"
    dont_pattern = r"don\'t\(\)"
    
    # Find all relevant patterns with their positions
    all_matches = (
        [(m.start(), "mul", m) for m in re.finditer(mul_pattern, memory)] +
        [(m.start(), "do", None) for m in re.finditer(do_pattern, memory)] +
        [(m.start(), "dont", None) for m in re.finditer(dont_pattern, memory)]
    )
    
    # Sort by position in string
    all_matches.sort()
    
    # Process matches in order
    for pos, type_, match in all_matches:
        if type_ == "do":
            enabled = True
        elif type_ == "dont":
            enabled = False
        elif type_ == "mul" and enabled:
            x, y = match.groups()
            total_sum += int(x) * int(y)
    
    return total_sum

if __name__ == "__main__":
    try:
        # Read the corrupted memory
        memory = read_memory('input.txt')
        
        # Part 1: Calculate sum of all valid multiplications
        part1_sum = parse_multiplications(memory, handle_conditions=False)
        print(f"Part 1 - Sum of all multiplications: {part1_sum}")
        
        # Part 2: Calculate sum of enabled multiplications
        part2_sum = parse_multiplications(memory, handle_conditions=True)
        print(f"Part 2 - Sum of enabled multiplications: {part2_sum}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")