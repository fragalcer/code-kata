# syntax=docker/dockerfile:1

FROM node:17
ENV NODE_ENV=development

COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

WORKDIR /app

# install 'nodemon' package for hot reloading the app:
RUN npm install -g nodemon

RUN npm install --quiet

COPY . /app
ENV PATH /app/frontend/node_modules/.bin:$PATH

# Execute the command to run development server of vue/cli using 'nodemon', after specify the files to track and to
# watch only, in my case only want 'src' file of vue application to watch, and track changes in files with:
# .js, .css and .vue extension.
CMD ["nodemon", "--ext", "js,css,vue.html", "--watch src", "--exec", "npm", "run", "serve" ]
