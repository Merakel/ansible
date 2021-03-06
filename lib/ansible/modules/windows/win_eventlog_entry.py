#!/usr/bin/python

# (c) 2017, Andrew Saraceni <andrew.saraceni@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: win_eventlog_entry
version_added: "2.4"
short_description: Write entries to Windows event logs
description:
     - Write log entries to a given event log from a specified source.
options:
  log:
    description:
      - Name of the event log to write an entry to.
    required: true
  source:
    description:
      - Name of the log source to indicate where the entry is from.
    required: true
  event_id:
    description:
      - The numeric event identifier for the entry.
      - Value must be between 0 and 65535.
    required: true
  message:
    description:
      - The message for the given log entry.
    required: true
  entry_type:
    description:
      - Indicates the entry being written to the log is of a specific type.
    choices:
      - Error
      - FailureAudit
      - Information
      - SuccessAudit
      - Warning
  category:
    description:
      - A numeric task category associated with the category message file for the log source.
  raw_data:
    description:
      - Binary data associated with the log entry.
      - Value must be a comma-separated array of 8-bit unsigned integers (0 to 255).
notes:
    - This module will always report a change when writing an event entry.
author:
    - Andrew Saraceni (@andrewsaraceni)
'''

EXAMPLES = r'''
- name: Write an entry to a Windows event log
  win_eventlog_entry:
    log: MyNewLog
    source: NewLogSource1
    event_id: 1234
    message: This is a test log entry.

- name: Write another entry to a different Windows event log
  win_eventlog_entry:
    log: AnotherLog
    source: MyAppSource
    event_id: 5000
    message: An error has occurred.
    entry_type: Error
    category: 5
    raw_data: 10,20
'''

RETURN = r'''
# Default return values
'''
