---
layout: post
title: "Error: Jest Test Environment 'jest-environment-jsdom' Not Found"
tags: ['javascript', 'node.js', 'typescript', 'jestjs', 'ts-jest']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When running the Jest testing framework, you may encounter the error `Error: Jest Test Environment 'jest-environment-jsdom' Not Found`. This is a common error that can occur when using Jest and is caused by a missing configuration setting. In this article, we'll discuss why this error occurs and how to fix it.

## What Causes the Error?

The `Error: Jest Test Environment 'jest-environment-jsdom' Not Found` error occurs when the Jest testing framework is unable to find the configuration setting `jest-environment-jsdom` in your project's `package.json` file. This configuration setting is required for Jest to be able to run tests in a browser-like environment. Without this setting, Jest will be unable to properly run tests in a browser-like environment.

## How to Fix the Error

To fix the `Error: Jest Test Environment 'jest-environment-jsdom' Not Found` error, you must add the `jest-environment-jsdom` configuration setting to your `package.json` file. This setting should be added to the `jest` section of your `package.json` file and should look like this:

```json
{
  "jest": {
    "env": {
      "jest-environment-jsdom": "true"
    }
  }
}
```

Once this setting has been added to your `package.json` file, Jest should be able to properly run tests in a browser-like environment.

## Common Mistakes

When trying to fix the `Error: Jest Test Environment 'jest-environment-jsdom' Not Found` error, it's important to be aware of some common mistakes that can cause the error to persist.

The first mistake to be aware of is that the `jest-environment-jsdom` configuration setting must be added to the `jest` section of your `package.json` file. If it is added to any other section, Jest will not be able to find the setting and the error will persist.

The second mistake to be aware of is that the `jest-environment-jsdom` configuration setting must be set to `true`. If it is set to any other value, Jest will not be able to find the setting and the error will persist.

## Conclusion

In conclusion, the `Error: Jest Test Environment 'jest-environment-jsdom' Not Found` error occurs when the Jest testing framework is unable to find the configuration setting `jest-environment-jsdom` in your project's `package.json` file. To fix this error, you must add the `jest-environment-jsdom` configuration setting to your `package.json` file and ensure that it is set to `true`. Additionally, it's important to be aware of some common mistakes that can cause the error to persist.

If you're a developer who's been working in **Javascript** or **Typescript**, you might have encountered the following error: `Error: Jest Test Environment 'jest-environment-jsdom' Not Found`. 

This error occurs when you're trying to run a **Jest** test in your project. It means that the **Jest** test environment is not properly configured. To resolve this issue, you'll need to make sure that the `jest-environment-jsdom` package is installed and that it's properly configured in your **Jest** configuration file.

## Installing the `jest-environment-jsdom` Package

The first step to resolving this issue is to install the `jest-environment-jsdom` package. This package provides the **Jest** test environment with the **JSDOM** environment, which is necessary for running **Jest** tests in a browser-like environment.

You can install the package using **npm** or **yarn**:

```bash
# Using npm
npm install --save-dev jest-environment-jsdom

# Using yarn
yarn add --dev jest-environment-jsdom
```

Once the package is installed, you'll need to configure **Jest** to use it as the test environment.

## Configuring **Jest** to Use the `jest-environment-jsdom` Package

The next step is to configure **Jest** to use the `jest-environment-jsdom` package as the test environment. To do this, you'll need to add the following entry to your **Jest** configuration file (e.g. `jest.config.js`):

```javascript
module.exports = {
  testEnvironment: 'jest-environment-jsdom'
};
```

Once you've added the entry, you can save the file and try running your **Jest** tests again. If everything is configured correctly, you should no longer see the `Error: Jest Test Environment 'jest-environment-jsdom' Not Found` error.

## Conclusion

If you're seeing the `Error: Jest Test Environment 'jest-environment-jsdom' Not Found` error, it means that the **Jest** test environment is not properly configured. To resolve this issue, you'll need to install the `jest-environment-jsdom` package and configure **Jest** to use it as the test environment.

Once you've done this, you should be able to run your **Jest** tests without any issues. If you're still having trouble, make sure to double-check your **Jest** configuration file and make sure that you've added the `testEnvironment` entry correctly.
# Recommended Sites

- [Jest Documentation - Troubleshooting](https://jestjs.io/docs/en/troubleshooting)
- [GitHub - Jest Environment Not Found](https://github.com/facebook/jest/issues/9014)
- [Stack Overflow - Jest Environment Not Found](https://stackoverflow.com/questions/49629072/jest-test-environment-jest-environment-jsdom-not-found)