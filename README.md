### ShellzGen
ShellzGen quickly creates [shellz](https://github.com/evilsocket/shellz) shells.

### How to Use
0. Modify ```self.hosts``` for the appropriate competition subnets. 

1. Execute wiith the following arguments:

```
./shellzgen.py -i ssh_primary_ident -o /tmp/ -g redteam
```
* ```-i```: specify identity to use.
* ```-o```: specify out dir.
* ```-g```: specify group for user.

### Use Cases
* Red vs Blue competitions
* Mass ssh command execution against hosts without the overhead Ansible.
