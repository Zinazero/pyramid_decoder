def read_encoded_message(file_path):
    """
    Reads the content of a file and return it as a list of strings. Accepts a
    file path as an argument and returns an Error if the file is not found.
    Otherwise, it returns a list of strings consisting of the lines of the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
                  file_lines = [line.strip() for line in file]
        return file_lines
    except FileNotFoundError:
        return "Error: File not found."
    
def sort(file_lines):
      """
      Sorts the list of strings by the number at the start of each string from
      lowest to highest value. Accepts a list of strings as an argument and 
      returns a sorted list.
      """
      def sort_key(line):
            return int(line.split()[0])
      
      sorted_strings = sorted(file_lines, key=sort_key)
      return sorted_strings

def construct_pyramid(sorted_strings):
      """
      Constructs a pyramid(or staircase) from the list elements in which each
      new list element contains an increasing number of strings, starting at 1.
      Accepts a list of strings as an argument and returns a list of lists.
      Raises a ValueError if the pyramid cannot be constructed due to
      insufficient strings.
      """
      step = 1
      subsets = []
      while len(sorted_strings) != 0:
            if len(sorted_strings) >= step:
                  subsets.append(sorted_strings[0:step])
                  sorted_strings = sorted_strings[step:]
                  step += 1
            else:
                  raise ValueError("Error: Unable to construct pyramid due to insufficient strings.")

      return subsets

def decode(message_file):
      """
      Decodes the encoded message stored in the file. Accepts a file path as an
      argument and returns a decoded message as a string.
      """
      file_lines = read_encoded_message(message_file)
      sorted_strings = sort(file_lines)
      pyramid = construct_pyramid(sorted_strings)
      decoded_message = []
      for lst in pyramid:
            strings = [' '.join(string.split()[1:]) for string in lst]
            decoded_message.append(strings[len(lst)-1])
      return ' '.join(decoded_message)

print(decode('coding_qual_input.txt'))
