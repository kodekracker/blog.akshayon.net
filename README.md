# kodekracker.github.io
My Personal Portfolio and Blog Website

## Instructions
1. To create new post
  ```shell
    $ fab new_post:"Title of the post"
  ```

2. To run live reload 
  ```shell
    $ fab live_build
  ```
  
3. To push content to gh-pages
  ```shell
    $ fab push
    OR
    $ fab push:publish_drafts=False,dns=False
  ```
