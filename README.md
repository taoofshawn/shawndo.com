# shawndo.com hugo blog

- [converted](https://gohugo.io/tools/migrations/) from wordpress
- completely rebuilt the old wordpress theme into a minimal, basic css-only theme. the original theme was a modified from the [Integrati](https://wordpress.org/themes/integrati/) wordpress theme
- learned css on the fly from youtube videos. mainly:
    - [CSS Tutorial](https://youtu.be/OXGznpKZ_sA)
    - [Kevin Powell](https://www.youtube.com/@KevinPowell)

- git action for building and pushing the container image. for some reason I had a difficult time finding these steps in one place
    - setup a [classic personal access token](https://github.com/settings/tokens)
        - give permission `write:packages`
    - add to repository secrets (repo > settings > secrets and variables > actions > new repository secret)
        - named `GHCR_TOKEN` to match the .github/workflows/docker-image.yml in this repository

```bash
```
