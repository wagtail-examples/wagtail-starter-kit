const browserSync = require('browser-sync').create();

browserSync.init({
    files: ['app/static_compiled/**/*', '**/templates/**/*'],
    proxy: 'http://localhost:8000',
    open: false,
    notify: false,
});
