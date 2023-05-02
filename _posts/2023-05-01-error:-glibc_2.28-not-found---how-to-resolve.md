---
layout: post
title: "Error: GLIBC_2.28 Not Found - How to Resolve"
tags: ['node.js', 'ubuntu']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

The **Error: GLIBC_2.28 Not Found** is an error that occurs when a program is compiled or executed on a system that does not have the required version of the GNU C Library (glibc) installed. This error can be caused by a variety of factors, including incompatibility between the program and the installed version of glibc, or by missing dependencies. In this article, we will discuss how to identify and resolve this error.

## Common Mistakes

There are several common mistakes that can lead to the Error: GLIBC_2.28 Not Found error. The most common of these is attempting to compile or execute a program on a system that does not have the required version of glibc installed. Another common mistake is attempting to use a program that requires a newer version of glibc than is installed on the system. Finally, the error can also be caused by missing dependencies or incompatibility between the program and the installed version of glibc.

## How to Resolve the Error

The first step in resolving the Error: GLIBC_2.28 Not Found error is to identify the version of glibc installed on the system. This can be done by running the `ldd` command, which will display the versions of glibc installed on the system. Once the version of glibc installed on the system is identified, the program can be checked for compatibility with the installed version. If the program is not compatible with the installed version of glibc, the program must be recompiled using the correct version of glibc.

If the program is compatible with the installed version of glibc, but the Error: GLIBC_2.28 Not Found error is still occurring, the next step is to check for missing dependencies. This can be done by running the `ldd` command again and checking the output for any missing libraries. If any missing libraries are identified, they must be installed before the program can be compiled and executed.

Finally, if the program is compatible with the installed version of glibc and all dependencies are present, the Error: GLIBC_2.28 Not Found error can be resolved by running the `ldconfig` command. This command will update the library paths on the system, allowing the program to be compiled and executed successfully.

## Examples

To demonstrate the steps outlined above, we will use a simple example program written in C. The program is designed to print the message "Hello, World!" to the console.

```c
#include <stdio.h>

int main(void) {
    printf("Hello, World!\n");
    return 0;
}
```

In order to compile and execute this program, the GNU C Library (glibc) must be installed on the system. The version of glibc installed on the system can be identified by running the `ldd` command, as shown below.

```
$ ldd --version
ldd (GNU libc) 2.27
```

In this example, the installed version of glibc is 2.27. To compile the program, we must use the same version of glibc. We can do this by running the `gcc` command with the `-m32` flag, as shown below.

```
$ gcc -m32 -o hello hello.c
```

This will compile the program using the 32-bit version of glibc 2.27. We can then execute the program by running the `./hello` command, which should produce the following output.

```
Hello, World!
```

If the program is not compatible with the installed version of glibc, or if any dependencies are missing, the Error: GLIBC_2.28 Not Found error will be displayed. In this case, the steps outlined above must be followed to resolve the error.

If you are a developer, you may have encountered this error while trying to run an application or while debugging. This error is caused by a missing library, specifically the `GLIBC_2.28` library. This library is necessary for applications to run properly, and if it is missing, the application will not run. In this blog post, we'll discuss what this error is, why it happens, and how to resolve it.

## What is GLIBC_2.28?

GLIBC_2.28 is a library that is part of the GNU C Library (Glibc) package, a collection of open source software libraries which provide the core functionality of the GNU operating system. This library is responsible for providing the basic functions of the system, such as memory allocation, process control, and threading. It is also responsible for providing the interface to the operating system's kernel, which allows applications to interact with the system.

## Why Does This Error Occur?

This error occurs when the `GLIBC_2.28` library is not installed on your system. This is usually because the version of the library that is installed is out of date, or because the library has not been installed at all.

## How to Resolve the Error

In order to resolve this error, you will need to install the correct version of the `GLIBC_2.28` library. This can be done in a few different ways, depending on your operating system.

### On Linux

If you are running a Linux-based operating system, you can use the `apt-get` command to install the library. First, open a terminal and run the following command:

```
sudo apt-get install libc6-dev
```

This will install the `GLIBC_2.28` library and all of its dependencies. Once the installation is complete, you can try running your application again.

### On macOS

If you are running a macOS-based operating system, you can use the `brew` command to install the library. First, open a terminal and run the following command:

```
brew install glibc
```

This will install the `GLIBC_2.28` library and all of its dependencies. Once the installation is complete, you can try running your application again.

### On Windows

If you are running a Windows-based operating system, you can use the `chocolatey` command to install the library. First, open a terminal and run the following command:

```
choco install glibc
```

This will install the `GLIBC_2.28` library and all of its dependencies. Once the installation is complete, you can try running your application again.

## Conclusion

In this blog post, we discussed the `GLIBC_2.28` error and how to resolve it. We explained what the library is, why the error occurs, and how to install it on Linux, macOS, and Windows. We hope this post has been helpful and that it has given you the information you need to resolve this error.
## Recommended sites

- [How to Resolve GLIBC_2.28 Not Found Error](https://www.2daygeek.com/glibc_2-28-not-found-error-solution/)
- [How to Fix GLIBC_2.28 Not Found Error](https://itsfoss.com/glibc_2-28-not-found-error/)
- [GLIBC_2.28 Not Found Error Solution](https://www.tecmint.com/glibc_2-28-not-found-error-solution/)
- [How to Fix GLIBC_2.28 Not Found Error on Linux](https://www.linuxbabe.com/linux-server/fix-glibc_2-28-not-found-error-linux)