blog.akshayon.net
==========================
This is my blog, which is developed using *[pelican](http://blog.getpelican.com/)* blog-generator.This blog is hosted on sub-domain named as [http://blog.akshayon.net](http://blog.akshayon.net).

## Environment Variables
1. `PELICAN_PLUGINS_PATH`
1. `TWITTER_WIDGET_ID`
1. `DISQUS_SITENAME`
1. `GITHUB_GOOGLE_ANALYTICS`

## Instructions
1. To create new post
  ```shell
    $ fab new_post:"Title of the post"
  ```

2. To run live reload
  ```shell
    $ fab live_serve
  ```

3. To publish content to gh-pages
  ```shell
    $ fab publish_github
    OR
    $ fab publish_github:publish_drafts=False
  ```
  **Note:**
  * To publish drafts also, put `publish_drafts=True `
