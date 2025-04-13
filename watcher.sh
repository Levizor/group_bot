#!/usr/bin/env bash

echo "Starting interactive bot runner..."
echo "Type anything to restart the bot, or 'quit' to stop."

run_bot() {
    python3 src/main.py &
    bot_pid=$!
}

stop_bot() {
    if [[ -n "$bot_pid" ]] && ps -p $bot_pid > /dev/null; then
        kill $bot_pid
        wait $bot_pid 2>/dev/null
    fi
}

run_bot

while true; do
    read -r -t 1 input
    if [[ $? -eq 0 ]]; then
        if [[ "$input" == "quit" ]]; then
            echo "Stopping bot..."
            stop_bot
            break
        else
            echo "Restarting bot..."
            stop_bot
            run_bot
        fi
    fi
done
