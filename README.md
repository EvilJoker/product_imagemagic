This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.

# 核心概念
+ react : 前端ui 框架

+ next ： 基于 react 的框架，使用 React 组件来构建用户界面，并使用 Next.js 来构建其他功能和优化。
https://nextjs.org/docs/app/building-your-application/routing/defining-routes

+ chrom/edge 插件： 基于 chrouim , manifest.json 是配置文件。一个厉害的静态网页框架，在后台，Next.js 还抽象并自动配置 React 所需的工具，例如捆绑、编译等。这使您可以专注于构建应用程序，而不是花时间进行配置。



+ next 核心功能的概念
> + 路由： 调用URL的能力，静态路由（写死），动态路由（根据数据加载），api 路由 (调用第三方接口)
>  https://nextjs.org/docs/app/building-your-application/routing/defining-routes
> + 数据获取：数据访问
> 
> + 渲染模式： 客户端生成 html 还是 服务端生成html
> 
> + 缓存 ： 保存数据，提供西能
> 
> + css : 样式
> + 资产： public, 图片、第三库的管理
> + 配置： ts, src, 环境变量
> + 部署：静态导出：

+ 静态站点（纯客户端）： 基于浏览器的内置 nodejs客户端。不和服务端打交道 


# 关于本项目

+ 主要使用 next.js 的[静态导出功能](https://nextjs.org/docs/app/building-your-application/deploying/static-exports)
>  next.config.js  ---> output: 'export'。
> npx serve out 查看静态页面

+ 给 chrome /edge 写插件



# 项目结构介绍
+ next 项目结构
> https://nextjs.org/docs/getting-started/project-structure
+ 有src 的项目结构（本项目）https://nextjs.org/docs/app/building-your-application/configuring/src-directory






# FAQ


+ 创建一个项目？ https://react.dev/learn/start-a-new-react-project
> npx create-next-app@latest

+ 启动和调试？ https://nextjs.org/learn-pages-router/basics/create-nextjs-app/setup
> 启动 npm run dev


+ 开发 chrome 插件介绍 ： https://juejin.cn/post/7179581995259789372?searchId=202312011349350FDFC8B1E8F66668C337

+ next.js 开发 chrome 插件 ：https://github.com/ibnzUK/next-chrome-starter

+ next 项目结构介绍： https://nextjs.org/docs/getting-started/project-structure

+ next starter 模板： https://vercel.com/templates/next.js

+ react + next 项目实践 ：https://juejin.cn/post/7194410416879960125?searchId=202312011354577556C1BBC6944A6A5E9A