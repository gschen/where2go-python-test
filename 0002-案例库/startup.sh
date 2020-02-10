#!/bin/bash
git pull

CMD_EXPORT=""

case "`uname`" in
Darwin) CMD_EXPORT=""$CMD_EXPORT"claat-darwin-amd64"
;;
Linux) CMD_EXPORT=""$CMD_EXPORT"claat-linux-amd64"
;;
esac

CMD_EXPORT=""$CMD_EXPORT" export *.md"
echo $CMD_EXPORT

cd codelabs
$CMD_EXPORT

cd ..
gulp serve --codelabs-dir=codelabs
