import os

def print_directory_contents(dir_path):
    for root, dirs, files in os.walk(dir_path):
        level = root.replace(dir_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")

# Directory paths to print
directory_paths = [
    '/home/surafelamsalu21/Pictures/Dashboars For Job/club_dashboard/dashboard',
    '/home/surafelamsalu21/Pictures/Dashboars For Job/club_dashboard/club_dashboard'
]

# Print contents for each directory path
for path in directory_paths:
    print(f"\nContents of {path}:")
    print_directory_contents(path)
