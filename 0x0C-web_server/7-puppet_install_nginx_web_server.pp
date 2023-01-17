# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Create custom "Hello World!" page
file { '/usr/share/nginx/html/index.html':
  ensure => file,
  content => "Hello World!",
}

# Create the redirect configuration file
file { '/etc/nginx/sites-available/redirect.conf':
  ensure => file,
  content => 'server {
    listen 80;
    server_name _;
    return 301 /redirected;
    location /redirect_me {
      return 301 /redirected;
    }
  }',
}

# Create the redirected page
file { '/usr/share/nginx/html/redirected.html':
  ensure => file,
  content => "You have been redirected!",
}

# Create a symlink to the redirect configuration file
file { '/etc/nginx/sites-enabled/redirect.conf':
  ensure => link,
  target => '/etc/nginx/sites-available/redirect.conf',
}

# Remove the default configuration file
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}

# Reload Nginx to apply the changes
service { 'nginx':
  ensure => running,
  subscribe => File['/etc/nginx/sites-enabled/redirect.conf'],
  refreshonly => true,
}

