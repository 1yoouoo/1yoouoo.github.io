---
layout: post
title: "Why Doesn't Microsoft Edge Support AVIF Images?"
tags: ['html', 'browser', 'microsoft-edge', 'w3c', 'avif']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)
Microsoft Edge is the default web browser for Windows 10 and is the successor to Internet Explorer. It is a Chromium-based browser, meaning that it uses the same open-source code as Google Chrome. As a result, it supports most of the same web technologies, including the popular image format JPEG. However, Microsoft Edge does not support the newer image format AVIF, which is quickly becoming the preferred image format for the web.

AVIF is a relatively new image format that is based on the AV1 video codec. It is an open-source format that is supported by most major browsers, including Chrome, Firefox, Safari, and Opera. Unlike JPEG, AVIF offers superior compression, meaning that it can reduce the file size of an image by up to 50% without sacrificing quality. This makes it ideal for web applications, where page load times are critical.

Despite the advantages of AVIF, Microsoft Edge does not support it. This is because Microsoft Edge is based on the Chromium browser engine, which does not support AVIF. The Chromium engine is used by Google Chrome and other popular browsers, but it does not include support for AVIF. As a result, Microsoft Edge users cannot view images in the AVIF format.

The lack of AVIF support in Microsoft Edge is a significant limitation, as it prevents web developers from using the latest image formats to reduce page load times. Fortunately, there are several workarounds that can be used to ensure that AVIF images are displayed correctly on Microsoft Edge.

One workaround is to convert AVIF images to the older JPEG format. This can be done using a variety of free online tools, such as ImageOptim and TinyPNG. Converting AVIF images to JPEG will allow them to be displayed correctly on Microsoft Edge, although the image quality may suffer due to the lossy compression used by JPEG.

Another workaround is to use the HTML5 `<picture>` element. This element allows web developers to specify multiple sources for an image, allowing them to provide an AVIF version of the image for browsers that support it and a JPEG version for those that don't.

```javascript
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="My Image">
</picture>
```

By using the `<picture>` element, web developers can ensure that their images are displayed correctly on Microsoft Edge, while still taking advantage of the superior compression offered by AVIF.

Finally, web developers can use the WebP format instead of AVIF. WebP is an open-source image format that is supported by Google Chrome, Firefox, and Microsoft Edge. It offers similar compression to AVIF, but with wider browser support.

In conclusion, Microsoft Edge does not support the AVIF image format. This can be a significant limitation for web developers, as it prevents them from taking advantage of the superior compression offered by AVIF. Fortunately, there are several workarounds that can be used to ensure that AVIF images are displayed correctly on Microsoft Edge.

In today's world, images are everywhere. We use them to convey information, tell stories, and even to express ourselves. But what happens when the images we want to use are not supported by the browser we are using? This is the case with AVIF images and Microsoft Edge.

AVIF (AV1 Image File Format) is a new image format that is based on the AV1 video codec, a royalty-free video format created by the Alliance for Open Media (AOMedia). AVIF is designed to be a successor to the popular JPEG and WebP image formats, offering better compression and higher quality images at smaller file sizes.

Unfortunately, Microsoft Edge does not currently support the AVIF image format. This means that if you are using Edge to view a website that uses AVIF images, they will not be displayed correctly. This can be a major problem for web developers, as it means that they are unable to use the latest image formats to create the best experience for their users.

## What Causes This Error?

The main cause of this error is that Microsoft Edge does not support the AVIF image format. This is because the AV1 video codec, on which AVIF is based, is not yet supported by Edge. As a result, any website that uses AVIF images will not be displayed correctly in Edge.

## How to Fix the Error

Fortunately, there is a way to fix this error and make your website work correctly in Edge. The first step is to use a different image format, such as JPEG or WebP, which are both supported by Edge.

If you want to use AVIF images, you can also use a polyfill library to convert AVIF images to a format that Edge can understand. There are several libraries available, such as the AVIF Polyfill library, which can be used to convert AVIF images to JPEG or WebP.

## JavaScript Code Example

Here is an example of how to use the AVIF Polyfill library to convert an AVIF image to JPEG or WebP:

```javascript
// Load the AVIF Polyfill library
const AVIFPolyfill = require('avif-polyfill');

// Load the AVIF image
const avifImage = require('avif-image');

// Convert the AVIF image to JPEG or WebP
const convertedImage = AVIFPolyfill.convert(avifImage, {
  format: 'jpeg' // or 'webp'
});
```

This code example shows how to use the AVIF Polyfill library to convert an AVIF image to JPEG or WebP. The library can also be used to convert AVIF images to any other format supported by Edge.

## Conclusion

In conclusion, Microsoft Edge does not currently support the AVIF image format. This can be a major problem for web developers, as it means that they are unable to use the latest image formats to create the best experience for their users. Fortunately, there is a way to fix this error and make your website work correctly in Edge. You can either use a different image format, such as JPEG or WebP, or you can use a polyfill library to convert AVIF images to a format that Edge can understand. By following the steps outlined in this blog post, you should be able to make your website work correctly in Edge.
## Recommended Sites

- [Microsoft Support](https://support.microsoft.com/en-us/help/4520260/microsoft-edge-avif-image-support)
- [Microsoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2020/08/12/avif-image-support-microsoft-edge/)
- [Mozilla Hacks Blog](https://hacks.mozilla.org/2020/07/avif-now-supported-in-firefox/)
- [AV1 Image File Format (AVIF) Explained](https://www.howtogeek.com/721127/what-is-the-av1-image-file-format-avif-explained/)