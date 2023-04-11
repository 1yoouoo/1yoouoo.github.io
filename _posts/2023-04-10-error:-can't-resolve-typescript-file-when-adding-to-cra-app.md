---
layout: post
title: "Error: Can't Resolve Typescript File When Adding to CRA App"
tags: ['reactjs', 'typescript', 'webpack', 'create-react-app']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

Are you having trouble adding a TypeScript file to your Create React App (CRA) project? If so, you’re probably getting an error that says “Cannot resolve file”. This can be a frustrating issue to deal with, but don’t worry! In this article, we’ll go over the steps to troubleshoot this error and get your project back up and running.

## Common Mistakes

When adding a TypeScript file to your CRA project, there are a few common mistakes that can lead to the “Cannot resolve file” error. The two most common mistakes are:

1. Not adding the `.ts` extension to the file name.
2. Not including the `@types/` package in your `package.json` file.

## Adding the `.ts` Extension

The first step in troubleshooting this error is to make sure you’ve added the `.ts` extension to the end of your file name. For example, if you’re trying to add a file named `MyComponent`, the file name should be `MyComponent.ts`.

If you’re still getting the “Cannot resolve file” error after adding the `.ts` extension, the next step is to make sure you’ve included the `@types/` package in your `package.json` file.

## Including the `@types/` Package

The `@types/` package is a collection of type definitions for popular JavaScript libraries. It’s necessary to include this package in your `package.json` file in order for TypeScript to properly recognize the types used in your project.

To include the `@types/` package in your `package.json` file, open the file and add the following line:

```json
"@types/": "^1.0.0"
```

Once you’ve added the line, save the file and then run `npm install` to install the `@types/` package.

## Conclusion

If you’re getting the “Cannot resolve file” error when adding a TypeScript file to your Create React App (CRA) project, the two most common mistakes are not adding the `.ts` extension to the file name and not including the `@types/` package in your `package.json` file. To troubleshoot this error, make sure you’ve added the `.ts` extension to the file name and included the `@types/` package in your `package.json` file.

If you are a React developer, chances are you have encountered the dreaded error: `Can't resolve './filename.tsx' in './path/to/project/src'`. This error can be incredibly frustrating, as it often pops up when you are trying to add a new Typescript file to an existing Create React App project.

The good news is that this error is easy to fix. All you need to do is make sure that you have the correct configuration settings in your `tsconfig.json` file.

## What is `tsconfig.json`?

`tsconfig.json` is a file that contains configuration settings for the TypeScript compiler. It tells the compiler where to look for TypeScript files and how to compile them.

## How to Fix the `Can't Resolve` Error

The first step is to make sure that you have the correct configuration settings in your `tsconfig.json` file. Here is an example of what a `tsconfig.json` file might look like:

```json
{
  "compilerOptions": {
    "target": "es6",
    "module": "commonjs",
    "sourceMap": true,
    "outDir": "build",
    "baseUrl": "./src",
    "paths": {
      "*": ["*", "src/*"]
    }
  },
  "include": ["src/**/*"]
}
```

The most important setting is the `baseUrl` setting. This setting tells the TypeScript compiler where to look for TypeScript files. In this example, the `baseUrl` is set to `./src`, which means that the compiler will look in the `src` folder for TypeScript files.

The other important setting is the `paths` setting. This setting tells the compiler where to look for TypeScript files that are imported by other TypeScript files. In this example, the `paths` setting is set to `"*": ["*", "src/*"]`, which means that the compiler will look for TypeScript files in the `src` folder and any of its subfolders.

Once you have the correct configuration settings in your `tsconfig.json` file, you can then add the new TypeScript file to your project. Make sure that the file is located in the `src` folder or one of its subfolders.

If you are still having trouble getting the TypeScript file to compile, you can try using the `--noEmit` flag when running the TypeScript compiler. This flag will tell the compiler to only type-check the file, but not actually compile it. This can be helpful if you are having issues with the TypeScript compiler not recognizing the new TypeScript file.

## Summary

The `Can't resolve './filename.tsx' in './path/to/project/src'` error is a common error that can occur when adding a new TypeScript file to a Create React App project. The solution is to make sure that you have the correct configuration settings in your `tsconfig.json` file. The most important settings are the `baseUrl` and `paths` settings, which tell the TypeScript compiler where to look for TypeScript files. Once you have the correct configuration settings, you can then add the new TypeScript file to your project. If you are still having trouble getting the TypeScript file to compile, you can try using the `--noEmit` flag when running the TypeScript compiler.
## Recommended sites

- [Error: Can't Resolve Typescript File When Adding to CRA App](https://stackoverflow.com/questions/56394545/error-cant-resolve-typescript-file-when-adding-to-cra-app)
- [Create React App with TypeScript](https://create-react-app.dev/docs/adding-typescript/)
- [Adding TypeScript to a React Project](https://www.pluralsight.com/guides/adding-typescript-to-a-react-project)
- [Adding TypeScript to a React App](https://www.freecodecamp.org/news/adding-typescript-to-a-react-app/)