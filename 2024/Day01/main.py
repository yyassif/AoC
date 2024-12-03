def read_coordinates(filename):
    """
    Reads coordinates from a text file where each line contains two numbers separated by whitespace.
    
    Args:
        filename (str): Path to the text file containing coordinates
        
    Returns:
        tuple: Two lists containing left and right coordinates respectively
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        ValueError: If the file contains invalid data format
    """
    # Initialize empty lists to store coordinates
    left_coords = []
    right_coords = []
    
    try:
        # Open and read the file
        with open(filename, 'r') as file:
            # Process each line in the file
            for line_number, line in enumerate(file, 1):
                # Strip whitespace and split the line
                values = line.strip().split()
                
                # Check if we have exactly two values
                if len(values) != 2:
                    raise ValueError(f"Invalid data format at line {line_number}. Expected 2 values, got {len(values)}")
                
                try:
                    # Convert strings to integers and append to respective lists
                    left = int(values[0])
                    right = int(values[1])
                    left_coords.append(left)
                    right_coords.append(right)
                except ValueError:
                    raise ValueError(f"Invalid number format at line {line_number}. Both values must be integers.")
                    
        return left_coords, right_coords
        
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")

def calculate_distance(left_coords, right_coords):
    """
    Calculate total distance between sorted coordinate pairs.
    
    Args:
        left_coords: List of integers from left column
        right_coords: List of integers from right column
        
    Returns:
        int: Total distance between paired coordinates
    """
    # Sort both lists
    left_sorted = sorted(left_coords)
    right_sorted = sorted(right_coords)
    
    # Calculate total distance
    total_distance = sum(abs(x - y) for x, y in zip(left_sorted, right_sorted))
    return total_distance

def calculate_similarity_score(left_coords, right_coords):
    """
    Calculate similarity score by multiplying each left number by its frequency in right list.
    
    Args:
        left_coords: List of integers from left column
        right_coords: List of integers from right column
        
    Returns:
        int: Total similarity score
    """
    # Calculate similarity score
    similarity_score = sum(x * right_coords.count(x) for x in left_coords)
    return similarity_score

if __name__ == "__main__":
    try:
        # Read coordinates from input file
        left_coords, right_coords = read_coordinates('input.txt')
        
        # Part 1: Calculate total distance
        total_distance = calculate_distance(left_coords, right_coords)
        print(f"Part 1 - Total distance between lists: {total_distance}")
        
        # Part 2: Calculate similarity score
        similarity_score = calculate_similarity_score(left_coords, right_coords)
        print(f"Part 2 - Similarity score: {similarity_score}")
    
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
