# Symlinks keep messing things up for me (which "side" should be the link?
# Git commits the links instead of the content. Etc...), so this script can
# quickly copy the User dir here
Remove-Item -LiteralPath ".\User" -Force -Recurse
Copy-Item -LiteralPath "$HOME\AppData\Roaming\Sublime Text 3\Packages\User" -Destination "$PSScriptRoot" -Recurse
