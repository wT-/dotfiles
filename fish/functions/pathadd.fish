# From https://github.com/matchai/dotfiles
# Use like:
#	pathadd ~/.cargo/bin
function pathadd -a dir
  if test -d $dir
    set -gx PATH $dir $PATH
  end
end
