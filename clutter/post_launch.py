# post install commands



root_user = config['machine_config']['root_user']
root_pwd = config['machine_config']['root_pwd']

for command in post_install_commands:
    os.system(f'VBoxManage guestcontrol {machine_name} --username {root_user} --password {root_pwd} {command}')


