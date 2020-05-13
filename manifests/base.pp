class {'::mongodb::globals':
  manage_package_repo => true
}->
class {'::mongodb::server':
  bind_ip => ['0.0.0.0']
}
class { 'mongodb::client':
  ensure => true 
}

package { 'mongodb-org-tools':
    tag => 'mongodb'
}