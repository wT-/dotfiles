if not functions -q fundle; eval (curl -sfL https://git.io/fundle-install); end

# Bass makes it easy to use utilities written for Bash in fish shell.
# Example: bass export X=3
fundle plugin 'edc/bass'

# Fish plugin to improve directory navigations. Aliases for .. etc
fundle plugin 'danhper/fish-fastdir'

# pisces is a plugin for fish that helps you to work with paired symbols like () and '' in the command line
fundle plugin 'laughedelic/pisces'

fundle init

# Hide the fish greeting
set fish_greeting ""

# Yet another prompt. Written in Rust. Fast
starship init fish | source
