---
layout: post
title: How to Disable Edge Visual Search Icon on Images
tags: ['html', 'css']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)
Edge Visual Search is an AI-based feature that allows users to quickly search for information related to images they come across while browsing the web. Unfortunately, some users may want to disable this feature due to privacy or other reasons. In this article, we will explain how to disable the Edge Visual Search icon on images.

## Understanding Edge Visual Search
Edge Visual Search is an AI-based feature that is available in Microsoft Edge browsers. It allows users to quickly search for information related to images they come across while browsing the web. When the feature is enabled, a small magnifying glass icon will appear in the top right corner of images. By clicking on this icon, users can perform a visual search to find out more information about the image.

## Disabling Edge Visual Search
Unfortunately, some users may want to disable this feature due to privacy or other reasons. To do this, users need to open their Microsoft Edge browser and click on the three dots in the top right corner. From here, they need to select the “Settings” option and then go to the “Advanced” tab. Under this tab, they will find the “Search in address bar with” option and then need to uncheck the “Edge Visual Search” box.

## JavaScript Code
To further customize the Edge Visual Search feature, users can also use JavaScript code to disable the icon. The following code can be used to disable the icon on all images:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('img').forEach(img => {
        img.removeAttribute('data-edge-visual-search');
    });
});
```

This code will remove the “data-edge-visual-search” attribute from all images, effectively disabling the Edge Visual Search icon.

## Typescript Code
Alternatively, users can also use Typescript code to disable the icon. The following code can be used to disable the icon on all images:

```typescript
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('img').forEach(img => {
        (img as HTMLImageElement).removeAttribute('data-edge-visual-search');
    });
});
```

This code will also remove the “data-edge-visual-search” attribute from all images, effectively disabling the Edge Visual Search icon.

## Common Mistakes
When disabling the Edge Visual Search icon, it is important to remember to uncheck the “Edge Visual Search” box in the “Search in address bar with” option. If this box is not unchecked, the icon will still appear on images. Additionally, it is important to make sure that the code used to disable the icon is the correct code for the language being used. For example, using JavaScript code when writing in Typescript will not work.

## Conclusion
Disabling the Edge Visual Search icon on images is a simple process that can be done in just a few steps. First, users need to uncheck the “Edge Visual Search” box in the “Search in address bar with” option in their Microsoft Edge browser. Then, they can use either JavaScript or Typescript code to further customize the feature. It is important to remember to uncheck the “Edge Visual Search” box and to use the correct code for the language being used.

It is possible to disable the Edge Visual Search Icon on images that appear on websites. The Visual Search Icon is a feature of Microsoft Edge that allows users to search for images on the internet. This feature can be useful for some users, but for others, it can be intrusive and distracting. Fortunately, there is a way to disable the Edge Visual Search Icon on images.

## Disabling the Edge Visual Search Icon

To disable the Edge Visual Search Icon, you can add a small piece of JavaScript code to the end of the HTML page. This code will prevent the Visual Search Icon from appearing on images.

### Step 1: Add the JavaScript Code

The JavaScript code you will need to add is as follows:

```javascript
<script>
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('img').forEach(img => {
            img.style.msInterpolationMode = 'nearest-neighbor';
        });
    });
</script>
```

This code should be added to the end of the HTML page, just before the closing `</body>` tag.

### Step 2: Test the Result

Once the JavaScript code has been added, you can test the result. Refresh the page in the browser and the Visual Search Icon should no longer appear on the images.

## Conclusion

Disabling the Edge Visual Search Icon on images is a simple process that involves adding a small piece of JavaScript code to the end of the HTML page. This code will prevent the Visual Search Icon from appearing on images, allowing users to enjoy the website without the distraction of the Visual Search Icon.