### Backup of media from Matrix Synapse server

This collection of scripts does the following:

- Moves all new media on Matrix chat server to a new folder in my home directory
- From nextcloud instance (residing on a different server), retrieves said files via FTP
- Renames all files with the correct extension for importing into nextcloud (files on Matrix server are named w/o extensions which causes problems)
- Creates new folder with appropriate month and year for organization purposes
- Moves files to above Nextcloud folder and gives proper ownership
- Refreshes Nextcloud cache so that photos are recognizes as being present

All files belong on nextcloud instance, other than two cronjobs in cronjobs.txt that should be scheduled on the chat server.

Requires vsftpd to be installed on the chat server.


