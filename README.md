AWS CLI v2
=========

Install AWS CLI v2 using the official install binary.

Tested On
------------
* Ubuntu 22

Tested With
-----------
* Ansible 2.10.8

Requirements
------------
1. Outbound internet connection.
2. unzip 

Variables
--------------

| var name | description | required? | default value |
| ---      | ---   | --- | --- |
| awscli2__executable_temp_dir | download location for the installer, must be executable, don't use /tmp on hardened OSes| y | /tmp |
| awscli2__version | version to install, e.g. '2.8.9' | y | latest |
| awscli2__upgrade | change to true if upgrading an existing installation | y | false |
| awscli2__bin_dir | symlink dir (ideally, one already inside your $PATH) | y | /usr/local/bin | 
| awscli2__install_dir | where to install awscli v2 | y | /usr/local/aws-cli |


License
-------

BSD

Credits
------------------
Original author: https://github.com/deekayen/ansible-role-awscli2
