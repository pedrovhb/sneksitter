import tree_sitter_languages

parser = tree_sitter_languages.get_parser("python")

sample_code_bytes = bytes(
    """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
""",
    "utf8",
)

tree = parser.parse(sample_code_bytes)


def collect_function_name_nodes(node, function_name_nodes):
    if node.type == "function_definition":
        # Get the function name node
        function_name_node = node.child_by_field_name("name")
        if function_name_node:
            # Add the function name node to the list
            function_name_nodes.append(function_name_node)

    # Recurse for each child node
    for child in node.children:
        collect_function_name_nodes(child, function_name_nodes)


# Collect function name nodes
function_name_nodes = []
collect_function_name_nodes(tree.root_node, function_name_nodes)

# Extract the byte positions and text for each function name node
nodes_to_replace = [
    (node.start_byte, node.end_byte, sample_code_bytes[node.start_byte : node.end_byte].decode())
    for node in function_name_nodes
]


from intervaltree import Interval, IntervalTree

# Define the replacements
# We will replace 'add' with 'sum' and 'subtract' with 'difference'
replacements = [(5, 8, "sum"), (38, 46, "difference")]

# Create an IntervalTree for the replacements
intervals = IntervalTree()
for start, end, replacement in replacements:
    intervals[start:end] = replacement


# Function to apply replacements on a bytes object
def apply_replacements_bytes(code_bytes, intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x.begin)
    offset = 0
    new_code_bytes = b""

    last_end = 0
    for interval in sorted_intervals:
        start, end = interval.begin, interval.end
        replacement = interval.data

        # Adjust for previous replacements
        adjusted_start = start + offset
        adjusted_end = end + offset

        # Add the text before the replacement and the replacement itself (as bytes)
        new_code_bytes += code_bytes[last_end:adjusted_start] + replacement.encode()

        # Update the offset and last end position
        offset += len(replacement) - (end - start)
        last_end = adjusted_end

    # Add the remaining part of the code
    new_code_bytes += code_bytes[last_end:]

    return new_code_bytes


# Apply the replacements on the bytes object
new_code_bytes = apply_replacements_bytes(sample_code_bytes, intervals)
print(new_code_bytes.decode())
