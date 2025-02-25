////////////////////////////////
// Setup
////////////////////////////////

// Gulp and package
const { src, dest, parallel, series, watch } = require('gulp');
const pjson = require('/app/package.json');

// Plugins
const autoprefixer = require('autoprefixer');
const browserSync = require('browser-sync').create();
const cssnano = require('cssnano');
const pixrem = require('pixrem');
const plumber = require('gulp-plumber');
const postcss = require('gulp-postcss');
const reload = browserSync.reload;
const rename = require('gulp-rename');
const sass = require('gulp-sass')(require('sass'));
const uglify = require('gulp-uglify-es').default;

// Relative paths function
function pathsConfig(appName) {
  this.app = '/app/app';

  return {
    app: this.app,
    templates: `${this.app}/templates`,
    css: `${this.app}/static/css`,
    sass: `${this.app}/static/sass`,
    fonts: `${this.app}/static/fonts`,
    images: `${this.app}/static/images`,
    js: `${this.app}/static/js`,
  };
}

const paths = pathsConfig();

////////////////////////////////
// Tasks
////////////////////////////////

// Styles autoprefixing and minification
const processCss = [
  autoprefixer(), // adds vendor prefixes
  pixrem(), // add fallbacks for rem units
];

const minifyCss = [
  cssnano({ preset: 'default' }), // minify result
];

function project_styles() {
  return src(`${paths.sass}/project.scss`)
    .pipe(
      sass({
        silenceDeprecations: [
          'legacy-js-api',
          'mixed-decls',
          'color-functions',
          'global-builtin',
          'import',
        ],
        includePaths: [paths.sass],
      }).on('error', sass.logError),
    )
    .pipe(plumber()) // Checks for errors
    .pipe(postcss(processCss))
    .pipe(dest(paths.css))
    .pipe(rename({ suffix: '.min' }))
    .pipe(postcss(minifyCss)) // Minifies the result
    .pipe(dest(paths.css));
}

// Javascript minification
function scripts() {
  return src([`${paths.js}/project.js`, `${paths.js}/*-page.js`])
    .pipe(plumber()) // Checks for errors
    .pipe(uglify()) // Minifies the js
    .pipe(rename({ suffix: '.min' }))
    .pipe(dest(paths.js));
}

// Browser sync server for live reload
function initBrowserSync() {
  console.log(`Listening at: ${process.env.APP_SERVER_HOST}`);
  browserSync.init(
    [`${paths.css}/*.css`, `${paths.js}/*.js`, `${paths.templates}/*.html`],
    {
      // https://www.browsersync.io/docs/options/#option-open
      // Disable as it doesn't work from inside a container
      open: false,
      // https://www.browsersync.io/docs/options/#option-proxy
      proxy: {
        target: process.env.APP_SERVER_HOST,
        proxyReq: [
          function (proxyReq, req) {
            // Assign proxy 'host' header same as current request at Browsersync server
            proxyReq.setHeader('Host', req.headers.host);
          },
        ],
      },
      // https://browsersync.io/docs/options/#option-notify
      notify: false,
    },
  );
}

// Watch
function watchPaths() {
  watch(`${paths.sass}/*.scss`, project_styles);
  watch(`${paths.templates}/**/*.html`).on('change', reload);
  watch([`${paths.js}/*.js`, `!${paths.js}/*.min.js`], scripts).on(
    'change',
    reload,
  );
}

const generateAssets = parallel(project_styles, scripts);
const dev = parallel(initBrowserSync, watchPaths);

exports.default = series(generateAssets, dev);
exports['generate-assets'] = generateAssets;
exports['dev'] = dev;
