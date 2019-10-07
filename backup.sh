#!/bin/bash

date=$(date +%Y-%m)
date_diff=1
folder_date=$(date -d "$data - $date_diff months" +%Y-%m)

working_dir="/home/jweaver/matrix_backup"
final_dest="/var/www/html/nextcloud/data/jweaver/files/Matrix_Backup/$folder_date"

# Get files from Matrix server
ncftpget -f login.cfg -R -T . -DD Media/

# Rename files with their proper extensions
python rename_files.py

# Move files into nextcloud folder
mkdir $final_dest && cp $working_dir/Media/*.* $final_dest

# Make files owned by www-data
chown -R www-data:www-data $final_dest

# Remove files from working directory
rm -rf $working_dir/Media
rm file_names.txt

# Recache files
sudo -u www-data php /var/www/html/nextcloud/occ files:scan --all

