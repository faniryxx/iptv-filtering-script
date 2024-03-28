# iptv-filtering-script

Jellyfin always struggles with enormous m3u files that contains thousands of TV show episodes and movies in addition to classic TV channels. Even VLC struggles sometimes when loading playlists.

This is a simple Python script that takes a m3u file as input, and splits it according to the group titles defined in the file.

It is also possible to export specific groups only with a Regex expression.

### Requirements
Python.

### Exemple of usage

    # Generate a different file for each group present in the m3u file
    python iptv_filtering_script.py --m3u /home/joe/TV/tv_channels.m3u --output /home/joe/TV/output

    # Generate files only for groups with the substring "USA"
    python iptv_filtering_script.py --m3u /home/joe/TV/tv_channels.m3u --output /home/joe/TV/output --regex usa

    # Generate files only for groups that start with "2024"
    python iptv_filtering_script.py --m3u /home/joe/TV/tv_channels.m3u --output /home/joe/TV/output --regex ^2024

