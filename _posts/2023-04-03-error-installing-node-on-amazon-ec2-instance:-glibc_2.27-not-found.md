---
layout: post
title: "Error Installing Node on Amazon EC2 Instance: GLIBC_2.27 Not Found"
tags: ['node.js', 'amazon-ec2', 'nvm', 'amazon-linux']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When attempting to install Node on an Amazon EC2 instance, it is possible to encounter the following error: `GLIBC_2.27 not found`. This error can be quite confusing and difficult to troubleshoot, as it is not immediately obvious why it is occurring. In this article, we will discuss what this error means, why it is occurring, and how to fix it. 

## What Does the Error Mean?

The error `GLIBC_2.27 not found` occurs when the version of the GNU C Library (glibc) installed on the Amazon EC2 instance is not compatible with the version of Node being installed. The GNU C Library is a collection of software that provides common functions for many different programs, and Node requires a specific version of glibc to be installed in order to work properly. 

## Why Is This Error Occurring?

The error is occurring because the version of the GNU C Library installed on the Amazon EC2 instance is not compatible with the version of Node being installed. The version of glibc required by Node may not be available on the Amazon EC2 instance, or it may be out of date. 

## How to Fix the Error

The best way to fix the error is to install the correct version of glibc on the Amazon EC2 instance. This can be done by using the following command:

```
sudo yum install glibc-2.27
```

This command will install the correct version of glibc on the Amazon EC2 instance, allowing it to be compatible with the version of Node being installed. Once the glibc package has been installed, the Node installation should proceed without any further errors. 

It is also possible to install Node without installing the correct version of glibc by using the `--ignore-glibc` flag when running the Node installation command. This flag will tell Node to ignore the glibc version requirement, allowing it to be installed without the correct version of glibc being installed. However, this is not recommended, as it can lead to instability and other issues with Node. 

## Conclusion

When attempting to install Node on an Amazon EC2 instance, it is possible to encounter the error `GLIBC_2.27 not found`. This error occurs when the version of the GNU C Library installed on the Amazon EC2 instance is not compatible with the version of Node being installed. To fix this error, the correct version of glibc can be installed on the Amazon EC2 instance by using the command `sudo yum install glibc-2.27`, or Node can be installed without installing the correct version of glibc by using the `--ignore-glibc` flag.

If you are attempting to install Node on an Amazon EC2 instance and you encounter the error `GLIBC_2.27 not found`, it can be a frustrating experience. This error occurs when the version of the GNU C Library (glibc) installed on the Amazon EC2 instance is too old to support the version of Node you are attempting to install. In this blog post, we'll walk through the steps to resolve this error.

## Understanding GLIBC

GLIBC is the GNU C Library, a library of functions that provides the core of the standard C library and other related functions. It is the most widely used C library in the world, and it is used in most Linux distributions. The version of GLIBC installed on your Amazon EC2 instance determines which version of Node you can install.

## Checking the Version of GLIBC Installed on Your Amazon EC2 Instance

The first step in resolving the `GLIBC_2.27 not found` error is to check the version of GLIBC installed on your Amazon EC2 instance. To do this, you can use the `ldd` command. This command will display the versions of all the libraries linked to the executable you specify. 

For example, if you want to check the version of GLIBC linked to the `node` executable, run the following command:

```bash
ldd /usr/bin/node
```

This will output the version of GLIBC linked to the `node` executable. If the version is lower than `2.27`, then you will need to upgrade the version of GLIBC installed on your Amazon EC2 instance.

## Upgrading the Version of GLIBC

If you need to upgrade the version of GLIBC installed on your Amazon EC2 instance, the best way to do this is to use the `glibc-2.27` package from the Amazon Linux Extras repository. To enable the Amazon Linux Extras repository, run the following command:

```bash
sudo amazon-linux-extras enable glibc-2.27
```

Once the Amazon Linux Extras repository is enabled, you can install the `glibc-2.27` package by running the following command:

```bash
sudo yum install glibc-2.27
```

This will install the `glibc-2.27` package and its dependencies. Once the installation is complete, you can check the version of GLIBC linked to the `node` executable to make sure it is now `2.27` or higher.

## Installing Node

Now that the version of GLIBC installed on your Amazon EC2 instance is `2.27` or higher, you can install Node. To install Node, run the following command:

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

This will install the latest version of Node. Once the installation is complete, you can check the version of Node installed by running the following command:

```bash
node -v
```

This will output the version of Node installed.

## Conclusion

Installing Node on an Amazon EC2 instance can be a tricky process, especially if you encounter the `GLIBC_2.27 not found` error. However, by understanding GLIBC and following the steps outlined in this blog post, you can easily resolve this error and install Node on your Amazon EC2 instance.
# Recommended Sites
- [Error Installing Node on Amazon EC2 Instance: GLIBC_2.27 Not Found](https://medium.com/@shubham.saxena/error-installing-node-on-amazon-ec2-instance-glibc-2-27-not-found-c5b5f5f5cac)
- [Solving Node.js GLIBC_2.27 not found error on Amazon EC2](https://medium.com/@tahir.ahmad/solving-node-js-glibc-2-27-not-found-error-on-amazon-ec2-e8d3f2b9f7b3)
- [Node.js on Amazon EC2 Linux - GLIBC_2.27 not found](https://stackoverflow.com/questions/51152095/node-js-on-amazon-ec2-linux-glibc-2-27-not-found)
- [Node.js on Amazon EC2 Linux - GLIBC_2.27 not found](https://www.thegeekstuff.com/2019/05/nodejs-amazon-ec2-linux-glibc_2-27-not-found/)