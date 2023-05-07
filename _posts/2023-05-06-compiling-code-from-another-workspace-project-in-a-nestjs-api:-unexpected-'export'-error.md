---
layout: post
title: "Compiling Code from Another Workspace Project in a NestJS API: Unexpected 'export' Error"
tags: ['typescript', 'nestjs', 'workspace', 'monorepo', 'yarn-workspaces']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When attempting to compile code from another workspace project in a NestJS API, developers may encounter an unexpected 'export' error. This error can be caused by a number of issues, including syntax errors, incorrect imports, or missing packages. In this article, we'll discuss the common mistakes that can lead to this error, and provide some examples of how to fix them.

## Common Mistakes

The most common mistakes that can lead to an unexpected 'export' error include:

* Using incorrect syntax when importing code from another workspace project.
* Failing to install the necessary packages for the project.
* Not properly exporting the code from the other workspace project.

## Fixing the Error

To fix the unexpected 'export' error, developers must first identify the cause of the problem. If the error is due to incorrect syntax, they should review the code and make sure that all imports are properly formatted. If the error is due to missing packages, they should install the necessary packages for the project. Finally, if the error is due to an incorrect export, they should review the code and make sure that all code is properly exported.

### Example 1: Incorrect Syntax

One of the most common causes of the unexpected 'export' error is incorrect syntax when importing code from another workspace project. To fix this issue, developers should review their code and make sure that all imports are properly formatted.

For example, if a developer is attempting to import a module from another workspace project, they should make sure to use the correct syntax:

```javascript
import { MyModule } from '../other-workspace-project/my-module';
```

### Example 2: Missing Packages

Another common cause of the unexpected 'export' error is failing to install the necessary packages for the project. To fix this issue, developers should review the project's package.json file and make sure that all necessary packages are installed.

For example, if a developer is attempting to use a package called 'my-package', they should make sure that it is installed in the project's package.json file:

```json
"dependencies": {
    "my-package": "^1.0.0"
}
```

### Example 3: Incorrect Export

The final common cause of the unexpected 'export' error is not properly exporting the code from the other workspace project. To fix this issue, developers should review their code and make sure that all code is properly exported.

For example, if a developer is attempting to export a module from another workspace project, they should make sure to use the correct syntax:

```javascript
export { MyModule } from '../other-workspace-project/my-module';
```

## Conclusion

In conclusion, the unexpected 'export' error can be caused by a number of issues, including syntax errors, incorrect imports, or missing packages. To fix this error, developers should review their code and make sure that all imports and exports are properly formatted, and that all necessary packages are installed.

If you're developing an API with NestJS, you may have run into the dreaded `Unexpected 'export'` error. This error can be confusing and difficult to debug, but there is a simple solution that can help you get your code up and running in no time.

In this blog post, we'll walk through the steps of how to resolve the `Unexpected 'export'` error when compiling code from another workspace project in a NestJS API. We'll explore the causes of the error, how to debug it, and the steps needed to get your code running again.

## What is the `Unexpected 'export'` Error?

The `Unexpected 'export'` error typically occurs when a developer attempts to compile code from another workspace project in a NestJS API. This error is caused by the NestJS compiler not being able to find the exported module from the other workspace project.

When the compiler is unable to find the exported module, it will throw an `Unexpected 'export'` error. This error can be difficult to debug and can take some time to resolve.

## Debugging the `Unexpected 'export'` Error

When debugging the `Unexpected 'export'` error, the first step is to check the code for any typos or syntax errors. If the code is correct, then the next step is to check the configuration of the workspace project.

The workspace project should be configured correctly in order for NestJS to be able to find the exported module. If the configuration is incorrect, then the compiler will not be able to find the exported module and will throw an `Unexpected 'export'` error.

## Resolving the `Unexpected 'export'` Error

The solution to resolving the `Unexpected 'export'` error is to make sure that the workspace project is configured correctly. To do this, you'll need to update the `tsconfig.json` file of the workspace project.

In the `tsconfig.json` file, you'll need to add the `"composite": true` option to the `compilerOptions` section. This will tell the NestJS compiler to look for the exported module in the workspace project.

```javascript
{
    "compilerOptions": {
        "composite": true,
        // ...
    }
    // ...
}
```

Once you've updated the `tsconfig.json` file, you should be able to compile the code from the workspace project without any errors.

## Conclusion

The `Unexpected 'export'` error can be frustrating to debug, but it is a relatively easy error to resolve. By following the steps outlined in this blog post, you should be able to get your code running again in no time.

If you're still running into issues, then you may need to check the NestJS documentation for further troubleshooting steps. Good luck, and happy coding!
## Recommended Sites

- https://stackoverflow.com/questions/63600753/compiling-code-from-another-workspace-project-in-a-nestjs-api-unexpected-export
- https://github.com/nestjs/nest/issues/3737
- https://docs.nestjs.com/techniques/workspace
- https://github.com/nestjs/nest/issues/3737#issuecomment-606866930