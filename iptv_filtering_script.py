import argparse
import os
import re
import sys


parser = argparse.ArgumentParser("iptv_filtering_script")
parser.add_argument("--m3u", help="A m3u file stored locally.", type=str, required=True)
parser.add_argument("--output", help="Output folder.", type=str, required=True)
parser.add_argument("--regex", help="Groups to export in regex format. Case insensitive.", type=str)
args = parser.parse_args()
m3u_file = args.m3u
output_folder = args.output
groups_regex = args.regex if args.regex else "."

group_titles = []

# Check if m3u file exists
if os.path.isfile(m3u_file):
    with open(m3u_file) as f:
        content = f.readlines()
        if content[0].strip("\n") == "#EXTM3U":
            # Delete first line with #EXTM3U tag
            content.pop(0)
            # Get unique groups
            for line in content:
                if 'group-title="' in line:
                    group_titles.append(line.split('group-title="')[-1].split('"')[0])
            group_titles = sorted(list(set(group_titles)))
            
            # Only keep groups according to regex pattern if any is provided
            pattern = re.compile(groups_regex, re.IGNORECASE)
            group_titles = [group for group in group_titles if pattern.search(group)]            

            # Assemble EXT info and media file link into one line
            concatenated_content = []
            for i in range(0, len(content), 2):
                if i+1 < len(content):
                    concatenated_content.append(content[i].strip() + ' stream_link=' + content[i+1].strip())

            # Create one folder and m3u file per group
            for group in group_titles:
                os.makedirs(f"{output_folder}/{group}", exist_ok=True)
                with open(f"{output_folder}/{group}/channels.m3u", "w+") as f:
                    f.writelines("#EXTM3U\n")
                    for i in range(0, len(concatenated_content)):
                        if group in concatenated_content[i]:
                            f.writelines(f'{concatenated_content[i].split(" stream_link=")[0]}\n')
                            f.writelines(f'{concatenated_content[i].split(" stream_link=")[-1]}\n')

        else:
            print(f"File {m3u_file} is an invalid m3u file.")
            sys.exit(-1)

else:
    print(f"File {m3u_file} does not exist.")
    sys.exit(-1)
