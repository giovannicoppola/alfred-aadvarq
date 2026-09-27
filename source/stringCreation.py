#!/usr/bin/python3

## STRING CREATION
# giovanni
# Build an mdfind metadata query from the typed tag expression.
# AND / OR / NOT (uppercase) are operators; everything else is a tag name.

import sys


def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)


def comparison(tag):
    # double quotes would terminate the query string: strip them
    tag = tag.replace('"', '')
    return f'kMDItemUserTags == "{tag}"'


def build_query(words):
    parts = []
    last_was_comparison = False
    for word in words:
        if word == 'AND':
            if last_was_comparison:
                parts.append('&&')
                last_was_comparison = False
        elif word == 'OR':
            if last_was_comparison:
                parts.append('||')
                last_was_comparison = False
        elif word == 'NOT':
            # a leading NOT would match nearly every file on the disk
            if not parts:
                return ""
            if last_was_comparison:
                parts.append('&&')
            parts.append('!')
            last_was_comparison = False
        else:
            # two tags in a row imply AND
            if last_was_comparison:
                parts.append('&&')
            parts.append(comparison(word))
            last_was_comparison = True
    # drop a trailing operator ("red AND" while still typing)
    while parts and parts[-1] in ('&&', '||', '!'):
        parts.pop()
    return " ".join(parts)


def main():
    myString = sys.argv[1] if len(sys.argv) > 1 else ""
    myOutput = build_query(myString.split())
    log(myOutput)
    print(myOutput)


if __name__ == "__main__":
    main()
