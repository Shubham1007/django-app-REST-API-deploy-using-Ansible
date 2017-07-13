# # django REST-API deploy using Ansible # # 

**Introduction**
Configuration management systems are designed to make controlling large numbers of servers easy for administrators and operations teams. They allow you to control many different systems in an automated way from one central location. **Ansible** is a great alternative to these options because it has a much smaller overhead to get started.

**How Does Ansible Work?**
Ansible works by configuring client machines from an computer with Ansible components installed and configured. It communicates over normal SSH channels in order to retrieve information from remote machines, issue commands, and copy files. Because of this, an Ansible system does not require any additional software to be installed on the client computers.

This is one way that Ansible simplifies the administration of servers. Any server that has an SSH port exposed can be brought under Ansible's configuration umbrella, regardless of what stage it is at in its life cycle.

Any computer that you can administer through SSH, you can also administer through Ansible.

Ansible takes on a modular approach, making it easy to extend to use the functionalities of the main system to deal with specific scenarios. Modules can be written in any language and communicate in standard JSON.

Configuration files are mainly written in the YAML data serialization format due to its expressive nature and its similarity to popular markup languages. Ansible can interact with clients through either command line tools or through its configuration scripts called Playbooks.

Installing Ansible


``` sudo apt-add-repository ppa:ansible/ansible ```


Press ENTER to accept the PPA addition.


``` sudo apt-get update ```

``` sudo apt-get install ansible ```


After completing the installation, change the ```playbook.yml``` and ```hosts``` file contents where necessary. Goto the ```gunicorn.service``` in devops directory and change values in ```WorkingDirectory``` and ```ExecStart``` of your needs. You also need to place your ip, domain, root, proxy_pass in ```myproject``` file which is an nginx file.

run: **ansible-playbook -i hosts -s playbook.yml -v**

**ENJOY**
