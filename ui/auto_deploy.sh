#!/bin/bash

echo "node: `node -v`"
echo "npm: `npm -v`"

# change directory according your physical truth
gitDir="/opt/repos/cooperate_web"

echo -e "\033[32m [AUTO SYNC] sync demo start \033[0m"
cd $gitDir

echo -e "\033[32m [AUTO SYNC] git pull...  \033[0m"
git pull

echo -e "\033[32m [AUTO SYNC] npm install... \033[0m"
npm install

echo -e "\033[32m [AUTO SYNC] npm run build... \033[0m"
npm run build

echo -e "\033[32m [AUTO SYNC] sync finish \033[0m"
