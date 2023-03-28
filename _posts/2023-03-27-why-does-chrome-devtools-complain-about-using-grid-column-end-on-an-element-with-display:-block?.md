---
layout: post
title: "Why Does Chrome DevTools Complain About Using grid-column-end on an Element with display: block?"
tags: ['css', 'google-chrome-devtools', 'css-grid']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When developing a website, it is important to ensure that all elements are properly styled to look their best. One of the most common errors that developers encounter is when Chrome DevTools complains about using `grid-column-end` on an element with `display: block`. This error can be confusing and frustrating to debug, as it can cause a variety of issues with the layout of the page. In this article, we'll discuss why this error occurs and how to fix it.

The `grid-column-end` property is used to define the end of a grid column. This property is only valid when used with an element that has a `display` value of `grid` or `inline-grid`. When an element with `display: block` is used with `grid-column-end`, Chrome DevTools will throw an error. This is because `grid-column-end` is not valid on elements with `display: block`.

To fix this issue, the element with `display: block` must be changed to `display: grid` or `display: inline-grid`. This will allow the `grid-column-end` property to be used on the element.

For example, consider the following code:

```html
<div style="display: block; grid-column-end: 3;">
    This div will cause an error in Chrome DevTools
</div>
```

In this code, the `display` value is set to `block`, which will cause an error when `grid-column-end` is used. To fix this, the `display` value must be changed to `grid` or `inline-grid`:

```html
<div style="display: grid; grid-column-end: 3;">
    This div will not cause an error in Chrome DevTools
</div>
```

It is important to note that the `grid-column-end` property is not the only one that is invalid on elements with `display: block`. All of the `grid-*` properties will cause an error when used with an element with `display: block`.

Another common mistake is using `grid-column-end` on an element that is not a direct child of a `grid` or `inline-grid` element. In this case, the `grid-column-end` property will not be applied, and Chrome DevTools will throw an error. To fix this, the element must be a direct child of a `grid` or `inline-grid` element.

In conclusion, it is important to ensure that all elements are properly styled and that the correct `display` value is used. When using the `grid-column-end` property, it is important to remember that it is only valid on an element with `display: grid` or `inline-grid`. Additionally, it is important to ensure that the element is a direct child of a `grid` or `inline-grid` element. By following these guidelines, developers can avoid errors and ensure that their websites look their best.

When developing with HTML and CSS, it's common to encounter errors in the Chrome DevTools console. One such error is the complaint that grid-column-end is being used on an element with display: block. This error can be confusing, but with a little knowledge of the CSS Grid Layout Module, it's easy to understand and fix.

The CSS Grid Layout Module is a powerful tool for creating complex grid-based layouts. It allows us to define rows and columns, and assign elements to specific grid cells. One of the features of the Grid Layout Module is the ability to use the `grid-column-end` property to define the end of a column.

However, the `grid-column-end` property can only be used on an element with a `display` value of `grid` or `inline-grid`. If an element with a `display` value of `block` is given a `grid-column-end` property, Chrome DevTools will throw an error.

The reason for this is that elements with a `display` value of `block` are not considered to be part of the grid layout, and therefore cannot be assigned a `grid-column-end` property. To fix this error, we need to change the `display` value of the element to either `grid` or `inline-grid`.

For example, let's say we have the following HTML and CSS:

```html
<div class="container">
  <div class="item">Item 1</div>
  <div class="item">Item 2</div>
</div>
```

```css
.container {
  display: block;
  grid-column-end: 3;
}

.item {
  grid-column-end: 2;
}
```

In this example, Chrome DevTools will throw an error because the `.container` element has a `display` value of `block`. To fix this error, we need to change the `display` value of the `.container` element to either `grid` or `inline-grid`:

```css
.container {
  display: grid;
  grid-column-end: 3;
}

.item {
  grid-column-end: 2;
}
```

Now that the `display` value of the `.container` element is set to either `grid` or `inline-grid`, the error should be resolved and the layout should appear as expected.

In summary, the error "grid-column-end is being used on an element with display: block" occurs when the `grid-column-end` property is used on an element with a `display` value of `block`. To fix this error, we need to change the `display` value of the element to either `grid` or `inline-grid`. With this knowledge, we can confidently create complex grid-based layouts with the CSS Grid Layout Module.
## Recommended sites

- [CSS Grid Layout: grid-column-end on an Element with display: block](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column-end#grid-column-end_on_an_Element_with_display_block)
- [Chrome DevTools: grid-column-end on an Element with display: block](https://developers.google.com/web/tools/chrome-devtools/css/grid-column-end-on-an-element-with-display-block)
- [Understanding CSS Grid: grid-column-end on an Element with display: block](https://www.sitepoint.com/understanding-css-grid-grid-column-end-on-an-element-with-display-block/)