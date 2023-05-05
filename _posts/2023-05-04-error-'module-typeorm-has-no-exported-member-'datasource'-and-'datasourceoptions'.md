---
layout: post
title: "Error 'Module typeorm has no exported member 'DataSource' and 'DataSourceOptions'"
tags: ['node.js', 'npm', 'nestjs', 'typeorm']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

The `Module "typeorm" has no exported member 'DataSource' and 'DataSourceOptions'` error is a common issue encountered by developers when working with the [TypeORM](https://github.com/typeorm/typeorm) library. This error usually occurs when the TypeORM library is not properly configured or when the code is not written correctly. In this article, we will discuss how to troubleshoot this error and how to avoid it in the future.

## What is TypeORM?

TypeORM is an open-source Object-Relational Mapping (ORM) library for TypeScript and JavaScript. It is designed to help developers work with databases in a more efficient and organized way. TypeORM provides a powerful and easy-to-use API that allows developers to interact with databases without having to write complex SQL queries.

## What is the 'Module "typeorm" has no exported member 'DataSource' and 'DataSourceOptions' Error?

The `Module "typeorm" has no exported member 'DataSource' and 'DataSourceOptions'` error is a common issue encountered by developers when using the TypeORM library. This error occurs when the TypeORM library is not properly configured or when the code is not written correctly.

## Common Mistakes

There are several common mistakes that can lead to the `Module "typeorm" has no exported member 'DataSource' and 'DataSourceOptions'` error. The most common mistakes are:

- Not importing the `DataSource` and `DataSourceOptions` modules from the TypeORM library.
- Not installing the TypeORM library correctly.
- Not specifying the correct database configuration in the `DataSourceOptions` object.

## Example Code

To illustrate how to troubleshoot this error, let's look at an example of code that could cause this error.

```typescript
import { createConnection } from 'typeorm';

const connection = createConnection();
```

In this example, we are trying to create a connection to a database using the `createConnection()` method from the TypeORM library. However, since we have not imported the `DataSource` and `DataSourceOptions` modules, the TypeORM library will not be able to create the connection and will throw the `Module "typeorm" has no exported member 'DataSource' and 'DataSourceOptions'` error.

## Solution

To fix this error, we need to first make sure that the TypeORM library is installed correctly. We can do this by running the `npm install typeorm` command.

Once the TypeORM library is installed, we need to import the `DataSource` and `DataSourceOptions` modules. We can do this by adding the following code to our file:

```typescript
import { createConnection, DataSource, DataSourceOptions } from 'typeorm';
```

Finally, we need to specify the database configuration in the `DataSourceOptions` object. We can do this by adding the following code to our file:

```typescript
const options: DataSourceOptions = {
  type: 'postgres',
  host: 'localhost',
  port: 5432,
  username: 'postgres',
  password: 'postgres',
  database: 'my_database',
};
```

Once these changes are made, we can now create a connection to the database using the `createConnection()` method and the `DataSourceOptions` object.

## Conclusion

The `Module "typeorm" has no exported member 'DataSource' and 'DataSourceOptions'` error is a common issue encountered by developers when using the TypeORM library. This error usually occurs when the TypeORM library is not properly configured or when the code is not written correctly. To fix this error, we need to make sure that the TypeORM library is installed correctly, import the `DataSource` and `DataSourceOptions` modules, and specify the database configuration in the `DataSourceOptions` object. By following these steps, we should be able to resolve this error and avoid it in the future.
If you are trying to use the TypeORM library in your project and you encounter the error 'Module "typeorm" has no exported member 'DataSource' and 'DataSourceOptions', then you are in the right place. This error is usually caused by an incorrect version of TypeORM being used in the project. In this blog post, we will discuss how to resolve this error.

## What is TypeORM?
TypeORM is an open-source object-relational mapping (ORM) library for TypeScript and JavaScript. It provides an easy way to map objects to relational databases and provides powerful features such as data validation, relationship mapping, and database migrations.

## What is causing the error?
The error 'Module "typeorm" has no exported member 'DataSource' and 'DataSourceOptions' is usually caused by an incorrect version of TypeORM being used in the project. This error occurs when you are trying to use a version of TypeORM that does not have the DataSource and DataSourceOptions modules.

## How to resolve the error?
The first step to resolving this error is to make sure you are using the correct version of TypeORM. You can do this by checking the version of TypeORM in your package.json file. If you are using an older version of TypeORM, you should update it to the latest version.

Once you have updated to the latest version of TypeORM, you can then install the DataSource and DataSourceOptions modules. To do this, you can run the following command in your terminal:

```
npm install typeorm-datasource
```

Once the DataSource and DataSourceOptions modules have been installed, you can then import them into your project. To do this, you can use the following code:

```javascript
import { DataSource, DataSourceOptions } from 'typeorm';
```

Once the DataSource and DataSourceOptions modules have been imported into your project, you can then use them to configure your TypeORM connection. To do this, you can use the following code:

```javascript
const dataSourceOptions: DataSourceOptions = {
  type: 'mysql',
  host: 'localhost',
  port: 3306,
  username: 'root',
  password: 'password',
  database: 'mydatabase'
};

const dataSource = new DataSource(dataSourceOptions);
```

Once you have configured your TypeORM connection, you can then use it to connect to your database. To do this, you can use the following code:

```javascript
await dataSource.connect();
```

## Conclusion
In this blog post, we discussed how to resolve the error 'Module "typeorm" has no exported member 'DataSource' and 'DataSourceOptions'. We discussed what TypeORM is and how to make sure you are using the correct version of TypeORM. We then discussed how to install the DataSource and DataSourceOptions modules and how to configure your TypeORM connection. Finally, we discussed how to use your configured connection to connect to your database.
## Recommended Sites

- [TypeORM Documentation - DataSourceOptions](http://typeorm.io/#/connection-options/datasourceoptions)
- [TypeORM GitHub Issue #6691](https://github.com/typeorm/typeorm/issues/6691)
- [Stack Overflow - Error: Module typeorm has no exported member DataSource and DataSourceOptions](https://stackoverflow.com/questions/62226999/error-module-typeorm-has-no-exported-member-datasource-and-datasourceoptions)