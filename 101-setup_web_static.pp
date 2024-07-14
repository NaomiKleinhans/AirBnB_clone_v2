# Puppet manifest to set up the web_static deployment

# Create /data directory
file { '/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create /data/web_static directory
file { '/data/web_static':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create /data/web_static/releases directory
file { '/data/web_static/releases':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create /data/web_static/shared directory
file { '/data/web_static/shared':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create /data/web_static/releases/test directory
file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create a simple index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create a symbolic link from /data/web_static/current to /data/web_static/releases/test
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Ensure correct permissions for all directories and files
file { '/data':
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}
