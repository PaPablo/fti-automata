while true
do
    python test
    if [ $? -ne 0 ]; 
    then
        play /usr/share/sounds/freedesktop/stereo/bell.oga 2> /dev/null
    else
        play /usr/share/sounds/freedesktop/stereo/complete.oga 2> /dev/null
    fi
    inotifywait -e modify ./**/*.py
done
