def read_reports(filename):
    """
    Reads grid reports from a text file where each line contains reports separated by whitespace.
    
    Args:
        filename (str): Path to the text file containing reports
        
    Returns:
        list(list): Lists containing reports
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        ValueError: If the file contains invalid data format
    """
    # Initialize empty reports
    reports = []
    
    try:
        # Open and read the file
        with open(filename, 'r') as file:
            # Process each line in the file
            for line_number, line in enumerate(file, 1):
                # Strip whitespace and split the line
                values = line.strip().split()
                try:
                    reports.append([int(v) for v in values])
                except ValueError:
                    raise ValueError(f"Invalid number format at line {line_number}. Both values must be integers.")
                    
        return reports
        
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")

def is_safe_sequence(sequence):
    """
    Check if a sequence is safe according to the basic rules:
    - Must be strictly increasing or decreasing
    - Adjacent numbers must differ by at least 1 and at most 3
    
    Args:
        sequence: List of integers representing the levels
        
    Returns:
        bool: True if the sequence follows the safety rules
    """
    if len(sequence) <= 1:
        return True
        
    # Get the first difference to determine direction
    diff = sequence[1] - sequence[0]
    if abs(diff) < 1 or abs(diff) > 3:
        return False
        
    increasing = diff > 0
    
    # Check all pairs maintain the pattern
    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        
        # Verify difference magnitude
        if abs(diff) < 1 or abs(diff) > 3:
            return False
            
        # Verify direction remains consistent
        if (increasing and diff <= 0) or (not increasing and diff >= 0):
            return False
            
    return True

def is_safe_with_dampener(sequence):
    """
    Check if a sequence is safe when allowing for one outlier to be removed.
    The sequence must either be safe without removal or become safe after
    removing exactly one element.
    
    Args:
        sequence: List of integers representing the levels
        
    Returns:
        bool: True if sequence is or can become safe with one removal
    """
    # First check if already safe without dampener
    if is_safe_sequence(sequence):
        return True
        
    # Try removing each element to see if sequence becomes safe
    for i in range(len(sequence)):
        remaining_sequence = sequence[:i] + sequence[i + 1:]
        if is_safe_sequence(remaining_sequence):
            return True
            
    return False

if __name__ == "__main__":
    try:
        # Read the reports from the file
        reports = read_reports('input.txt')
        
        # Part 1: Count reports that are safe without the dampener
        safe_count = sum(is_safe_sequence(report) for report in reports)
        print(f"Part 1 - Safe reports without dampener: {safe_count}")
        
        # Part 2: Count reports that are safe with the dampener
        safe_with_dampener = sum(is_safe_with_dampener(report) for report in reports)
        print(f"Part 2 - Safe reports with dampener: {safe_with_dampener}")
    
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")