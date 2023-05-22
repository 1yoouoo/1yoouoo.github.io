---
layout: post
title: "Fixing Address Bar Visibility in Safari iOS 15 for Fixed Positioned Views"
tags: ['html', 'css', 'ios', 'safari', 'address-bar']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

### Common Mistakes and Errors

In this article, we will discuss how to fix the address bar visibility issue in Safari iOS 15 for fixed positioned views. We will also talk about two common mistakes that developers make when dealing with this issue.

**Mistake #1:** Not accounting for the dynamic height of the address bar in Safari iOS 15.

**Mistake #2:** Relying on `window.innerHeight` to calculate the viewport height.

## The Issue with Address Bar Visibility in Safari iOS 15

In Safari iOS 15, the address bar has a dynamic height that changes as the user scrolls. This poses a problem for fixed positioned views, as they may not account for the changing height of the address bar, leading to content being obscured or cut off.

## The Solution: Using `window.visualViewport`

To fix the address bar visibility issue, we can use the `window.visualViewport` API to calculate the correct viewport height. This API provides an accurate measurement of the viewport dimensions, taking into account the dynamic height of the address bar.

Here's an example of how to use `window.visualViewport` to set the height of a fixed positioned view:

```javascript
const fixedView = document.querySelector('.fixed-view');

function updateFixedViewHeight() {
  const viewportHeight = window.visualViewport.height;
  fixedView.style.height = `${viewportHeight}px`;
}

window.visualViewport.addEventListener('resize', updateFixedViewHeight);
updateFixedViewHeight();
```

In this example, we first select the fixed positioned view element using `document.querySelector`. Then, we define a function `updateFixedViewHeight` that sets the height of the fixed view to the current `window.visualViewport.height`. We also add a `resize` event listener to the `window.visualViewport` to update the fixed view height whenever the viewport size changes.

## The Problem with `window.innerHeight`

Many developers rely on `window.innerHeight` to calculate the viewport height. However, this method does not account for the dynamic height of the address bar in Safari iOS 15, leading to incorrect measurements.

Here's an example of the issue when using `window.innerHeight`:

```javascript
const fixedView = document.querySelector('.fixed-view');

function updateFixedViewHeight() {
  const viewportHeight = window.innerHeight;
  fixedView.style.height = `${viewportHeight}px`;
}

window.addEventListener('resize', updateFixedViewHeight);
updateFixedViewHeight();
```

In this example, we use `window.innerHeight` to calculate the viewport height. However, this will lead to an incorrect height calculation in Safari iOS 15, as it does not account for the dynamic address bar height.

## The Importance of `window.visualViewport` in Safari iOS 15

As mentioned earlier, the `window.visualViewport` API is crucial for accurately calculating the viewport height in Safari iOS 15. It provides an up-to-date measurement of the viewport dimensions, taking into account the dynamic address bar height.

Here's a comparison between `window.innerHeight` and `window.visualViewport.height`:

```javascript
console.log('window.innerHeight:', window.innerHeight);
console.log('window.visualViewport.height:', window.visualViewport.height);
```

In Safari iOS 15, `window.innerHeight` will remain constant, even when the address bar height changes. On the other hand, `window.visualViewport.height` will provide an accurate measurement of the current viewport height, accounting for the dynamic address bar height.

## A Complete Example with Fixed Positioned Views

Here's a complete example of how to use `window.visualViewport` to fix the address bar visibility issue in Safari iOS 15 for fixed positioned views:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    .fixed-view {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: rgba(0, 0, 0, 0.8);
      color: white;
      text-align: center;
      padding: 1rem;
    }
  </style>
</head>
<body>
  <div class="fixed-view">This is a fixed positioned view</div>
  <script>
    const fixedView = document.querySelector('.fixed-view');

    function updateFixedViewHeight() {
      const viewportHeight = window.visualViewport.height;
      fixedView.style.height = `${viewportHeight}px`;
    }

    window.visualViewport.addEventListener('resize', updateFixedViewHeight);
    updateFixedViewHeight();
  </script>
</body>
</html>
```

In this example, we have a fixed positioned view with a background color and some text. We use the `window.visualViewport` API to set the height of the fixed view, ensuring that it accounts for the dynamic address bar height in Safari iOS 15.

## Conclusion

In summary, the address bar visibility issue in Safari iOS 15 for fixed positioned views can be fixed by using the `window.visualViewport` API. This API provides an accurate measurement of the viewport dimensions, taking into account the dynamic height of the address bar. By using this API, developers can avoid common mistakes such as relying on `window.innerHeight` and not accounting for the dynamic address bar height.

**Understanding the Error**

In iOS 15, Apple introduced a new design for the Safari browser, which includes a change in the way the address bar behaves. When scrolling down a webpage, the address bar is hidden, and when scrolling up, it reappears. This can cause issues with fixed positioned elements, such as headers, footers, or sidebars, as they may become obscured by the address bar or unexpectedly shift in position.

**Step 1: Identify the Problem**

To begin, you must first identify the elements that are affected by this issue. Look for any elements with a `position: fixed` CSS property, as these are the most likely to be impacted by the address bar's behavior.

**Step 2: Create a Wrapper Element**

To address this issue, you can create a wrapper element around the fixed positioned element. This wrapper will help to ensure that the fixed positioned element remains in the correct position, even when the address bar is hidden or shown.

```javascript
const FixedElementWrapper = ({ children }) => {
  return <div className="fixed-element-wrapper">{children}</div>;
};
```

In this example, we create a simple React component called `FixedElementWrapper` that takes in `children` as a prop and renders them inside a `div` with the class `fixed-element-wrapper`.

**Step 3: Apply CSS to the Wrapper**

Next, apply the necessary CSS to the wrapper element to ensure it maintains the correct position and size. The key is to use the `position: sticky` property, which will keep the element in place while also allowing it to move with the scroll.

```css
.fixed-element-wrapper {
  position: sticky;
  top: 0;
  z-index: 1000;
}
```

In this example, we apply the `position: sticky` property to the `.fixed-element-wrapper` class, setting the `top` value to `0` to keep it at the top of the viewport, and assigning a high `z-index` value to ensure it is always visible above other elements.

**Step 4: Update Your Fixed Positioned Elements**

Now that you have created the wrapper component and applied the necessary CSS, you need to update your fixed positioned elements to use this new wrapper. Replace the fixed positioned element with the `FixedElementWrapper` component, passing the element as a child.

```javascript
// Before
<div className="fixed-element">My Fixed Element</div>

// After
<FixedElementWrapper>
  <div className="fixed-element">My Fixed Element</div>
</FixedElementWrapper>
```

In this example, we replace the original `div` with the `FixedElementWrapper` component, passing the original `div` as a child.

**Step 5: Test Your Solution**

Finally, test your solution by opening your web application in Safari on iOS 15. Scroll up and down the page to ensure that the address bar's behavior no longer impacts the position and visibility of your fixed positioned elements.

**Conclusion**

In conclusion, the new address bar behavior in Safari on iOS 15 can cause issues with fixed positioned elements, but by following the steps outlined in this blog post, you can resolve these issues and ensure that your web application remains compatible with this popular mobile browser. By creating a wrapper element, applying the correct CSS properties, and updating your fixed positioned elements to use this wrapper, you can maintain the correct position and visibility of your elements, regardless of the address bar's behavior.

As developers, it's crucial to stay up-to-date with the latest changes in browser behavior and design, as these can have a significant impact on the user experience of your web applications. By proactively addressing these issues and sharing your solutions with the community, you can contribute to the ongoing improvement of web development practices and help to create a better experience for users across all devices and browsers.

Remember to always test your solutions thoroughly and seek feedback from your peers to ensure that your code is both effective and efficient. With a little bit of effort and attention to detail, you can overcome the challenges presented by browser compatibility and create web applications that are both visually appealing and highly functional on all platforms.
# Recommended sites

1. [Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-15-release-notes)
2. [WebKit on iOS 15](https://webkit.org/blog/11975/updates-to-webkit-on-ios-15/)
3. [CSS-Tricks: Fixing the Address Bar in iOS 15](https://css-tricks.com/fixing-the-address-bar-in-ios-15/)
4. [Stack Overflow: Address Bar Visibility in Safari iOS 15](https://stackoverflow.com/questions/69564174/address-bar-visibility-in-safari-ios-15)
5. [GitHub: iOS 15 Safari Address Bar Issue](https://github.com/WebKit/WebKit/issues/234601)