---
layout: post
title: "Sending Emails with Nodemailer After Google Disables Less Secure App Option"
tags: ['node.js', 'oauth-2.0', 'gmail', 'nodemailer']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

Sending emails with Nodemailer can be a tricky process, especially after Google has disabled the Less Secure App option. This article will explain the various steps that need to be taken in order to successfully send emails with Nodemailer.

## What is Nodemailer?

Nodemailer is an npm package that enables Node.js applications to send emails. It is a popular library for creating and sending emails from Node.js applications. It is easy to use and provides many features such as email address validation, SMTP authentication, and HTML content support.

## What is the Less Secure App option?

The Less Secure App option is a Google setting that allows users to access their accounts with applications that do not use the latest security measures. This option was disabled by Google in June of 2019 in order to increase security and prevent malicious applications from accessing user accounts.

## How to send emails with Nodemailer after Google disables the Less Secure App option?

In order to send emails with Nodemailer after the Less Secure App option has been disabled, you will need to use OAuth2. OAuth2 is an open standard for authorization that provides a secure way to access user data.

### Step 1: Create a Project in the Google Developer Console

The first step is to create a project in the Google Developer Console. This will allow you to create credentials that are needed for authentication.

1. Go to the [Google Developer Console](https://console.developers.google.com/projectselector/apis/credentials).
2. Click on **Create Project** and enter a project name.
3. Select a project type and click **Create**.

### Step 2: Enable the Gmail API

The next step is to enable the Gmail API. This will allow you to access the Gmail API and create credentials.

1. Go to the [Google APIs Library](https://console.developers.google.com/apis/library).
2. Search for the **Gmail API** and click on it.
3. Click on **Enable** to enable the API.

### Step 3: Create OAuth2 Credentials

The next step is to create OAuth2 credentials. This will allow you to authenticate with the Gmail API and send emails.

1. Go to the [Google APIs Credentials](https://console.developers.google.com/apis/credentials).
2. Click on **Create Credentials** and select **OAuth Client ID**.
3. Select **Web application** as the application type.
4. Enter a name for your credentials and click **Create**.

### Step 4: Configure Nodemailer

The next step is to configure Nodemailer to use OAuth2. This will allow you to authenticate with the Gmail API and send emails.

```javascript
let transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    type: 'OAuth2',
    user: 'your-email@gmail.com',
    clientId: 'your-client-id',
    clientSecret: 'your-client-secret',
    refreshToken: 'your-refresh-token',
    accessToken: 'your-access-token'
  }
});
```

In the above code, you will need to replace `your-email@gmail.com` with your email address, `your-client-id` with the Client ID from the Google Developer Console, `your-client-secret` with the Client Secret from the Google Developer Console, `your-refresh-token` with the Refresh Token from the Google Developer Console, and `your-access-token` with the Access Token from the Google Developer Console.

### Step 5: Send the Email

The final step is to send the email. This can be done using the `sendMail()` method of the Nodemailer transporter object.

```javascript
transporter.sendMail({
  from: 'your-email@gmail.com',
  to: 'recipient-email@example.com',
  subject: 'Email Subject',
  text: 'Email Body'
});
```

In the above code, you will need to replace `your-email@gmail.com` with your email address and `recipient-email@example.com` with the recipient's email address.

## Conclusion

Sending emails with Nodemailer after Google disables the Less Secure App option can be a tricky process. However, by following the steps outlined in this article, you should be able to successfully send emails with Nodemailer.

If you have been using Nodemailer to send emails using your Gmail account, you may have encountered an error recently when trying to send emails. This is because Google has recently disabled the "Less Secure App" option, which was previously used to authorize Nodemailer to send emails.

In this blog post, we will discuss what this error means, why it has occurred, and how to fix it. We will also provide a step-by-step guide to setting up Nodemailer with your Gmail account, so that you can start sending emails again.

## What is the Error?

When you try to send emails with Nodemailer, you may receive the following error message:

```
Error: Invalid login: 535-5.7.8 Username and Password not accepted.
```

This error occurs because Google has disabled the "Less Secure App" option, which was previously used to authorize Nodemailer to send emails.

## Why Has Google Disabled the "Less Secure App" Option?

Google has disabled the "Less Secure App" option because it was found to be vulnerable to malicious attacks. By disabling this option, Google is making it more difficult for malicious actors to gain access to user accounts.

## How to Fix the Error and Set up Nodemailer

Fortunately, there is a way to fix this error and set up Nodemailer to send emails using your Gmail account. The first step is to create a Google project and enable the Gmail API.

1. Go to the [Google Developer Console](https://console.developers.google.com/) and create a new project.
2. Select the project and go to the **APIs & Services** tab.
3. Search for the **Gmail API** and enable it.

Once you have enabled the Gmail API, you will need to create credentials for your project.

1. Go to the **Credentials** tab and click on the **Create credentials** button.
2. Select **OAuth Client ID** from the dropdown menu.
3. Select **Web application** as the application type.
4. Enter a name for your credentials and click on the **Create** button.
5. Enter the URL of your application in the **Authorized redirect URIs** field and click on the **Create** button.

Once you have created the credentials, you will need to generate an access token.

1. Go to the **OAuth consent screen** tab and enter a product name.
2. Select the **User Type** as **External** and click on the **Save** button.
3. Go to the **Credentials** tab and click on the **Download JSON** button.
4. Copy the **client_secret** from the JSON file and paste it into the **clientSecret** field in the **index.js** file.
5. Run the **index.js** file and follow the instructions to generate an access token.

Once you have generated the access token, you can use it to set up Nodemailer.

1. Open the **index.js** file and add the following code:

```javascript
const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    type: 'OAuth2',
    user: '<your-email-address>',
    clientId: '<your-client-id>',
    clientSecret: '<your-client-secret>',
    accessToken: '<your-access-token>',
    refreshToken: '<your-refresh-token>',
  },
});
```

2. Replace the `<your-email-address>`, `<your-client-id>`, `<your-client-secret>`, `<your-access-token>`, and `<your-refresh-token>` placeholders with the appropriate values.

3. Add the following code to send an email:

```javascript
const mailOptions = {
  from: '<your-email-address>',
  to: '<recipient-email-address>',
  subject: 'Test Email',
  text: 'This is a test email sent with Nodemailer.',
};

transporter.sendMail(mailOptions, (error, info) => {
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
```

4. Replace the `<your-email-address>` and `<recipient-email-address>` placeholders with the appropriate values.

5. Run the **index.js** file and check your inbox to see if the email was sent successfully.

## Conclusion

In this blog post, we discussed the error that occurs when Google disables the "Less Secure App" option and how to fix it. We provided a step-by-step guide to setting up Nodemailer with your Gmail account and sending emails using the Gmail API.

We hope that this blog post has been helpful and that you are now able to send emails using Nodemailer and your Gmail account. If you have any questions or comments, please feel free to leave them in the comments section below.
### Recommended Sites

- [Send Email with Nodemailer After Google Disables Less Secure App Option](https://www.nodemailer.com/usage/using-gmail/)
- [Gmail Less Secure App Access](https://support.google.com/accounts/answer/6010255)
- [Gmail SMTP Configuration](https://support.google.com/a/answer/176600?hl=en)
- [Using OAuth2 for Gmail API Access](https://developers.google.com/identity/protocols/oauth2/scopes#gmail)