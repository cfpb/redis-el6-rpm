# Installation instructions

## Installation

Build RPM using Vagrant

1. The repo is cloned into a local sandbox
2. Run "vagrant up" to build the VM.
3. Run "vagrant ssh" to connect to VM.
4. Run "rpmbuild -ba SPECS/redis.spec" to build the redis rpm package.


Build RPM on server

1. Once repo is cloned, run "sh ./bootstrap.sh"
2. cd to ~/rpmbuild 
3. Run "rpmbuild -ba SPECS/redis.spec"

Installing the RPM 

Install the built RPM by running "sudo yum install RPMS/x86_64/redis-3.0.7-1.el6.x86_64.rpm"


