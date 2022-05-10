#!/bin/sh
mkdir -p "build/ddlc/game/mpMod"
find -not \( -path "./build" -prune \) -iname "*.rpy" -exec cp --parents \{\} "build/ddlc/game/mpMod" \;
build/renpy/renpy.sh "build/ddlc" compile 2>&1 | tee build/compile.log | perl -ne 'print if (/^game\/mpMod[^\s]*: \w*Warning/ || !/^game\//)' | sed 's/game\/mpMod\///g'
if grep -Eq '^.*Error:.*$|^File ".*", line .*:.*$' build/compile.log; then exit 1; fi
find "build/ddlc/game/mpMod" -type f -not -iname "*.rpyc" -delete
mkdir -p "build/out/game/Submods"
mv "build/ddlc/game/mpMod" "build/out/game/Submods/$(perl -ne 'printf $1 if /name="([^"]*)"/' "mod/00_header.rpy")"
