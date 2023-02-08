# adds holberton as a user

exec { 'add_holberton_user':
  command => 'adduser holberton',
  unless  => 'id holberton',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin'
}

exec { 'add_holberton_to_sudo':
  command => 'usermod -aG sudo holberton',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin'
}

exec { 'create_testfile':
  command => 'touch /home/holberton/testfile && chm
od 755 /home/holberton/testfile',
  creates => '/home/holberton/testfile',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
