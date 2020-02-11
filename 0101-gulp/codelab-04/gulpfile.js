// npm install --save-dev uglify-es 
// npm install --save-dev @babel/core @babel/preset-env

const gulp = require('gulp')
const babel = require('gulp-babel')
const uglifyes = require('uglify-es');
const composer = require('gulp-uglify/composer');
const uglify = composer(uglifyes, console);

gulp.task('demo', function(){
    return gulp.src('js/*.js')
    .pipe(babel())
    .pipe(uglify())
    .pipe(gulp.dest('build/'))
})