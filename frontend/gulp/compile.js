var gulp = require('gulp');
var typescript = require('gulp-tsc');

gulp.task('watch-compile', function () {
    gulp.watch('src/**/*.ts', ['compile'])
});

gulp.task('compile', function () {
    return gulp.src('src/**/*.ts')
        .pipe(typescript({ emitError: false }))
        .pipe(gulp.dest('dest/'));
});
