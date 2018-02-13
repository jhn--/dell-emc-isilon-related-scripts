# isi_release_quarantined_files
Releases _ALL_ quarantined files in Isilon. 

Basic script, no error checks, results get printed out on terminal. 

get_threat_list() - get the list of quarantined files in json format.
release_threats() - calls get_threat_list() to get list of quarantined files and releases individual files from quarantine.
