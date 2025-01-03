"""
Task 3: Merge Two Dictionaries
You are given two dictionaries. Write a function to merge the dictionaries into a single dictionary.
If a key appears in both dictionaries, sum the values for that key using the `get()` method.

Input:
- Two dictionaries with integer values.

Output:
- A dictionary that contains the merged keys and summed values.

Example:
Input:
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
Output:
    {'a': 1, 'b': 5, 'c': 7, 'd': 5}
"""
if __name__ == "__main__":
    # input dictionary
    dict1 = input("Enter the first dictionary (format: key:value pairs separated by commas): ").strip()
    dict2 = input("Enter the second dictionary (format: key:value pairs separated by commas): ").strip()

    # Helper function to parse input into a dictionary
    def parse_dict(input_str): # example "a:2, b:3"
        if not input_str:
            return {}
        try:
            # input_str.split(","): Splits the input string into a list of items, using commas as separators. Example: "a:2,b:3" becomes ["a:2", "b:3"].
            # (item.split(":") for item in input_str.split(",")): For each item in the list, it splits the string into a key and a value using a colon (:) as the separator. Example: "a:2" becomes ["a", "2"].
            # {k: int(v) for k, v in ...}: A dictionary comprehension that iterates over the key-value pairs from the previous step and converts the value (v) to an integer using int(v). Example: ["a", "2"] becomes {"a": 2}.
            return {k: int(v) for k, v in (item.split(":") for item in input_str.split(","))}  
        except ValueError:
            raise ValueError("Invalid input! Ensure the format is 'key:value' and values are integers.")

    # Parse input strings into dictionaries
    dict1 = parse_dict(dict1)
    dict2 = parse_dict(dict2)

    # Merge dictionaries and sum values for duplicate keys
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value

    print("Merged Dictionary:", merged_dict)