#!/usr/bin/env python

import subprocess, shlex, json

def get_threat_list():
    isi_threat_list_raw = "isi antivirus reports threats list --format json -a -z"
    isi_threat_list_split = shlex.split(isi_threat_list_raw)
    isi_threat_list_cmd = subprocess.Popen(isi_threat_list_split, stdout = subprocess.PIPE)
    isi_threat_list_strings = isi_threat_list_cmd.communicate()[0]
    isi_threat_list_results = json.loads(isi_threat_list_strings)

    return isi_threat_list_results

def release_threats():
    isi_threat_list_results = get_threat_list()
    for i in isi_threat_list_results:
        isi_release_quarantine_raw = "isi antivirus release --verbose"
        isi_release_quarantine_split = shlex.split(isi_release_quarantine_raw)
        isi_release_quarantine_split.append(i["file"])
        isi_release_quarantine_cmd = subprocess.Popen(isi_release_quarantine_split, stdout = subprocess.PIPE)
        isi_release_quarantine_results = isi_release_quarantine_cmd.communicate()[0]

        print(isi_release_quarantine_results)

def main():
    release_threats()

if __name__ == '__main__':
    main()
