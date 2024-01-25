#! /bin/bash

case ${1,,} in
    luis | admin)
        echo "Hello, you're the boss here!"
        ;;
    help)
        echo "Just enter your username"
        ;;
    *)
        echo "I don't know who you are. But you're not the boss of me!"
esac