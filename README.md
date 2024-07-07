ModerSite
---------

Proof of concept for a site that uses some technologies I want to learn.

### Technologies

https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/client-server-architectures/

## Frontend

- [X] [SCSS](https://sass-lang.com/): Bootstrap uses SCSS
- [X] [pnpm](https://pnpm.io/): easy to use, most efficient than npm and yarn
- [X] [Bootstrap](https://getbootstrap.com/): the only CSS framework with a Django package
- [ ] [TypeScript](https://www.typescriptlang.org/)
- [ ] [Dark Mode](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)
- [X] [Webpack](https://webpack.js.org/)
- [ ] [Htmx](https://htmx.org/)
- [ ] [AlpineJS](https://alpinejs.dev/)
- [ ] [Node.js](https://nodejs.org/): used by webpack

### Excluded
- [X] [Vite](https://vitejs.dev/): created SPA
- [X] [Material-UI](https://material-ui.com/): no Django package
- [X] [TailwindCSS](https://tailwindcss.com/): no Django package
- [X] [npm](https://www.npmjs.com/): replaced by pnpm
- [X] [yarn](https://yarnpkg.com/): replaced by pnpm
- [ ] [React](https://react.dev/)

## Backend

- [X] [Django](https://www.djangoproject.com/)
- [X] [Django-pipeline](https://django-pipeline.readthedocs.io/en/stable/)
- [ ] [Django Rest Framework](https://www.django-rest-framework.org/)
- [ ] [Django debug toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/)
- [ ] [Django Channels](https://channels.readthedocs.io/en/stable/)
- [ ] [Gunicorn](https://gunicorn.org/)
- [ ] [Hypercorn](https://hypercorn.readthedocs.io/en/stable/)
- [X] [Poetry](https://python-poetry.org/)
- [ ] [Celery](https://docs.celeryproject.org/en/stable/)
- [X] [Python3.12](https://www.python.org/)
- [ ] [Django-allauth](https://django-allauth.readthedocs.io/en/latest/)
- [ ] [DjangoCookieConsent](https://django-cookie-consent.readthedocs.io/en/latest/)
- [ ] alert messages when the site is offline
- [ ] wait for the database to be ready

## HTML and web server

- [ ] [Nginx](https://www.nginx.com/)
- [ ] [Apache](https://httpd.apache.org/)
- [ ] [HTTP/2](https://http2.github.io/)
- [ ] [Mozilla observatory](https://observatory.mozilla.org/)
- [ ] [OpenGraph meta tags](https://ogp.me/)
- [ ] [Performances](https://web.dev/)
- [ ] [Generate a favicon](https://favicon.io/favicon-generator/)
- [ ] [Favicon validation](https://realfavicongenerator.net/favicon_checker)
- [ ] [HTML validation](https://html5.validator.nu/)
- [X] [OpenGraph validation](https://www.opengraph.xyz/)
- [ ] [Structured data validation](https://search.google.com/structured-data/testing-tool)
- [ ] [Webhint](https://webhint.io/)
- [ ] [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [ ] [SSL validation](https://www.ssllabs.com/ssltest/)
- [ ] [XML site map](https://www.xml-sitemaps.com/)
HTML Checker, CSS Validator, Link Checker, JS Validator

## DevOps

- [X] [git](https://git-scm.com/)
- [X] [Precommit](https://pre-commit.com/)
- [X] [Docker](https://www.docker.com/)
- [X] [Docker Compose](https://docs.docker.com/compose/)
- [ ] [SonarQube](https://www.sonarqube.org/)
- [ ] [Pytest](https://docs.pytest.org/en/stable/)
- [ ] [Jest](https://jestjs.io/)
- [X] [editorconfig](https://editorconfig.org/)
- [ ] Copyright checking

## Code analysis and formatting

- [ ] Dockerfile
- [ ] HTML
- [X] ini
- [ ] JavaScript:  [ESlint](https://eslint.org/)
- [X] JSON
- [ ] Markdown
- [X] Python: [Ruff](https://docs.astral.sh/ruff/)
- [ ] SCSS [StyleLint](https://stylelint.io/)
- [X] TOML
- [ ] TypeScript:  [ESlint](https://eslint.org/)
- [X] YAML

### Excluded tools

- [X] [JSHint](https://jshint.com/): replaced by ESLint
- [X] [JSLint](https://www.jslint.com/): replaced by ESLint
- [X] [JSCS](https://jscs.dev/): replaced by ESLint and limited to code style
- [X] [Pylint](https://pylint.pycqa.org/): replaced by Ruff
- [X] [Flake8](https://flake8.pycqa.org/en/latest/): replaced by Ruff
- [X] [Black](https://black.readthedocs.io/en/stable/): replaced by Ruff
- [X] [isort](https://pycqa.github.io/isort/): replaced by Ruff
- [X] [PyDocStyle](https://www.pydocstyle.org/en/stable/): replaced by Ruff
- [X] [PyUpgrade](https://pypi.org/project/pyupgrade/): replaced by Ruff
- [X] [Autoflake](https://pypi.org/project/autoflake/): replaced by Ruff
- [X] [SassLint](https://www.npmjs.com/package/sass-lint): no longer maintained

## Database and storage

- [X] [PostgreSQL](https://www.postgresql.org/)
- [X] [Redis](https://redis.io/)
- [X] [minio](https://min.io/)
