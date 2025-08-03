#!/usr/bin/env python3
import os
import shutil
import shlex

folder_path = input("Enter target path: ").strip()
raw_extensions = input("Enter target filetypes (e.g., mp4 mov jpeg): ") #can be left blank, in which case it will only use keyword
raw_key_words = input("Enter identifiable keywords (e.g., 111 applesauce 'ex wife'): ") #can be left blank, in which case it will only use extensions
new_destination = input("Enter name of new folder: ").strip()

#creating destination path
new_destination = os.path.join(folder_path, new_destination)
os.makedirs(new_destination, exist_ok=True)

#cleaning ext
extensions = []
for ext in raw_extensions.strip().split():
    if ext.startswith("."):
        extensions.append(ext)
    else:
        extensions.append("." + ext)
extensions = tuple(extensions)

#cleaning key_words
key_words = tuple(shlex.split(raw_key_words))

#filter through files
target_files = []
for filename in os.listdir(folder_path):
    full_path = os.path.join(folder_path, filename)
    if not os.path.isfile(full_path):
        continue

    ext_matching = not extensions or filename.lower().endswith(extensions)
    kw_match = not key_words or any(filename.lower().startswith(kw.lower()) for kw in key_words)

    if ext_matching and kw_match:
        target_files.append(filename)

#showcase
print("\nFiles that will be relocated:")
for files in target_files:
    print("  " + files)

#confirmation
confirm = input(f"\nProceed to move {len(target_files)} file(s)? (yes/no): ").strip().lower()
if confirm == "yes":
    for filename in target_files:
        shutil.move(os.path.join(folder_path, filename), os.path.join(new_destination, filename))
    print("Transfer complete.")
else:
    print("Transfer aborted.")
