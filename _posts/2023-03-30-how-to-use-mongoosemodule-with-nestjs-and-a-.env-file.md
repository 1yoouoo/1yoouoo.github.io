---
layout: post
title: "How to Use MongooseModule with Nestjs and a .env File"
tags: ['mongoose', 'environment-variables', 'nestjs', 'config']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

Using MongooseModule with Nestjs and a .env file is a great way to keep your configuration settings secure and organized. MongooseModule is a popular object modeling library for MongoDB and Nestjs is a progressive Node.js framework for building efficient and scalable server-side applications. The .env file allows you to store environment variables in a secure and organized way.

In this tutorial, we will show you how to use MongooseModule with Nestjs and a .env file. We will also provide some examples that you can use to help you understand the concepts better.

## What is MongooseModule?

MongooseModule is an object modeling library for MongoDB. It provides a simple and straightforward way to represent and store data in MongoDB. It also provides an easy way to access and manipulate the data.

MongooseModule provides a schema-based solution for modeling your application data. It also provides a powerful query builder that allows you to easily query your data.

## What is Nestjs?

Nestjs is a progressive Node.js framework for building efficient and scalable server-side applications. It is built on top of Express.js and uses TypeScript to provide a strongly-typed and object-oriented programming environment.

Nestjs provides a powerful dependency injection system that helps you to easily inject services and components into your application. It also provides a modular structure for organizing your application code.

## What is a .env File?

A .env file is a text file that stores environment variables. It is used to keep configuration settings secure and organized. It is commonly used in web applications to store database credentials, API keys, and other sensitive information.

## Setting up MongooseModule with Nestjs

To use MongooseModule with Nestjs, you first need to install the MongooseModule package. You can do this using the following command:

```
$ npm install @nestjs/mongoose
```

Once the package is installed, you need to create a MongooseModule instance. You can do this in your main.ts file, like so:

```typescript
import { MongooseModule } from '@nestjs/mongoose';

@Module({
  imports: [
    MongooseModule.forRoot('mongodb://localhost:27017/my_db'),
  ],
})
export class AppModule {}
```

In the code above, we are creating a MongooseModule instance and providing the MongoDB connection string.

## Setting up a .env File

To use a .env file with Nestjs, you first need to create a .env file in the root of your project. You can do this using a text editor or the command line.

Once the .env file is created, you can add your environment variables to it. For example, you can add your MongoDB connection string like so:

```
MONGODB_CONNECTION_STRING=mongodb://localhost:27017/my_db
```

## Using a .env File with MongooseModule

Now that you have your .env file set up, you can use it with MongooseModule. To do this, you need to use the `.forRoot()` method, like so:

```typescript
import { MongooseModule } from '@nestjs/mongoose';

@Module({
  imports: [
    MongooseModule.forRoot(process.env.MONGODB_CONNECTION_STRING),
  ],
})
export class AppModule {}
```

In the code above, we are using the `process.env` object to access the MongoDB connection string stored in the .env file.

## Conclusion

In this tutorial, we showed you how to use MongooseModule with Nestjs and a .env file. We discussed what MongooseModule and Nestjs are and how to use them together. We also discussed what a .env file is and how to set it up. Finally, we showed you how to use the .env file with MongooseModule.

Nestjs is a popular framework for creating Node.js applications. It is a great way to quickly get up and running with a Node.js application. However, when it comes to connecting to a MongoDB database, you may run into some issues. This tutorial will show you how to use the MongooseModule with Nestjs and a .env file.

## What is Mongoose?

Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js. It is designed to work in an asynchronous environment. Mongoose provides a straight-forward, schema-based solution to model your application data. It includes built-in type casting, validation, query building, business logic hooks and more, out of the box.

## What is a .env file?

A .env file is a plain text file that contains environment variables. Environment variables are key-value pairs that are used to store and retrieve configuration settings for your application. They are typically used to store sensitive information such as passwords, API keys, and other secrets.

## Setting up the MongooseModule

The first step is to install the MongooseModule. To do this, open a terminal window and run the following command:

```
npm install @nestjs/mongoose
```

Once the module is installed, you need to configure it. To do this, open the `app.module.ts` file and add the following code:

```typescript
import { MongooseModule } from '@nestjs/mongoose';

@Module({
  imports: [
    MongooseModule.forRoot(process.env.MONGO_URI),
  ],
})
export class AppModule {}
```

The `forRoot()` method takes a URI as an argument. This URI is used to connect to the MongoDB database. The URI is stored in an environment variable called `MONGO_URI`. This environment variable should not be stored in the code. Instead, it should be stored in a .env file.

## Creating a .env file

The next step is to create a .env file. To do this, open a terminal window and run the following command:

```
touch .env
```

This will create a file called `.env` in the root directory of your project. Open this file and add the following line:

```
MONGO_URI=<your_mongo_uri>
```

Replace `<your_mongo_uri>` with the URI to your MongoDB database. This URI should be in the following format:

```
mongodb://<username>:<password>@<host>:<port>/<database>
```

Once you have added the URI, save the file.

## Adding the .env file to the project

The last step is to add the .env file to the project. To do this, open the `.gitignore` file and add the following line:

```
.env
```

This will prevent the .env file from being committed to the Git repository.

## Conclusion

In this tutorial, you learned how to use the MongooseModule with Nestjs and a .env file. You learned how to install the MongooseModule and configure it to connect to a MongoDB database. You also learned how to create a .env file and add it to the project. With this knowledge, you should be able to get up and running with a Node.js application quickly and easily.
## Recommended Sites

- [Using MongooseModule with Nestjs and .env File](https://docs.nestjs.com/techniques/mongodb#using-mongoosemodule-with-nestjs-and-env-file)
- [Using Mongoose with Nest.js](https://www.npmjs.com/package/@nestjs/mongoose)
- [How to use Mongoose with Nest.js](https://blog.bitsrc.io/how-to-use-mongoose-with-nest-js-9b9f7d9f1b1b)
- [Using .env files with Nest.js](https://docs.nestjs.com/techniques/configuration#using-env-files-with-nestjs)