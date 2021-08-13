# kill a process named killmenow

exec { 'kill_process':
  command  => 'pkill -9 "killmenow"',
  provider => 'shell'
}
