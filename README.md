### ShellzGen
ShellzGen quickly creates [shellz]() shells.

### How to Use
0. Modify ```self.hosts``` for the appropriate competition subnets. 

Execute wiith the following arguments:

```
./shellzgen.py -i ssh_primary_ident -o /tmp/ -g redteam
```
* ```-i```: specify identity to use.
* ```-o```: specify out dir.
* ```-g```: specify group for user.

### Use Cases
* Red vs Blue competitions
* Mass ssh command execution against hosts.
