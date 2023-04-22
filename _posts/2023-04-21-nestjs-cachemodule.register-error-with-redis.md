---
layout: post
title: "NestJS CacheModule.register Error with Redis"
tags: ['redis', 'nestjs']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

NestJS is a modern and progressive Node.js web framework. It provides a powerful set of tools and features that enable developers to quickly and easily create robust and scalable applications. One of the most powerful features of NestJS is its caching capabilities. NestJS provides a CacheModule, which allows developers to easily cache data and improve the performance of their applications.

However, when using the CacheModule with Redis, developers may encounter errors. In this article, we'll explore some of the most common errors that developers encounter when using the CacheModule with Redis and how to fix them.

## Common Errors

When using the CacheModule with Redis, developers may encounter the following errors:

### Error 1: Redis connection refused

The most common error when using the CacheModule with Redis is the “Redis connection refused” error. This error occurs when the Redis server is not running or is not accessible. To fix this error, you need to make sure that the Redis server is running and is accessible from the application.

### Error 2: Redis authentication failed

Another common error when using the CacheModule with Redis is the “Redis authentication failed” error. This error occurs when the Redis server is not configured to accept connections from the application. To fix this error, you need to make sure that the Redis server is configured to accept connections from the application.

## Registering the CacheModule

Once you have ensured that the Redis server is running and is accessible from the application, you can register the CacheModule in your NestJS application. To do this, you need to add the following code to your main.ts file:

```typescript
import { Module } from '@nestjs/common';
import { CacheModule } from '@nestjs/common';

@Module({
  imports: [
    CacheModule.register({
      store: 'redis',
      host: 'localhost',
      port: 6379,
    }),
  ],
})
export class AppModule {}
```

In the above code, we are registering the CacheModule with Redis as the store. We also specify the host and port of the Redis server. This will allow the CacheModule to connect to the Redis server and store and retrieve data from it.

## Using the CacheModule

Once the CacheModule is registered, you can use it in your NestJS application. To store data in the cache, you can use the `set()` method. For example, you can use the following code to store a value in the cache:

```typescript
import { Injectable } from '@nestjs/common';
import { CacheService } from '@nestjs/common';

@Injectable()
export class MyService {
  constructor(private readonly cacheService: CacheService) {}

  async storeData(key: string, value: any) {
    await this.cacheService.set(key, value);
  }
}
```

In the above code, we are using the `set()` method of the CacheService to store a value in the cache.

To retrieve data from the cache, you can use the `get()` method. For example, you can use the following code to retrieve a value from the cache:

```typescript
import { Injectable } from '@nestjs/common';
import { CacheService } from '@nestjs/common';

@Injectable()
export class MyService {
  constructor(private readonly cacheService: CacheService) {}

  async getData(key: string) {
    return await this.cacheService.get(key);
  }
}
```

In the above code, we are using the `get()` method of the CacheService to retrieve a value from the cache.

## Conclusion

In this article, we explored some of the common errors that developers encounter when using the CacheModule with Redis and how to fix them. We also looked at how to register the CacheModule and how to use it to store and retrieve data from the cache.

If you have been running a NestJS application with Redis as your caching solution, you may have encountered the error `CacheModule.register is not a function`. This error is caused by an incorrect version of the `@nestjs/common` package being installed. In this blog post, we'll go over the steps to resolve this issue.

## What is the issue?

The issue is caused by an outdated version of the `@nestjs/common` package. To use Redis with NestJS, you must have version 6.0.0 or higher of the `@nestjs/common` package installed. If you have an older version, you will get the `CacheModule.register is not a function` error.

## How to resolve the issue

The first step is to check the version of the `@nestjs/common` package that is installed in your project. To do this, open the `package.json` file in the root of your project and check the version of the `@nestjs/common` package. If it is an older version than 6.0.0, you will need to update it.

The next step is to update the version of the `@nestjs/common` package. To do this, open the terminal and run the following command:

```
npm install @nestjs/common@latest
```

This will install the latest version of the `@nestjs/common` package in your project. Once the package is installed, you can check the version of the package in the `package.json` file.

## Conclusion

If you are getting the `CacheModule.register is not a function` error when using Redis with NestJS, it is likely due to an outdated version of the `@nestjs/common` package. To resolve the issue, you must update the version of the `@nestjs/common` package to 6.0.0 or higher. To do this, you can run the `npm install @nestjs/common@latest` command in the terminal. Once the package is updated, you should not see the error anymore.
# Recommended sites
- [NestJS CacheModule.register Error with Redis](https://github.com/nestjs/nest/issues/1458)
- [NestJS CacheModule](https://docs.nestjs.com/techniques/caching#cachemodule-api)
- [Redis Cache Module](https://github.com/nestjs-community/cache-module)
- [NestJS Redis Module](https://github.com/nestjs-community/redis-module)