#!/usr/bin/python3
'''
Script to generate shellz shellz for Collegiate competition.s
'''

import json
import sys
import argparse

class ShellzGen():
    '''
    Leverage blueteam document to auto fill and create shellz for competition
    Linux VMs
    '''
    def __init__(self, args):
        self.hosts = ["10.X.1.10", "10.X.2.10", "10.X.2.20", "10.X.2.30",
                      "10.X.3.30", "10.X.3.40", "10.X.3.50"]

        self.host_names = {"1.10" : "parrot-acidburn", "2.10" : "fedora-pwnsauce",
                           "2.20" : "debian10-viral", "2.30" : "ubuntu1804-anarachos",
                           "3.30" : "centos7-kayla", "3.40" : "debian9-avunit",
                           "3.50" : "centos7-tflow"}

        self.template = """
                { 
                    "name": "Ubuntu-1804-Dev", "host": "172.16.29.152", 
                "port": 22, "identity": "default", "type": "ssh", "ciphers": null,
                "https": true, "insecure": false, "enabled": true, "groups": [ "vms"],
                "proxy": { "address": "", "port": 0, "username": "", "password": "" }, 
                "tunnel": { "local": { "address": "", "port": 0 }, "remote": {
                "address": "", "port": 0 } }
                }
                """

        self.json_data = json.loads(self.template)
        self.out_filepath = args.o

    def gen_shellz(self):
        '''
        Loop through each host and create a team vm to be stored in self.out_filepath
        shellz's shells entry.
        '''
        for host in self.hosts:
            for i in range(1, 14):
                self.json_data["host"] = host.replace("X", str(i))
                try:
                    new_host_name = self.host_names.get(self.json_data["host"][5:]) \
                            + "-team-" + str(i)
                except TypeError:
                    new_host_name = self.host_names.get(self.json_data["host"][6:]) \
                            + "-team-" + str(i)

                self.json_data["name"] = new_host_name
                self.json_data["identity"] = args.i
                groups = [args.g, new_host_name.split("-")[0]]
                self.json_data["groups"] = groups
                try:
                    with open(self.out_filepath + new_host_name+".json", "w+") as fout:
                        fout.write(json.dumps(self.json_data))
                except IOError as err:
                    print("[!] Something has gone horribly wrong. %s" % str(err))
                    sys.exit(1)

        print("[+] Success! Run shellz -list")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", type=str, required=True,
            help="Specify identity for shellz profile")

    parser.add_argument("-o", type=str, required=True,
            help="Specify dir to write out to.")

    parser.add_argument("-g", type=str, required=True, default="helloworld",
            help="Specify group to include shellz into.")

    args = parser.parse_args()

    shells = ShellzGen(args)
    shells.gen_shellz()
