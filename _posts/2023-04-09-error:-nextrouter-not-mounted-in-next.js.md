---
layout: post
title: "Error: NextRouter Not Mounted in Next.js"
tags: ['typescript', 'next.js', 'next-router']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When developing applications with [Next.js](https://nextjs.org/), it is common to encounter errors related to the `next-router` package. One such error is the `Error: NextRouter Not Mounted` error, which usually occurs when the `next-router` package is not correctly installed or configured. In this article, we will discuss what this error means, why it occurs, and how to resolve it.

## What is the Error: NextRouter Not Mounted?

The `Error: NextRouter Not Mounted` error occurs when the `next-router` package is not correctly installed or configured. This error can be caused by a variety of different issues, such as an incorrect version of the `next-router` package being installed, or the `next-router` package not being properly configured.

## Common Mistakes

When encountering the `Error: NextRouter Not Mounted` error, there are a few common mistakes that can be made. 

The first mistake is not installing the `next-router` package correctly. This can occur when the wrong version of the `next-router` package is installed, or when the `next-router` package is not installed at all. To ensure that the `next-router` package is correctly installed, it is important to check the version of the `next-router` package that is installed and to make sure that it is compatible with the version of Next.js that you are using.

The second mistake is not configuring the `next-router` package correctly. This can occur when the `next-router` package is not configured to use the correct routes, or when the `next-router` package is not configured to use the correct server-side rendering. To ensure that the `next-router` package is correctly configured, it is important to check the configuration of the `next-router` package and to make sure that it is using the correct routes and server-side rendering.

## Resolving the Error

To resolve the `Error: NextRouter Not Mounted` error, it is important to first check the version of the `next-router` package that is installed and to make sure that it is compatible with the version of Next.js that you are using. If the version of the `next-router` package is not compatible with the version of Next.js that you are using, then it is important to update the `next-router` package to the correct version.

Once the version of the `next-router` package has been updated, it is important to check the configuration of the `next-router` package and to make sure that it is using the correct routes and server-side rendering. If the configuration of the `next-router` package is incorrect, then it is important to update the configuration of the `next-router` package to the correct values.

Finally, once the version of the `next-router` package and the configuration of the `next-router` package have been updated, it is important to restart the application to ensure that the changes have taken effect.

## Conclusion

The `Error: NextRouter Not Mounted` error occurs when the `next-router` package is not correctly installed or configured. To resolve this error, it is important to check the version of the `next-router` package that is installed and to make sure that it is compatible with the version of Next.js that you are using. Once the version of the `next-router` package has been updated, it is important to check the configuration of the `next-router` package and to make sure that it is using the correct routes and server-side rendering. Finally, once the version of the `next-router` package and the configuration of the `next-router` package have been updated, it is important to restart the application to ensure that the changes have taken effect.

Have you ever encountered a situation where you are trying to use the Next.js framework and you get the error “NextRouter not mounted”? If so, you’re not alone! This is a common issue that many developers encounter when working with Next.js. 

In this blog post, we’ll explain what this error is and how to fix it. We’ll also provide a step-by-step guide to help you resolve the issue quickly and easily. 

## What is the NextRouter Not Mounted Error? 

The “NextRouter not mounted” error occurs when the Next.js router is not mounted correctly. This is usually due to a missing or incorrect configuration in your `next.config.js` file. 

The Next.js router is responsible for routing requests to the correct page or component. Without it, the application won’t work correctly. 

## How to Fix the NextRouter Not Mounted Error 

The first step to fixing the “NextRouter not mounted” error is to check your `next.config.js` file. This file is responsible for configuring the Next.js router and other Next.js settings. 

If you don’t have a `next.config.js` file, you’ll need to create one. Here’s an example of a basic `next.config.js` file: 

```javascript
module.exports = {
  webpack: (config, { dev }) => {
    // Perform customizations to webpack config
    // Important: return the modified config
    return config
  },
  webpackDevMiddleware: config => {
    // Perform customizations to webpack dev middleware config
    // Important: return the modified config
    return config
  },
  exportPathMap: function() {
    // Put your custom routes here
    return {
      '/': { page: '/' }
    }
  }
}
```

Once you’ve created your `next.config.js` file, you’ll need to add the following code to it: 

```javascript
const { Router } = require('next/router');

module.exports = {
  webpack: (config, { dev }) => {
    // Perform customizations to webpack config
    // Important: return the modified config
    return config
  },
  webpackDevMiddleware: config => {
    // Perform customizations to webpack dev middleware config
    // Important: return the modified config
    return config
  },
  exportPathMap: function() {
    // Put your custom routes here
    return {
      '/': { page: '/' }
    }
  },
  router: {
    Router
  }
}
```

This code will ensure that the Next.js router is mounted correctly. After you’ve added it, you can save and close the `next.config.js` file. 

## Conclusion 

The “NextRouter not mounted” error is a common issue that many developers encounter when working with Next.js. To fix it, you’ll need to check your `next.config.js` file and add the code provided in this blog post. Once you’ve done that, the error should be resolved. 

If you’re still having trouble resolving the issue, you can reach out to the Next.js community for help. There are many helpful developers who are willing to provide assistance. 

We hope this blog post has helped you resolve the “NextRouter not mounted” error. Good luck!
## Recommended Sites
- [Next.js Documentation - Troubleshooting](https://nextjs.org/docs/advanced-features/custom-error-handling#troubleshooting)
- [Next.js GitHub - NextRouter Not Mounted](https://github.com/zeit/next.js/issues/5462)
- [Stack Overflow - NextRouter Not Mounted](https://stackoverflow.com/questions/56950206/nextrouter-not-mounted-error-in-next-js)