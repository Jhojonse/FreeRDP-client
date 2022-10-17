# https://unix.stackexchange.com/questions/202891/how-to-know-whether-wayland-or-x11-is-being-used

# Alt:
# https://itsfoss.com/check-wayland-or-xorg/

command = "loginctl list-sessions --no-legend"

output = subprocess(command)

session = split(output, " ")

return session[0]
