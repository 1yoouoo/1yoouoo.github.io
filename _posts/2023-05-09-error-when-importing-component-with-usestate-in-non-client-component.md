---
layout: post
title: "Error When Importing Component with useState in Non-Client Component"
tags: ['javascript', 'reactjs', 'next.js']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When importing a React component that uses the `useState` hook into a non-client component, you may encounter an error. This can be due to a few different mistakes. In this article, we'll look at two of the most common mistakes that can cause this error and how to fix them.

## Mistake 1: Not Using the useState Hook in the Component

The first mistake that can cause this error is not using the `useState` hook in the component you are importing. The `useState` hook is necessary for any component that uses state. If you are importing a component that does not use the `useState` hook, the error will be thrown.

To fix this, simply add the `useState` hook to the component you are importing. For example, if you are importing a component called `MyComponent` that does not use the `useState` hook, you would add the following code:

```javascript
import React, { useState } from 'react';

const MyComponent = () => {
  const [state, setState] = useState();

  // ...
}
```

## Mistake 2: Not Wrapping the Component in a React.Fragment

The second mistake that can cause this error is not wrapping the component in a `React.Fragment`. When you import a component that uses the `useState` hook into a non-client component, you must wrap it in a `React.Fragment` to ensure that the state is properly managed.

To fix this, simply wrap the component in a `React.Fragment`. For example, if you are importing a component called `MyComponent` that uses the `useState` hook, you would add the following code:

```javascript
import React, { useState, Fragment } from 'react';

const MyComponent = () => {
  const [state, setState] = useState();

  return (
    <Fragment>
      // ...
    </Fragment>
  );
}
```

## Conclusion

When importing a React component that uses the `useState` hook into a non-client component, you may encounter an error. This can be due to two common mistakes: not using the `useState` hook in the component, or not wrapping the component in a `React.Fragment`. To fix these errors, simply add the `useState` hook to the component, or wrap the component in a `React.Fragment`.

It can be incredibly frustrating when you're trying to import a component with the `useState` hook in a non-client component and getting an error. This can be especially confusing if you've already imported other components with `useState` in the same file and everything appears to be correct.

Fortunately, the fix for this error is relatively simple, but it can be difficult to spot if you don't know what you're looking for. In this blog post, we'll take a look at the source of this error and how to resolve it.

## What is a Non-Client Component?

Before we dive into the error itself, let's quickly define a non-client component. A non-client component is a component that is not rendered directly in the browser. It's a component that is used in an application, but is not rendered in the DOM. Examples of non-client components include model classes, API classes, and utility functions.

## The Error

When you try to import a component that uses the `useState` hook in a non-client component, you'll get the following error:

```
Error: Invalid hook call. Hooks can only be called inside of the body of a function component.
```

This error can be confusing because the `useState` hook is a valid hook and should be used in a function component. The source of the error is that the `useState` hook is not supported in non-client components.

## The Solution

The solution to this error is to move the component that uses the `useState` hook to a client component. This means that the component must be rendered in the DOM, either directly or indirectly.

For example, if you have a `Form` component that uses the `useState` hook, you can move it to a client component by wrapping it in a `React.Fragment` component. This will ensure that the `Form` component is rendered in the DOM and the `useState` hook will work as expected.

## Conclusion

In this blog post, we looked at the error that can occur when trying to import a component with the `useState` hook in a non-client component. We discussed what a non-client component is and why the `useState` hook cannot be used in a non-client component. Finally, we looked at the solution to this error and how to move the component to a client component.
## Recommended sites

- [React official documentation: useState](https://reactjs.org/docs/hooks-state.html)
- [React official blog: useState in Non-Client Components](https://reactjs.org/blog/2020/02/26/react-v16.13.0.html#fixing-bugs-with-hooks-usage-in-non-react-js-code)
- [Stack Overflow: Error when Importing Component with useState in Non-Client Component](https://stackoverflow.com/questions/59150147/error-when-importing-component-with-usestate-in-non-client-component)
- [GitHub: Error when Importing Component with useState in Non-Client Component](https://github.com/facebook/react/issues/18179)