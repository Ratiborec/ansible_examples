# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
 config.vm.box = "sbeliakou/centos"
  config.vm.box_version = "7.5"
  

  config.vm.define "ansible" do |ansible|

    ansible.vm.hostname = "ansible"
    ansible.vm.network "private_network", ip: "192.168.1.100"
    config.vm.provider "virtualbox" do |vb|
   	vb.name = "Ansible"
	vb.gui = false
  	vb.memory = "1024"
    end
  end


  config.vm.define "web" do |web|
    
    web.vm.hostname = "web"
    web.vm.network "private_network", ip: "192.168.1.101"
    config.vm.provider "virtualbox" do |vb|
        vb.name = "web"
        vb.gui = false
        vb.memory = "1024"
    end
  end


  config.vm.define "app" do |app|

    app.vm.hostname = "app"
    app.vm.network "private_network", ip: "192.168.1.102"
    config.vm.provider "virtualbox" do |vb|
        vb.name = "app"
        vb.gui = false
        vb.memory = "1024"
    end
  end




 
  end
  
  
  

