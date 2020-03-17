if not functions -q fundle; eval (curl -sfL https://git.io/fundle-install); end

fundle plugin 'matchai/spacefish'

# Leaner than spacefish
# Fundle install was broken last time I tried
#fundle plugin 'rafaelrinaldi/pure'

# Bass makes it easy to use utilities written for Bash in fish shell.
# Example: bass export X=3
fundle plugin 'edc/bass'

# Fish plugin to improve directory navigations. Aliases for .. etc
fundle plugin 'danhper/fish-fastdir'

# pisces is a plugin for fish that helps you to work with paired symbols like () and '' in the command line
fundle plugin 'laughedelic/pisces'

fundle init
