if not functions -q fundle; eval (curl -sfL https://git.io/fundle-install); end

fundle plugin 'matchai/spacefish'

# Leaner than spacefish
# Fundle install was broken last time I tried
#fundle plugin 'rafaelrinaldi/pure'

fundle plugin 'edc/bass'
fundle plugin 'danhper/fish-fastdir'
fundle plugin 'oh-my-fish/plugin-foreign-env'
fundle plugin 'laughedelic/pisces'

fundle init
