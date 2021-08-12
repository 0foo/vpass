### About

* Vagrant is great but requires navigating to the folder with the Vagrantfile when you want to work with a VM
* multipass is great but stashes the VM's it creates in weird places on the file system that aren't easily portable
* Combine the two to have vpass
* A very light wrapper around vagrant allowing control of VM's from anywhere on the command line.
* I `think` this works on Windows, all of the code was written to be portable, but hasn't been tested on windows, so there may or may not be a bug.


### Install
1. Make sure vagrant is installed and working, as well as python3 on the system path
2. pull this repo down and add the bin directory to the path.


### To use
```
Examples:
vpass help
vpass launch # creates a new VM
vpass list # lists all the vpass VMs
vpass ssh cocky-wozniak # ssh into a vpass VM
vpass suspend cocky-wozniak
vpass up cocky-wozniak
vpass destroy cocky-wozniak
```
* view all of the vpass machines with vpass list
* Any regular vagrant commands will work with vpass, just pass in the machine name instead of navigating to the directory with the Vagrantfile.
