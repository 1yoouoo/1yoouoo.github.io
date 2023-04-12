---
layout: post
title: "IntersectionObserver Not Intercepting Elements with Display Contents"
tags: ['javascript', 'html', 'css', 'intersection-observer']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

The IntersectionObserver API is a powerful tool for tracking the visibility of elements on a web page. It allows developers to detect when an element enters or leaves the viewport, allowing them to perform certain actions based on the visibility of the element. Unfortunately, it is not always reliable and can sometimes fail to detect elements with the `display: contents` property set.

The `display: contents` property is a relatively new CSS property that allows an element to be treated as if it had no box model. This means that the element won't have a width, height, padding or border, and will be treated as if it were a single element. This is especially useful for elements that are part of a layout, such as a grid or flexbox.

Unfortunately, the IntersectionObserver API does not currently support the `display: contents` property, meaning that it will not detect elements with this property set. This can lead to unexpected behavior, as the IntersectionObserver will not detect any elements inside the element with the `display: contents` property set.

To get around this issue, developers need to use a workaround. One approach is to wrap the element with the `display: contents` property set in a container element, and then use the IntersectionObserver API to detect the visibility of the container element.

This approach works because the IntersectionObserver API will detect the visibility of the container element, even if the element with the `display: contents` property set is not visible. This means that the IntersectionObserver API will still be able to detect when the element with the `display: contents` property set enters or leaves the viewport, even though it cannot detect the element itself.

To illustrate this workaround, let's look at an example. Suppose we have the following HTML:

```html
<div class="container">
  <div class="item" style="display: contents;">
    Item 1
  </div>
  <div class="item" style="display: contents;">
    Item 2
  </div>
</div>
```

We want to use the IntersectionObserver API to detect when the `item` elements enter or leave the viewport. However, since the `item` elements have the `display: contents` property set, the IntersectionObserver API will not detect them.

To get around this, we can wrap the `item` elements in a container element, like so:

```html
<div class="container">
  <div class="container-wrapper">
    <div class="item" style="display: contents;">
      Item 1
    </div>
    <div class="item" style="display: contents;">
      Item 2
    </div>
  </div>
</div>
```

Now, we can use the IntersectionObserver API to detect the visibility of the `container-wrapper` element. This will allow us to detect when the `item` elements enter or leave the viewport, even though the IntersectionObserver API cannot detect the `item` elements directly.

To set up the IntersectionObserver, we can use the following code:

```javascript
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // Do something when the element enters the viewport
    } else {
      // Do something when the element leaves the viewport
    }
  });
});

observer.observe(document.querySelector('.container-wrapper'));
```

This code will set up an IntersectionObserver that will detect when the `container-wrapper` element enters or leaves the viewport. Whenever this happens, the code will execute the corresponding callback function.

In conclusion, the IntersectionObserver API does not currently support the `display: contents` property. To get around this, developers can wrap the element with the `display: contents` property set in a container element, and then use the IntersectionObserver API to detect the visibility of the container element. This will allow the IntersectionObserver API to detect when the element with the `display: contents` property set enters or leaves the viewport, even though it cannot detect the element itself.

Have you ever encountered an issue with IntersectionObserver not intercepting elements with display contents? If so, you're not alone. This is a common issue that developers face when using IntersectionObserver, and it can be a bit tricky to figure out. In this blog post, we'll explore what this issue is, why it occurs, and how to fix it.

## What is IntersectionObserver?

IntersectionObserver is a JavaScript API that allows developers to detect when an element enters or exits the viewport. It's used to create lazy loading, infinite scroll, and other performance-enhancing techniques. It's a powerful tool, but it can be tricky to get right.

## What is the Issue?

The issue we're talking about here is when IntersectionObserver fails to detect an element with display contents. This can be a problem because it means that the element won't be lazy loaded, or that the infinite scroll won't work properly. The issue can be even more confusing because it only occurs in certain circumstances.

## Why Does This Issue Occur?

The issue occurs because IntersectionObserver only works with elements that are visible. If an element has a display value of `none`, IntersectionObserver will not detect it. This is because IntersectionObserver is designed to only detect elements that are visible on the page.

## How to Fix the Issue

The solution to this issue is to make sure that all elements that you want to detect with IntersectionObserver have a display value of `block`. This will ensure that IntersectionObserver can detect the element and that it will work as expected.

## Example Code

To help illustrate how to fix this issue, let's take a look at some example code. Here, we have a div with a display value of `none`. We want to use IntersectionObserver to detect when this element enters the viewport.

```html
<div id="myDiv" style="display: none;">
  This element won't be detected by IntersectionObserver
</div>
```

To fix this issue, we need to change the display value to `block`. This will ensure that IntersectionObserver can detect the element.

```html
<div id="myDiv" style="display: block;">
  This element will be detected by IntersectionObserver
</div>
```

## Conclusion

In this blog post, we explored why IntersectionObserver fails to detect elements with display contents, and how to fix the issue. We saw that the issue occurs because IntersectionObserver only works with elements that are visible, and that the solution is to make sure that all elements that you want to detect with IntersectionObserver have a display value of `block`. We also looked at an example code snippet to help illustrate the issue and the solution.
# Recommended Sites

- [Using Intersection Observer to Lazy Load Images](https://developers.google.com/web/fundamentals/performance/lazy-loading-guidance/images-and-video/)
- [IntersectionObserver API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
- [IntersectionObserver not intercepting elements with display:contents](https://github.com/WICG/IntersectionObserver/issues/211)
- [IntersectionObserver Not Intercepting Elements with display:contents](https://stackoverflow.com/questions/53681281/intersectionobserver-not-intercepting-elements-with-displaycontents)