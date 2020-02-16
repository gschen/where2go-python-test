// npm install --save-dev gulp-webserver

const gulp = require('gulp');
const webserver = require('gulp-webserver');

gulp.task('webserver', function() {
  gulp.src('app')
    .pipe(webserver({
      livereload: true,
      directoryListing: false,
      port: 9000,
      host: 'localhost',
      open: true
    }));
});
