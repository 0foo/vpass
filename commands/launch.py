'''
References for some code in this file:
https://stackoverflow.com/questions/4028904/what-is-the-correct-cross-platform-way-to-get-the-home-directory-in-python
'''

from lib import random_names
import os, sys
from pathlib import Path
from lib import download


def run():
    # Create paths in home to put files
    home = str(Path.home())
    vpass_home_dir = os.path.join(home, 'vpass')
    if not os.path.exists(vpass_home_dir):
        print("vpass home directory doesnt exist, creating")
        os.makedirs(vpass_home_dir)
    if not os.path.exists(f"{vpass_home_dir}/iso_files"):
        os.makedirs(f"{vpass_home_dir}/iso_files")

    # Create a random machine name
    machine_name = random_names.run()

    # Check if file exists then download if not
    iso_name = "ubuntu-21.04-live-server-amd64.iso"
    iso_url = "https://releases.ubuntu.com/21.04/ubuntu-21.04-live-server-amd64.iso"
    iso_location = f"{vpass_home_dir}/iso_files/{iso_name}"
    if not os.path.exists(iso_location):
        print("Iso file doesn't exist, pulling from repository.")
        print("Pulling from Ubuntu repository:" + iso_url)
        download.with_progress_bar(iso_url, iso_location)

    commands = [
        f'VBoxManage createvm --name {machine_name} --ostype "Debian_64" --register --basefolder {vpass_home_dir}',
        f'VBoxManage modifyvm {machine_name} --ioapic on',
        f'VBoxManage modifyvm {machine_name} --memory 1024 --vram 128',
        f'VBoxManage modifyvm {machine_name} --nic1 nat',
        f'VBoxManage createhd --filename {vpass_home_dir}/{machine_name}/{machine_name}_DISK.vdi --size 80000 --format VDI',
        f'VBoxManage storagectl {machine_name} --name "SATA Controller" --add sata --controller IntelAhci',
        f'VBoxManage storageattach {machine_name} --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium  {vpass_home_dir}/{machine_name}/{machine_name}_DISK.vdi',
        f'VBoxManage storagectl {machine_name} --name "IDE Controller" --add ide --controller PIIX4',
        f'VBoxManage storageattach {machine_name} --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --medium {vpass_home_dir}/iso_files/{iso_name}',
        f'VBoxManage modifyvm {machine_name} --boot1 dvd --boot2 disk --boot3 none --boot4 none',
    ]

    print(f"Creating {machine_name}")
    for command in commands:
        # print(command)
        os.system(command)

    os.system(f'VBoxManage startvm {machine_name} --type headless')
    print(f"{machine_name} created and started.")





