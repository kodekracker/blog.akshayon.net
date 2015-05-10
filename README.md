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
  
3. To publish content to gh-pages
  ```shell
    $ fab publish_github
    OR
    $ fab publish_github:publish_drafts=False,dns=False
  ```
  **Note:** 
  * To publish drafts also, put `publish_drafts=True `
  * To host github pages on custom pages, put `dns='ip-address'`
