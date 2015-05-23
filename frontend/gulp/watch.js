'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync');

function isOnlyChange(event) {
  return event.type === 'changed';
}

module.exports = function(options) {
  gulp.task('watch', ['compile', 'inject'], function () {

    gulp.watch([options.src + '/*.html', 'bower.json'], ['inject']);

    gulp.watch([
      options.src + '/**/*.css',
      options.src + '/**/*.scss'
    ], function(event) {
      if(isOnlyChange(event)) {
        gulp.start('styles');
      } else {
        gulp.start('inject');
      }
    });

    gulp.watch(options.src + '/**/*.ts', function (event) {
      if(isOnlyChange(event)) {
        gulp.start('compile');
      } else {
        gulp.start('inject');
      }
    });

    // TODO: remove me
    // gulp.watch(options.src + '/app/**/*.js', function(event) {
    //   if(isOnlyChange(event)) {
    //     gulp.start('scripts');
    //   } else {
    //     gulp.start('inject');
    //   }
    // });

    gulp.watch(options.src + '/**/*.html', function(event) {
      browserSync.reload(event.path);
    });
  });
};
