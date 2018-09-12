    sudo ansible all -i inventory -u vagrant -m copy -a "src=/home/vagrant/.ssh/id_rsa.pub
    dest=~/.ssh/authorized_keys" -k
