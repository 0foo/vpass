### About

* Vagrant is great but requires navigating to the folder with the Vagrantfile when you want to work with a VM
* multipass is great but stashes the VM's it creates in weird places on the file system that aren't easily portable
* Combine the two to have vpass
* A very light wrapper around vagrant and virtual box allowing control of VM's from anywhere on the command line and some additional functionality as well.
* I `think` this works on Windows, all of the code was written to be portable, but hasn't been tested on windows, so there may or may not be a bug.


### Dependencies
1. vagrant is installed and working on the CLI
2. python3 on the system path
3. virtual box and virtual box extensions installed and working on the CLI
  

### Install
1. pull this repo down and add the bin directory to the path.


### To use
```
    A very light wrapper around vagrant allowing control of VM\'s from anywhere on the command line.
    Simply replace the command vagrant with the command vpass and pass in a machine name, no need to manually navigate to the machines folder.
    The config files for each  machine are found at <home directory>/vpass/machines and can be changed after creation to customize the vm.
    Inspired by Ubuntu multipass.
    
    
    Usage: vpass <command> <machine> [options]
    
    Vpass Specific Commands
    -------------------------
    launch: launches a new instance
    list: lists all instances available with vpass
    destroy/delete: destroys the instance
    start: start VM
    stop: stop the VM
    
    
    Any regular vagrant commands will work with vpass without the need to manually navigate to the machines directory.

    
    Examples: 
    vpass launch 
    vpass list
    vpass ssh cocky-wozniak
    vpass suspend cocky-wozniak
    vpass up cocky-wozniak
    vpass destroy cocky-wozniak
    
```

