---
layout: post
title: "IntersectionObserver Not Intercepting Elements with Display Contents"
tags: ['javascript', 'html', 'css', 'intersection-observer']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

IntersectionObserver is a JavaScript API that allows developers to detect when an element enters or exits the viewport. It's a powerful tool for creating user experiences that are more reactive and engaging. Unfortunately, some developers have encountered an issue where IntersectionObserver does not intercept elements with a `display: contents` style applied. This can cause unexpected behavior, as the element may not be detected when it enters the viewport. In this article, we'll discuss how to troubleshoot this issue and get your IntersectionObserver working as expected.

## Common Mistakes

When using IntersectionObserver, there are a few common mistakes that can cause the issue of `display: contents` elements not being detected. The first is forgetting to add the `root` option to the IntersectionObserver options. The `root` option specifies the element that will be used as the viewport for the observer. Without this option, the browser's viewport will be used as the viewport, and elements with `display: contents` may not be detected.

The second common mistake is not setting the `threshold` option to the correct value. The `threshold` option specifies the percentage of the element that must enter the viewport before the observer will detect it. If the `threshold` is set too high, elements with `display: contents` may not be detected.

## Code Example

To illustrate how to properly use IntersectionObserver, let's look at a simple example. We'll create an observer that will detect when an element enters the viewport and log a message to the console.

```javascript
// Select the element to observe
const element = document.querySelector('.my-element');

// Create the observer
const observer = new IntersectionObserver(
  (entries) => {
    // Check if the element is entering the viewport
    if (entries[0].isIntersecting) {
      console.log('Element has entered the viewport!');
    }
  },
  {
    root: document.querySelector('#my-root-element'),
    threshold: 0.5
  }
);

// Start observing the element
observer.observe(element);
```

In this example, we've specified the `root` option to be a specific element, and the `threshold` option to be 0.5. This means that the element must be at least 50% visible in the viewport for the observer to detect it. This should ensure that all elements, including those with `display: contents`, are detected by the observer.

## Other Considerations

In addition to the two common mistakes mentioned above, there are a few other considerations to keep in mind when using IntersectionObserver. 

First, the `root` element specified in the options must be an ancestor of the element being observed. If the `root` element is not an ancestor of the observed element, the observer will not be able to detect the element.

Second, the `threshold` option must be set to a value between 0 and 1. If the `threshold` is set to a value outside of this range, the observer will not be able to detect the element.

Finally, the `rootMargin` option can be used to adjust the size of the viewport used by the observer. This option is useful for cases where the element may not be visible in the viewport, but is still within the `root` element.

## Conclusion

IntersectionObserver is a powerful tool for creating user experiences that are more reactive and engaging. Unfortunately, some developers have encountered an issue where IntersectionObserver does not intercept elements with a `display: contents` style applied. This can be caused by forgetting to add the `root` option to the IntersectionObserver options, not setting the `threshold` option to the correct value, or not setting the `root` element to an ancestor of the observed element. Additionally, the `threshold` option must be set to a value between 0 and 1, and the `rootMargin` option can be used to adjust the size of the viewport used by the observer. By following these tips and troubleshooting steps, you should be able to get your IntersectionObserver working as expected.
Have you ever encountered an issue with IntersectionObserver not intercepting elements with display contents? If so, you're not alone. This is a common issue that occurs when using IntersectionObserver to observe elements with display contents. In this blog post, we'll discuss what this issue is, why it occurs, and how to solve it. 

## What is IntersectionObserver?
IntersectionObserver is a browser API that allows developers to observe when an element is visible in the viewport. It can be used to detect when an element is entering or leaving the viewport, as well as when an element is partially visible. This is useful for things such as lazy loading images, or triggering animations when an element is visible. 

## What is the Issue?
The issue occurs when using IntersectionObserver to observe elements with display contents. Display contents is a CSS property that is used to hide elements from the layout. It does this by making the element invisible, but still taking up space in the layout. This can cause issues with IntersectionObserver, as it will not be able to detect when the element is visible. 

## Why Does This Issue Occur?
This issue occurs because IntersectionObserver relies on the browser's layout engine to determine when an element is visible. When an element has display contents set, it is invisible to the layout engine. As a result, IntersectionObserver is not able to detect when the element is visible. 

## How to Solve the Issue
The solution to this issue is to set the visibility property of the element to visible. This will make the element visible to the layout engine, and thus IntersectionObserver will be able to detect when the element is visible. 

### Example
Let's look at an example of how to solve this issue. In this example, we have an element with display contents set. 

```html
<div style="display: contents;">My Element</div>
```

To make this element visible to the layout engine, we need to set the visibility property to visible.

```html
<div style="display: contents; visibility: visible;">My Element</div>
```

Now, IntersectionObserver will be able to detect when the element is visible. 

## Conclusion
In this blog post, we discussed the issue of IntersectionObserver not intercepting elements with display contents. We discussed what this issue is, why it occurs, and how to solve it. We also looked at an example of how to solve this issue by setting the visibility property of the element to visible. Hopefully, this blog post has helped you understand the issue and how to solve it.
## Recommended sites

- [Intersection Observer Not Intercepting Elements with Display Contents](https://stackoverflow.com/questions/51334432/intersection-observer-not-intercepting-elements-with-display-contents)
- [Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
- [IntersectionObserver Not Intercepting Elements with Display Contents](https://www.sitepoint.com/intersectionobserver-not-intercepting-elements-with-display-contents/)