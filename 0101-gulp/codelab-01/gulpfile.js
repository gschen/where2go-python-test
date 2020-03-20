const gulp = require('gulp')

gulp.task('t1', function(){
    console.log('hello, t1');
})

gulp.task('t2', function(){
    console.log('hello, t2.')
})

gulp.task('t3', gulp.series('t1', 't2'))

// function demo(){

//     console.log('hello')

// }

// exports.demo = demo