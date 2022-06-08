# Reading Python Error Messages

## Learning Goals

- Read the different parts of an error message
- Identify common types of errors

## Introduction

In this lab, you'll be reading error messages from tests. This lab is designed
so that both running the files _and_ running the test suite via the `pytest`
command will show the error messages for you to decode. Moving forward though,
you'll be reading error messages mainly through running the test suite.

## Reading Error Messages

Let's start by running some of the Python code in the `lib` folder to produce an
error message. Run this in your terminal:

```console
$ python lib/a_name_error.py
```

Error messages have 3 parts:

```console
File "lib/a_name_error.py",
line 3, in <module>
    print(hello_world)
NameError: name 'hello_world' is not defined
```

1. The location of the error, the "where":

   ```console
   "lib/a_name_error.py", line 3, in <module>:
   ```

   - `"lib/a_name_error.py"` is the file the error occurred in.
   - `line 3` is the line of code with the error.
   - `<module>` is the scope of the error.

2. The type of error, the "who":

   ```console
   NameError:
   ```

   This is a [Python Error Type](https://docs.python.org/3/tutorial/errors.html).

3. The description, the "why":

   ```console
   name 'hello_world' is not defined
   ```

   The interpreter does the best job it can to tell you what it thinks went wrong.

You've solved games of _Clue_ with less information. This is one of the best
parts of programming: debugging and fixing errors. It's like you're a detective
solving a crime. The only bad thing is that more often than not, you're also the
criminal that caused the error in the first place.

Errors are clues, and reading them is the interpreter telling you what to do to
fix the program and move on.

## Three Common Error Types

### Syntax Errors

Syntax errors are pretty self-explanatory: they're the result of incorrect
syntax. Thankfully, they're usually followed by a guess about the location of
the error. For instance:

```py
2 * #
```

Will result in:

```console
File "<stdin>", line 1
    2*#
      ^
SyntaxError: invalid syntax
```

Here, Python is saying that on line 1, there is a missing number (every `*`
operator must be preceded and followed by a number or variable with a numerical
value). Always read the full details of syntax errors and look for line numbers,
which usually appear at the beginning of the error message.

### Logic Errors

Logic errors are often difficult to find because they are not perceived as
errors by the Python interpreter itself. To find a logic error, a programmer
will often need to comb through their code line by line. Debugging tools such
as `pdb` (which we will cover later on in Phase 3) are very helpful for
locating and fixing logic errors.

```py
count = 1
while count < 100:
    print("%i" % count)
```

Will produce the following output:

```console
1
1
1
1
1
1
1
...
```

The programmer here forgot to increase the count during each iteration of the
`while` loop. This is perfectly valid Python code, so the interpreter will not
throw an error, but the loop will continue forever until it is manually
stopped by the user. (The easiest way to do this in the terminal is `ctrl + c`)

### Exceptions

A `DivisionError` is caused when a given number is divided by 0.

## Instructions

To get started, run `learn test --f-f` to run the first test in the test suite.
Use the error messages to guide your work:

- Read the errors. Scroll through the entire output to get a sense of what the
  failures are trying to tell you. What does the error mean? How can we fix it?

- Each error prints out a **stack trace**, which points to where the code failed
  and attempts to follow it _up the stack_ — that is, through the bits of
  code that ran leading up to the failure. You can use these stack traces to
  pinpoint which line(s) of code need your attention.

- These stack traces can also point you to which files you should run to get a
  better sense of the errors.

Fix the errors in each of the files in `lib/`. Then confirm the fix by running
`learn test` again.
