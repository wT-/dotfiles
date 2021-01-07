if not functions -q fundle; eval (curl -sfL https://git.io/fundle-install); end

# Prompt. Should use Spaceship instead
# fundle plugin 'matchai/spacefish'

# Leaner than spacefish
# Fundle install was broken last time I tried
# fundle plugin 'rafaelrinaldi/pure'

# Bass makes it easy to use utilities written for Bash in fish shell.
# Example: bass export X=3
fundle plugin 'edc/bass'
# Similar deal
# fundle plugin 'oh-my-fish/plugin-foreign-env'

# Fish plugin to improve directory navigations. Aliases for .. etc
fundle plugin 'danhper/fish-fastdir'

# pisces is a plugin for fish that helps you to work with paired symbols like () and '' in the command line
fundle plugin 'laughedelic/pisces'

fundle init

# Remove directory truncation (defaults to only 3)
set -x SPACEFISH_DIR_TRUNC 0

# Completions for Kitty(?)
kitty + complete setup fish | source

# Yet another prompt. Written in Rust. Fast
starship init fish | source
starship completions | source
