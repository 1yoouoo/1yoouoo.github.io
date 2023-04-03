---
layout: post
title: "Fixing the It looks like you're trying to use TypeScript but don't have the required dependencies installed Error in Expo"
tags: ['javascript', 'typescript', 'react-native', 'dependencies', 'expo']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

If you're a React Native developer, you've probably encountered the dreaded “It looks like you're trying to use TypeScript but don't have the required dependencies installed” error. This error can be especially frustrating because it's not always clear what the cause of the error is or how to fix it. Fortunately, there are a few simple steps you can take to get your project back up and running.

The first step is to make sure that you have the correct version of TypeScript installed. If you're using Expo, you'll need to make sure that you have the latest version of TypeScript installed. To do this, open your terminal and run the following command:

```
npm install -g typescript
```

Once you have the latest version of TypeScript installed, you'll need to make sure that your project is using the correct version of TypeScript. To do this, open your project's package.json file and make sure that the typescript version is set to the latest version.

```
"dependencies": {
  "typescript": "^3.9.7"
}
```

If your package.json file doesn't have the correct version of TypeScript, you'll need to update it. To do this, run the following command in your terminal:

```
npm install --save-dev typescript@latest
```

Once you have the correct version of TypeScript installed and your package.json file is updated, you'll need to make sure that your project is using the correct version of TypeScript. To do this, open your project's tsconfig.json file and make sure that the typescript version is set to the correct version.

```
{
  "compilerOptions": {
    "target": "esnext",
    "module": "esnext",
    "lib": ["esnext"],
    "jsx": "react",
    "typeRoots": ["node_modules/@types"],
    "types": ["typescript"],
    "moduleResolution": "node",
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noImplicitThis": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "allowJs": true,
    "sourceMap": true,
    "noEmit": true,
    "baseUrl": ".",
    "typeRoots": [
      "./node_modules/@types"
    ],
    "types": [
      "typescript"
    ],
    "target": "es5"
  }
}
```

If your tsconfig.json file doesn't have the correct version of TypeScript, you'll need to update it. To do this, run the following command in your terminal:

```
tsc --init
```

Once you've updated your package.json and tsconfig.json files, you should be able to run your project without encountering the “It looks like you're trying to use TypeScript but don't have the required dependencies installed” error. If you're still encountering the error, make sure that you have the correct version of TypeScript installed and that your package.json and tsconfig.json files are updated.

If you are a React Native developer, chances are you have encountered the dreaded `It looks like you're trying to use TypeScript but don't have the required dependencies installed` error when trying to use TypeScript in your Expo project. This error can be incredibly frustrating, as it can prevent you from running your project and cause a lot of confusion.

Fortunately, this error is relatively easy to fix. In this blog post, we will go over the steps needed to resolve this error and get your project up and running again.

## Step 1: Install the TypeScript Dependency

The first step is to install the TypeScript dependency in your project. You can do this by running the following command in your terminal:

```
npm install --save-dev typescript
```

This command will install the TypeScript dependency in your project. Once the installation is complete, you can move on to the next step.

## Step 2: Create a TypeScript Configuration File

The next step is to create a TypeScript configuration file in your project. This file will contain all the necessary information for TypeScript to work correctly. To create the configuration file, run the following command in your terminal:

```
tsc --init
```

This command will create a `tsconfig.json` file in your project. This file will contain all the necessary information for TypeScript to work correctly.

## Step 3: Install the TypeScript Babel Plugin

The next step is to install the TypeScript Babel plugin. This plugin is necessary for TypeScript to work correctly with Babel. To install the plugin, run the following command in your terminal:

```
npm install --save-dev @babel/plugin-transform-typescript
```

Once the plugin is installed, you can move on to the next step.

## Step 4: Configure the Babel Plugin

The next step is to configure the Babel plugin so that it can work with TypeScript. To do this, open the `babel.config.js` file in your project and add the following code:

```
module.exports = {
  plugins: [
    [
      '@babel/plugin-transform-typescript',
      {
        allowNamespaces: true
      }
    ]
  ]
};
```

This code will configure the Babel plugin so that it can work with TypeScript. Once the configuration is complete, you can move on to the next step.

## Step 5: Install the TypeScript ESLint Plugin

The next step is to install the TypeScript ESLint plugin. This plugin is necessary for TypeScript to work correctly with ESLint. To install the plugin, run the following command in your terminal:

```
npm install --save-dev @typescript-eslint/parser
```

Once the plugin is installed, you can move on to the next step.

## Step 6: Configure the ESLint Plugin

The next step is to configure the ESLint plugin so that it can work with TypeScript. To do this, open the `.eslintrc.js` file in your project and add the following code:

```
module.exports = {
  parser: '@typescript-eslint/parser',
  extends: ['plugin:@typescript-eslint/recommended'],
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module'
  },
  rules: {
    // Place to specify ESLint rules. Can be used to overwrite rules specified from the extended configs
    // e.g. "@typescript-eslint/explicit-function-return-type": "off",
  }
};
```

This code will configure the ESLint plugin so that it can work with TypeScript. Once the configuration is complete, you can move on to the next step.

## Step 7: Install the TypeScript Prettier Plugin

The next step is to install the TypeScript Prettier plugin. This plugin is necessary for TypeScript to work correctly with Prettier. To install the plugin, run the following command in your terminal:

```
npm install --save-dev prettier-plugin-typescript
```

Once the plugin is installed, you can move on to the next step.

## Step 8: Configure the Prettier Plugin

The last step is to configure the Prettier plugin so that it can work with TypeScript. To do this, open the `.prettierrc` file in your project and add the following code:

```
{
  "plugins": ["prettier-plugin-typescript"]
}
```

This code will configure the Prettier plugin so that it can work with TypeScript. Once the configuration is complete, you can save the file and you should now be able to run your project without any errors.

## Conclusion

In this blog post, we have gone over the steps needed to fix the `It looks like you're trying to use TypeScript but don't have the required dependencies installed` error in Expo. We have gone over how to install the TypeScript dependency, create a TypeScript configuration file, install the TypeScript Babel plugin, configure the Babel plugin, install the TypeScript ESLint plugin, configure the ESLint plugin, install the TypeScript Prettier plugin, and configure the Prettier plugin.

Following these steps should help you resolve the error and get your project up and running again. If you have any questions or comments, please feel free to leave them in the comments section below.
## Recommended Sites

- [Expo Documentation: Using TypeScript](https://docs.expo.io/guides/typescript/)
- [Expo Community Tutorial: Using TypeScript with Expo](https://docs.expo.io/tutorial/typescript/)
- [Expo TypeScript Support](https://docs.expo.io/versions/latest/guides/typescript/)
- [GitHub: TypeScript Support in Expo](https://github.com/expo/expo/blob/master/docs/pages/versions/unversioned/guides/typescript.md)