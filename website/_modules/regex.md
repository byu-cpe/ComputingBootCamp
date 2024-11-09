---
layout: page
toc: true
title: Unix Tools and Regex
slug: regex
type: development
order: 15
---

## Why Regex?

Regular expressions have a long history of use in Unix and Linux tools.
Examples include vi(m), sed, AWK, perl, ed, grep, sam, and lex.
Regex provides a concise notation for pattern-matching on strings,
and allow for efficient manipulation and identification of textual data.

## Intro to Regex

There's a lot of interesting theory behind the "regular" part,
but we're just going to go over how they work.  For more
information about the theory, see the wikipedia page:
<https://en.wikipedia.org/wiki/Regular_expression>.

There are different variants of syntax for regular expressions.  This is
a commonly used syntax, called POSIX Extended Regular Expressions.

+ `hello`: The simplest regular expression is a string, which matches that exact string.
+ `.ello`: You can use a `.` character to represent any single character.
+ `helloo*`: You can use a `*` character to represent 0 or more repetitions of a character.
+ `.*hello.*`: Those can be combined to represent an arbitrary string of characters.
+ `[hy]ello`: The square braces represent a character set, matching any one of the characters inside.
+ `[^bz]ello`: Adding the caret inverts the set, matching any character not in the braces.
+ `[a-z]ello`: This matches any single character in the range from `a` to `z`, followed by `ello`.
+ `[a-zA-Z]ello`: This matches any alphabetical character, followed by `ello`.
+ `hello|world`: This matches either `hello` or `world`.
+ `(he|ye)llow?`: This matches one of `hello`, `yello`, `hellow`, or `yellow`.
+ `hello+`: This matches `hello` with at least one `o`.
+ `^hello`: This matches `hello` at the beginning of the search.
+ `hello$`: This matches `hello` at the end of the search.

Note that by default, grep (among others) is in basic regex mode.
This means there is no `?`, `|`, or `+` operator, and you have to precede
`(` and `)` by a backslash.  To enable these features you can use `egrep`,
which is deprecated, or `grep -E`.

## grep

`grep` comes from the ed search command, `g/re/p`, which means global
regex print.  You almost always want `grep -E` unless your search
is simple.  It expects data on stdin, and searches through a line at
a time, printing out each line that matches the regex provided on the
command line.  Some helpful flags include `-F` (matching a literal string,
useful to prevent lots of backslashes), `-v` (print all lines that don't
match), `-o` (only print exact match instead of the whole line), and
`-n` (prefix match with its line number).  There are others, but this
is enough to get started.  Read `man grep` for more.

## sed

`sed` is based off of `ed`, but built for working over pipes instead of
seekable files.  The most common command is `sed 's/regex/repl/'`, which
replaces the first match of `regex` in every line with `repl`.  To do all
matches per line, you add the `g` command like so: `sed 's/regex/repl/g'`.

Note that you can implement `grep` in sed.  `grep 're'` is the same as
`sed -n '/re/p'`, and `grep -v 're'` is `sed '/re/d'`.  Also `head -n15`
is `sed 15q`.  `sed` implements a full editor language, but I don't
necessarily recommend using it for everything, as it can be kind of
cryptic and difficult to debug.

Also, `sed` by default does not edit files in place.  GNU sed has the
`-i` flag if you want that, or the more general option is a utility
called `sponge` from the moreutils package, which reads all of stdin
before writing to the file on the command line.  You can also do
`fancy command on dest >tempfile; mv tempfile dest`.  These options are
more general than the `sed`-specific flag.

For a more comprehensive overview, see:
<https://www.grymoire.com/Unix/Sed.html> or `man sed`.

## AWK

AWK is named after its three authors, Alfred Aho, Peter Weinberger,
and Brian Kernighan.  AWK is a language for text processing, and is
much more readable than `sed`.  It is excellent at generating reports
and filtering data.

AWK programs consist of a series of expressions, all having the form
`condition { actions }`.  For every line satisfying `condition`, `actions`
are executed.  Conditions are often `/re/` or `/re1/,/re2/` (starting
line matches `re1`, ending line matches `re2`, inclusive), but they
can also be arbitrary logical conditions on variables.  Actions include
`print`, where each argument is separated by the output field separator
(OFS, tab by default), or variable assignments and calculations.

The real strength of AWK comes from the automatic field parsing.
`$0` represents the whole line, while `$n` represents the nth field.
Fields are broken up according to the FS variable, which can be set to
any sequence of characters, but defaults to whitespace.  Some other
variables include `NR` (Number of Records, usually the current line
number), `FILENAME`, and `NF` (Number of Fields).

AWK also has support for dictionaries with string keys, called associative
arrays, and floating point numbers.  Conversion between strings and
floats is automatic, and there are several functions for floating point
calculations.

An example of an awk script to calculate the mode of the second column
of a group of numbers:

```
#!/bin/awk -f
{stats[$2]++}
END {
	max["k"] = ""
	max["v"] = 0
	for (s in stats) {
		if (stats[s] > max["v"]) {
			max["k"] = s
			max["v"] = stats[s]
		}
	}
	print max["k"]
}
```

In fact, the above script works no matter what the second column contains,
it will always calculate the mode.  The END condition runs after all
the input is consumed.  There is an analagous BEGIN condition, that runs
before the input.

A couple of things to note about AWK:
+ If you have multiple condition/action pairs, each one is checked independently, so you could have multiple sets of actions fire on a single line of input.
+ No condition is the same as true, that is, it runs for every line.
+ Separating 2 strings with a space results in concatenation.  This is often used to create keys and values for an associative array.

This is intended to give a basic taste of awk, enough to
make it readable.  For a more comprehensive overview, see
<https://www.grymoire.com/Unix/Awk.html>, or `man awk`.

## Conclusion

Regular expressions are used throughout the unix ecosystem for matching
pieces of text.  Knowing them enables you to use several fundamental
tools.  If you use vim, you can search with regex with `/regex`.  Also,
the heritage from ed is definitely visible in vi and vim, in that you
can type an arbitrary ed command in vim by prefixing it with a colon
like so: `:g/regex/p`.  The gist of it all is that the unix tools were
all designed to work together, and learning the basic principles pays
dividends for the rest of the unix experience.

## Links

+ A good set of tutorials on all these tools, and more (make, sh, find, permissions, etc.): <https://www.grymoire.com/Unix/>
+ An intro to the ideas underlying vim/vi: <https://stackoverflow.com/a/1220118>
+ The package with `sponge`: <https://joeyh.name/code/moreutils/>
