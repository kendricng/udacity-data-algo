import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.exists(path):
        files_with_suffix = []
    else:
        return []

    for f in os.listdir(path):
        fp = os.path.join(path, f)

        if os.path.isfile(fp) and fp.endswith(suffix):
            files_with_suffix.append(fp)

        if os.path.isdir(fp):
            files_with_suffix.extend(find_files(suffix, fp))

    return sorted(files_with_suffix)

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(find_files(".c", "./testdir"))

# Test Case 2
print(find_files(".h", "./testdir"))

# Test Case 3
print(find_files(".cpp", "./testdir"))
print(find_files(".c", "./testdir/subdir1"))
print(find_files(".c", ".."))
