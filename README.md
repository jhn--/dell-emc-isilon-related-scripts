# dell-emc-isilon-related-scripts

Just a bunch of scripts that tries to make life easier for people.

Currently contains just one tool/script.

# isi_release_quarantined_files.py
Releases _ALL_ quarantined files in Isilon. 

Basic script, no error checks, results get printed out on terminal. 
For situations where people tried some POC on antivirus systems and forgot to deal w/ the whitelisting policies and end up seeing a ton of false positives and when trying to release files from quarantine, realised that the GUI doesn't allow release of multiple files.

get_threat_list() - get the list of quarantined files in json format.
release_threats() - calls get_threat_list() to get list of quarantined files and releases individual files from quarantine.
