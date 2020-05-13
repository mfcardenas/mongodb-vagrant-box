Vagrant.configure("2") do |config|
  config.vm.box     = "ubuntu/trusty64"

  config.vm.network :forwarded_port, host: 17017, guest: 27017  

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "manifests"
    puppet.manifest_file  = "base.pp"
    puppet.module_path    = "modules"
    puppet.facter = {
      "fqdn" => "mongobox"
    }
  end

  config.vm.synced_folder "files/", "/srv/files"

  config.vm.provision "shell", 
    inline: "cd /srv/files && mongorestore"
end
