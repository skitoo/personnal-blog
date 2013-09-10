
module.exports = (grunt) ->
    grunt.initConfig
        less:
            development:
                files:
                    'theme/static/css/style.css' : ['theme/static/less/style.less']
        watch:
            less:
                files: ['theme/static/less/**/*.less']
                tasks: ['less']

    

    grunt.loadNpmTasks 'grunt-contrib-watch'
    grunt.loadNpmTasks 'grunt-contrib-less'

    grunt.registerTask 'default', ['watch']