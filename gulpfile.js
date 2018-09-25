'use strict';

let gulp = require('gulp');

gulp.task('copy-bootstrap', () => {
  return gulp.src('./node_modules/bootstrap/dist/*/*.*')
    .pipe(gulp.dest('./static/vendor/bootstrap'));
});

gulp.task('copy-jquery', () => {
  return gulp.src('./node_modules/jquery/dist/jquery.min.*')
    .pipe(gulp.dest('./static/vendor/jquery'));
});

gulp.task('copy-popper', () => {
  return gulp.src('./node_modules/popper.js/dist/popper.min.*')
    .pipe(gulp.dest('./static/vendor/popper.js'));
});


gulp.task('task-start', () => {
    console.log('Start copy files');
});

gulp.task('task-end', () => {
    console.log('Copy files completed');
});


gulp.task('copy', [
    'task-start',
    'copy-bootstrap',
    'copy-jquery',
    'copy-popper',
    'task-end'
]);
