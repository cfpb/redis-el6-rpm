# Defines our Vagrant environment
#
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

 # create redis node (change this to new project)

  config.vm.define :redis do |redis_config|
      redis_config.vm.box = "bento/centos-6.7"
      redis_config.vm.hostname = "redis"
      redis_config.vm.network :private_network, ip: "192.168.1.22"
      redis_config.vm.provider "virtualbox" do |vb|
      end 
      redis_config.vm.provision :shell, path: "bootstrap.sh", privileged: false
  end 

end
