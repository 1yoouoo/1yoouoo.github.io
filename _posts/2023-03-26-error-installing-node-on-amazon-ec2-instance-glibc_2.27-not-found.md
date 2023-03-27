---
layout: post
title: "Error Installing Node on Amazon EC2 Instance: GLIBC_2.27 Not Found"
tags: ['node.js', 'amazon-ec2', 'nvm', 'amazon-linux']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

If you're trying to install Node on an Amazon EC2 instance and you're getting the error "GLIBC_2.27 Not Found", then you're not alone. This is a relatively common issue, and can be caused by a few different things. In this article, we'll explore some of the most common reasons for this error, and provide some tips for resolving it.

## What is GLIBC_2.27?

GLIBC_2.27 is the GNU C Library version 2.27. It is a library of functions and constants used by the GNU C Compiler (GCC) to build programs. The GNU C Library is an essential part of the GNU operating system, and is used by many programs and applications.

## What Causes the "GLIBC_2.27 Not Found" Error?

There are a few common causes of this error. The most common is that the version of the GNU C Library installed on the system is out of date. This can happen if an older version of the library is installed, or if the system is running an outdated version of the operating system.

Another common cause is that the system is missing the necessary dependencies for the library. This can happen if the system is missing the necessary development packages, or if the packages are out of date.

## How to Resolve the "GLIBC_2.27 Not Found" Error

The first step in resolving this error is to check the version of the GNU C Library installed on the system. To do this, run the following command:

```bash
$ ldd --version
```

This will output the version of the GNU C Library installed on the system. If the version is out of date, then you'll need to update it.

If the version is up to date, then the next step is to check for any missing dependencies. To do this, run the following command:

```bash
$ ldd --list-needed
```

This will output a list of the libraries that the system is missing. If any of the libraries are missing, then you'll need to install them.

Once you've installed any missing libraries, you should be able to install Node without any further issues.

## Conclusion

The "GLIBC_2.27 Not Found" error can be caused by a few different things, including an outdated version of the GNU C Library, or missing dependencies. To resolve this error, check the version of the library installed on the system, and install any missing dependencies. Once this is done, you should be able to install Node without any further issues.

If you are trying to install Node on an Amazon EC2 instance and you get an error that reads `GLIBC_2.27 not found`, you are probably running into a common issue related to the version of GLIBC on your instance. This issue can be resolved by making sure your instance is running the correct version of GLIBC.

## What is GLIBC?

GLIBC (GNU C Library) is a collection of low-level system libraries that provide the basic building blocks for many other software components. It is used by many applications, including Node, and is a critical component of the Linux operating system.

## What is the Issue?

The issue occurs when the version of GLIBC on your Amazon EC2 instance is too old to support the version of Node you are trying to install. In order to install Node, the version of GLIBC must be at least `2.27`.

## How to Resolve the Issue

To resolve the issue, you must update the version of GLIBC on your Amazon EC2 instance. To do this, you will need to SSH into your instance and run the following commands:

```bash
# Update the package manager
sudo yum update

# Install the latest version of GLIBC
sudo yum install glibc-2.27

# Restart the instance
sudo reboot
```

Once the instance has restarted, you can try installing Node again and the issue should be resolved.

## Conclusion

If you are trying to install Node on an Amazon EC2 instance and you get an error that reads `GLIBC_2.27 not found`, you can resolve the issue by updating the version of GLIBC on your instance. To do this, you will need to SSH into your instance and run the commands outlined above. Once the instance has restarted, you can try installing Node again and the issue should be resolved.