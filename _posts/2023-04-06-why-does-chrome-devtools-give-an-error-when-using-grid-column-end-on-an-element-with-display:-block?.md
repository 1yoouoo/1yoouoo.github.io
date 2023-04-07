---
layout: post
title: "Why Does Chrome DevTools Give an Error When Using grid-column-end on an Element with display: block?"
tags: ['css', 'google-chrome-devtools', 'css-grid']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When using the grid-column-end property on an element with display: block, Chrome DevTools will throw an error. This error is thrown because the grid-column-end property is only supported on elements with display: grid or display: inline-grid.

The grid-column-end property is used to specify the ending column line of a grid item. It is only used in combination with the grid-column-start property. Together, these properties define the horizontal placement of a grid item within the grid.

In order to use the grid-column-end property, the element must have a display value of grid or inline-grid. This is because the grid-column-end property is a part of the CSS Grid Layout Module, which is only supported on elements with display: grid or display: inline-grid.

One of the most common mistakes when using the grid-column-end property is to forget to set the display value of the element to grid or inline-grid. For example, if you were to set the display value of an element to block and then try to use the grid-column-end property, Chrome DevTools would throw an error.

Another common mistake is to forget to set the grid-column-start property. The grid-column-start property is used to specify the starting column line of a grid item. Without setting the grid-column-start property, the grid-column-end property will not work.

To illustrate these mistakes, let's look at a few examples.

In the first example, we have an element with display: block and grid-column-end set to 3. Since the element has a display value of block, Chrome DevTools will throw an error.

```css
div {
  display: block;
  grid-column-end: 3;
}
```

In the second example, we have an element with display: grid and grid-column-end set to 3. However, we have forgotten to set the grid-column-start property. Without setting the grid-column-start property, the grid-column-end property will not work.

```css
div {
  display: grid;
  grid-column-end: 3;
}
```

In the third example, we have an element with display: grid and both the grid-column-start and grid-column-end properties set. This is the correct way to use the grid-column-end property and Chrome DevTools will not throw an error.

```css
div {
  display: grid;
  grid-column-start: 1;
  grid-column-end: 3;
}
```

When using the grid-column-end property, it is important to remember to set the display value of the element to grid or inline-grid. It is also important to remember to set the grid-column-start property in order for the grid-column-end property to work. If either of these conditions are not met, Chrome DevTools will throw an error.

If you've ever tried to use the `grid-column-end` property on an element with `display: block`, you may have been surprised to find that Chrome DevTools throws an error. In this post, we'll take a look at why this is the case, and what you can do to fix it.

## What is the Error?

The error you will see in Chrome DevTools when trying to use `grid-column-end` on an element with `display: block` is:

> **Error in parsing value for 'grid-column-end'.**  Declaration dropped.

## Why Does This Error Occur?

The reason this error occurs is because the `grid-column-end` property is only valid on elements with `display: grid` or `display: inline-grid`. If you try to use it on an element with `display: block`, then it will be ignored by the browser and you will see this error in Chrome DevTools.

## How to Fix the Error

To fix this error, you simply need to change the `display` property of the element from `block` to `grid` or `inline-grid`. Once you do this, the `grid-column-end` property will be valid and the error will be gone.

Here is an example of how you can do this in CSS:

```css
.element {
  display: grid;
  grid-column-end: 4;
}
```

And here is an example of how you can do this in JavaScript:

```javascript
const element = document.querySelector('.element');
element.style.display = 'grid';
element.style.gridColumnEnd = '4';
```

## Conclusion

As you can see, the error you get in Chrome DevTools when using `grid-column-end` on an element with `display: block` is due to the fact that the `grid-column-end` property is only valid on elements with `display: grid` or `display: inline-grid`. To fix this error, you simply need to change the `display` property of the element to `grid` or `inline-grid`.
## Recommended sites

- [Chrome DevTools | Google Developers](https://developers.google.com/web/tools/chrome-devtools/)
- [CSS Grid Layout Module Level 1](https://www.w3.org/TR/css-grid-1/)
- [CSS Grid Layout: The `grid-column-end` Property](https://www.freecodecamp.org/news/css-grid-layout-the-grid-column-end-property-e3a3d3eecb6a/)
- [CSS Grid Layout: Understanding the `display` Property](https://www.freecodecamp.org/news/css-grid-layout-understanding-the-display-property-d8a6a7f6f7f6/)