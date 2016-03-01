#!/usr/bin/python

import os

# Where the SuperDuper! log files are.
logdir = (os.environ["HOME"] +
          "/Library/Application Support/" +
          "SuperDuper!/Scheduled Copies/" +
          "Smart Update Clone from Titan HD.sdsp/Logs/")

def sdinfo(s):
  "Return just the timestamp and process information from a SuperDuper line."
  parts = s.split('|')
  ratespot = parts[3].find("at an effective transfer rate")
  if ratespot > -1:
    parts[3] = parts[3][:ratespot]
  detailspot = parts[3].find("(")
  if detailspot > -1:
    parts[3] = parts[3][:detailspot]
  return "%s: %s" % (parts[1].strip(), parts[3].strip(' \\\n'))

# Get the last log file.
logfiles = [x for x in os.listdir(logdir) if x[-5:] == 'sdlog']
logfiles.sort()
lastlog = logdir + logfiles[-1]

with open(lastlog) as f:
  for line in f:
    for signal in ["Started on", "PHASE:", "Copied", "Cloned", "Copy complete"]:
        if signal in line:
          print sdinfo(line)
