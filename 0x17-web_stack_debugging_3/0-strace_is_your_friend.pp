exec { 'fix-apache-error':
  command => 'chmod 755 /path/to/file/or/directory',
  onlyif  => 'test -f /path/to/file/or/directory && !(stat -c %a /path/to/file/or/directory | grep 755)',
}
