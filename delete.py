#!/usr/bin/env python3
import os

folder_path = input("Enter path: ").strip()
raw_extensions = input("Enter target filetypes (e.g., mp4 mov jpeg): ")

#cleaning ext
extensions = []
for ext in raw_extensions.strip().split():
    if ext.startswith("."):
        extensions.append(ext)
    else:
        extensions.append("." + ext)
extensions = tuple(extensions)

#showcase
print("\nFiles that will be deleted:")
for filename in os.listdir(folder_path):
    if filename.endswith(extensions):
        print("  " + filename)

#confirmation
confirm = input("Proceed with deletion? (yes/no): ").lower()
if confirm == "yes":
    for filename in os.listdir(folder_path):
        if filename.endswith(extensions):
            os.remove(os.path.join(folder_path, filename))
    print("Deletion complete.")
else:
    print("Aborted. No files were deleted.")

