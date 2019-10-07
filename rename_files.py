#!/usr/bin/python3.5

import subprocess
	
def get_file_name_type():
	files = []
	subprocess.call('ls Media/* > file_names.txt', shell=True)
	with open('file_names.txt','r') as f:
		data = f.read()
		data = data.split('\n')
	for name in data:
		if name != '':
			ftype = subprocess.check_output('file %s' % name, shell=True)
			if 'ASCII' in ftype:
				pass
			else:
				if 'JPEG' in ftype:
					files.append({name[6:]:'.jpg'})
				elif 'PNG' in ftype:
					files.append({name[6:]:'.png'})
				elif 'MP4' in ftype:
					files.append({name[6:]:'.mp4'})
				elif 'MOV' in ftype:
					files.append({name[6:]:'.mov'})

	return files

def rename_files(files):
	for fn in files:
		for k,v in fn.items():
			new_fn = k+v
			subprocess.call('mv Media/%s Media/%s' % (k,new_fn), shell=True)

def dedupe():
	new_files = subprocess.check_output('ls Media/*', shell=True)
	new_files = new_files.split('\n')
	trimmed_files = []
	for x in new_files:
		if x != '':
			trimmed_files.append(x[6:])
	existing_files = subprocess.check_output('ls -R /var/www/html/nextcloud/data/jweaver/files/Matrix_Backup/*', shell=True)
	for item in trimmed_files:
		if item != '':
			if item in existing_files:
				print("Found dupe!")
				subprocess.call('rm Media/%s' % item, shell=True)
			

files = get_file_name_type()
rename_files(files)
dedupe()

