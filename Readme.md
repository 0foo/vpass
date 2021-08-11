### About

* Vagrant is great but requires navigating to the folder with the Vagrantfile when you want to work with a VM
* multipass is great but stashes the VM's it creates in weird places on the file system that aren't easily portable
* Combine the two to have vpass
* A very light wrapper around vagrant allowing control of VM's from anywhere on the command line.


### Install
1. Make sure vagrant is installed and working
2. pull this repo down and add the bin directory to the path.


### To use
```
vpass help
vpass launch 
vpass list
vpass ssh cocky-wozniak
vpass suspend cocky-wozniak
vpass up cocky-wozniak
vpass destroy cocky-wozniak
```

* Any regular vagrant commands will work with vpass, just pass in the machine name instead of navigating to the directory with the Vagrantfile.