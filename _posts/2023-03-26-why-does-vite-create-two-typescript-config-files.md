---
layout: post
title: Why Does Vite Create Two TypeScript Config Files?
tags: ['javascript', 'typescript', 'tsconfig', 'vite']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When using the Vite build tool, developers may encounter an issue where two TypeScript config files are created. This can be confusing and lead to errors in the build process. To understand why Vite creates two TypeScript config files, it is important to understand how Vite works.

Vite is a modern build tool that is designed to make development faster and more efficient. It allows developers to quickly and easily create a development environment and build a project. It is based on the JavaScript and TypeScript programming languages, and uses a configuration file written in TypeScript to define the project's configuration.

When a project is created with Vite, the configuration file is automatically generated. This file contains the settings for the project, such as the project name, the source code directory, and the build settings. The configuration file is written in TypeScript and is called vite.config.ts.

However, when a project is built with Vite, an additional TypeScript config file is created. This file is called tsconfig.json and contains the settings for the TypeScript compiler. This file is necessary for the TypeScript compiler to understand how to compile the project.

The main reason why Vite creates two TypeScript config files is because the vite.config.ts file is used to configure the Vite build tool, while the tsconfig.json file is used to configure the TypeScript compiler. This is necessary because the TypeScript compiler needs to understand the project's configuration in order to properly compile the project.

One common mistake that developers make is to modify the vite.config.ts file instead of the tsconfig.json file. This can lead to errors in the build process, as the TypeScript compiler will not understand the project's configuration if it is not properly configured in the tsconfig.json file.

Another common mistake is to modify the tsconfig.json file without understanding the project's configuration. This can lead to errors in the build process, as the TypeScript compiler may not understand the project's configuration if it is not properly configured.

It is important to understand why Vite creates two TypeScript config files in order to properly configure the project and avoid errors in the build process. By understanding the differences between the two files and how they are used, developers can ensure that their project is properly configured and avoid errors in the build process.
Typescript is a language that is widely used in the software development world. It is a superset of JavaScript that allows developers to write code that is more structured and maintainable.

Vite is a modern web development build tool that uses TypeScript as its primary language. It is a zero-configuration build tool that makes it easier for developers to get up and running quickly.

One of the most common issues that developers face when using Vite is that it creates two TypeScript config files: tsconfig.json and vite.config.ts. This can be confusing for developers who are used to working with traditional build tools like webpack and gulp. In this article, we will discuss why Vite creates two TypeScript config files and how to use them.

## What is tsconfig.json?

The tsconfig.json file is a configuration file for the TypeScript compiler. It contains settings that tell the compiler how to compile your TypeScript code. This includes things like which files to include, which language features to enable, and which output format to use.

## What is vite.config.ts?

The vite.config.ts file is a configuration file for the Vite build tool. It contains settings that tell Vite how to build your project. This includes things like which files to include, which plugins to use, and which output format to use.

## How Do These Two Files Work Together?

The tsconfig.json file is used by the TypeScript compiler to compile your TypeScript code. The vite.config.ts file is used by Vite to build your project. The two files work together to create a complete build process.

The tsconfig.json file is used to configure the TypeScript compiler. It tells the compiler which files to include, which language features to enable, and which output format to use.

The vite.config.ts file is used to configure Vite. It tells Vite which files to include, which plugins to use, and which output format to use.

## How Do I Configure These Two Files?

The tsconfig.json file is configured using standard TypeScript compiler options. You can find a full list of options in the TypeScript documentation.

The vite.config.ts file is configured using the Vite configuration API. You can find a full list of options in the Vite documentation.

## Conclusion

Vite creates two TypeScript config files, tsconfig.json and vite.config.ts, to allow developers to configure both the TypeScript compiler and Vite. The tsconfig.json file is used to configure the TypeScript compiler and the vite.config.ts file is used to configure Vite. Both files must be configured correctly in order for Vite to build your project correctly.