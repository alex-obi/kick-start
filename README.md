# Google Kick Start Solutions

A collection of my solutions for some of the [Google Kick Start](https://codingcompetitions.withgoogle.com/kickstart) problems.
Some solutions are inspired by the Analysis tab provided by Google.
While most code files do work with the Sample inputs, there is no guarantee that they will provide a 100% accurate or time efficient solution.


## Run

One can use the bash scripts from the root directory for testing as

```
$ bash runcc.sh [FILE] [INPUT]
$ bash runpy.sh [FILE] [INPUT]
```
to compile and/or execute C++ and Python files locally.
`[FILE]` is the filename of code (without extension) and `[INPUT]` defines the file with input content.
At runtime, the programs are fed with the entries defined in `[INPUT]`.
Print the output directly into a file:
```
$ bash runcc.sh [FILE] [INPUT] > output.out
$ bash runpy.sh [FILE] [INPUT] > output.out
```

----
